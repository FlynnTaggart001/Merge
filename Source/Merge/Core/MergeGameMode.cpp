// Copyright Merge Project. All Rights Reserved.

#include "Core/MergeGameMode.h"
#include "Character/MergeCharacter.h"
#include "Core/MergePlayerController.h"

AMergeGameMode::AMergeGameMode()
{
	DefaultPawnClass = AMergeCharacter::StaticClass();
	PlayerControllerClass = AMergePlayerController::StaticClass();
}
