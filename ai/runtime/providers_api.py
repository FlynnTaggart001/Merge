"""Legacy metered-API adapters retained for compatibility only.

The selected Merge toolchain is ChatGPT Plus, Claude Code, and Wingman Premium.
These OpenAI/Gemini/xAI HTTP functions are NOT the selected integrations and
must not be routed by default. ChatGPT Plus is a subscription interface, not an
OpenAI API credential or API credit balance. Secrets are read from environment
variables; never commit them.
"""

from __future__ import annotations

import json
import os
import urllib.request
from dataclasses import dataclass


@dataclass
class APIResponse:
    provider_id: str
    text: str


def _post_json(url: str, headers: dict[str, str], payload: dict) -> dict:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={**headers, "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=180) as response:
        return json.loads(response.read().decode("utf-8"))


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
    data = _post_json(
        url,
        {},
        {"contents": [{"parts": [{"text": prompt}]}]},
    )
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
