// Copyright Merge Project. All Rights Reserved.

#include "Core/MergeGameInstance.h"

void UMergeGameInstance::Init()
{
	Super::Init();
	InitializeCoreSystems();
}

void UMergeGameInstance::Shutdown()
{
	Super::Shutdown();
}

void UMergeGameInstance::InitializeCoreSystems()
{
	// Future: register / warm up persistent subsystems (save, audio mix, etc.)
}
