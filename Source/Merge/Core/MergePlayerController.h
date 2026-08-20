// Copyright Merge Project. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/PlayerController.h"
#include "MergePlayerController.generated.h"

class UInputMappingContext;

/**
 * Player-facing controller.
 * Owns input mapping contexts and high-level UI / camera orchestration.
 * Gameplay logic stays on the Character / components.
 */
UCLASS()
class MERGE_API AMergePlayerController : public APlayerController
{
	GENERATED_BODY()

public:
	AMergePlayerController();

protected:
	virtual void BeginPlay() override;
	virtual void SetupInputComponent() override;

	/** Default mapping context applied on possess. */
	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Input")
	TObjectPtr<UInputMappingContext> DefaultMappingContext;
};
