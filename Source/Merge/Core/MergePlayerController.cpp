// Copyright Merge Project. All Rights Reserved.

#include "Core/MergePlayerController.h"
#include "EnhancedInputSubsystems.h"

AMergePlayerController::AMergePlayerController()
{
}

void AMergePlayerController::BeginPlay()
{
	Super::BeginPlay();

	if (UEnhancedInputLocalPlayerSubsystem* Subsystem =
		ULocalPlayer::GetSubsystem<UEnhancedInputLocalPlayerSubsystem>(GetLocalPlayer()))
	{
		if (DefaultMappingContext)
		{
			Subsystem->AddMappingContext(DefaultMappingContext, 0);
		}
	}
}

void AMergePlayerController::SetupInputComponent()
{
	Super::SetupInputComponent();
	// Character binds its own Enhanced Input actions.
}
