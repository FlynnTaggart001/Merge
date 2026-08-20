// Copyright Merge Project. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "MergeDataTypes.generated.h"

/**
 * Shared data-oriented types for future data assets / tables.
 * Keep pure data here; no heavy logic.
 */

USTRUCT(BlueprintType)
struct FMergeAttributeBlock
{
	GENERATED_BODY()

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Attributes")
	float Health = 100.f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Attributes")
	float MaxHealth = 100.f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Attributes")
	float Stamina = 100.f;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Attributes")
	float MaxStamina = 100.f;
};
