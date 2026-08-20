// Copyright Merge Project. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Engine/GameInstance.h"
#include "MergeGameInstance.generated.h"

/**
 * Global entry point for persistent systems.
 * Keep this class lightweight: it owns/references long-lived subsystems,
 * it does not implement gameplay rules itself.
 */
UCLASS()
class MERGE_API UMergeGameInstance : public UGameInstance
{
	GENERATED_BODY()

public:
	virtual void Init() override;
	virtual void Shutdown() override;

protected:
	/** Placeholder for future subsystem registration / init order. */
	void InitializeCoreSystems();
};
