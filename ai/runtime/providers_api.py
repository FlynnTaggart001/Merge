"""HTTP provider adapters for OpenAI, Gemini and xAI.

Secrets are read only from environment variables. Network operations use the
shared timeout/retry policy and never contain credentials in logs or errors.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from dataclasses import dataclass

from .retry import RetryPolicy, execute_with_retry


@dataclass
class APIResponse:
    provider_id: str
    text: str


TRANSIENT_HTTP_STATUS = {408, 409, 425, 429, 500, 502, 503, 504}


def _retryable(exc: Exception) -> bool:
    if isinstance(exc, (TimeoutError, urllib.error.URLError)):
        return True
    return isinstance(exc, urllib.error.HTTPError) and exc.code in TRANSIENT_HTTP_STATUS


def _post_json(url: str, headers: dict[str, str], payload: dict) -> dict:
    policy = RetryPolicy(
        max_retries=int(os.getenv("MERGE_MAX_RETRIES", "2")),
        timeout_seconds=float(os.getenv("AI_REQUEST_TIMEOUT_SECONDS", "60")),
    )

    def operation() -> dict:
        request = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={**headers, "Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=policy.timeout_seconds) as response:
            return json.loads(response.read().decode("utf-8"))

    return execute_with_retry(operation, policy, _retryable)


def openai_execute(prompt: str) -> APIResponse:
    key = os.environ["OPENAI_API_KEY"]
    model = os.getenv("OPENAI_MODEL", "gpt-5")
    data = _post_json(
        "https://api.openai.com/v1/responses",
        {"Authorization": f"Bearer {key}"},
        {"model": model, "input": prompt},
    )
    return APIResponse("openai", data.get("output_text", ""))


def gemini_execute(prompt: str) -> APIResponse:
    key = os.environ["GEMINI_API_KEY"]
    model = os.getenv("GEMINI_MODEL", "gemini-2.5-pro")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
    data = _post_json(url, {}, {"contents": [{"parts": [{"text": prompt}]}]})
    text = ""
    for candidate in data.get("candidates", []):
        for part in candidate.get("content", {}).get("parts", []):
            text += part.get("text", "")
    return APIResponse("gemini", text)


def grok_execute(prompt: str) -> APIResponse:
    key = os.environ["XAI_API_KEY"]
    model = os.getenv("XAI_MODEL", "grok-4.5")
    data = _post_json(
        "https://api.x.ai/v1/responses",
        {"Authorization": f"Bearer {key}"},
        {"model": model, "input": prompt},
    )
    return APIResponse("grok", data.get("output_text", ""))
