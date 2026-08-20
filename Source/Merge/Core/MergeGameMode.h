// Copyright Merge Project. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/GameModeBase.h"
#include "MergeGameMode.generated.h"

/**
 * Global game rules for Merge.
 * Owns default pawn / controller classes and high-level match flow hooks.
 */
UCLASS()
class MERGE_API AMergeGameMode : public AGameModeBase
{
	GENERATED_BODY()

public:
	AMergeGameMode();
};
