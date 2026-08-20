// Copyright Merge Project. All Rights Reserved.

using UnrealBuildTool;
using System.Collections.Generic;

public class MergeTarget : TargetRules
{
	public MergeTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Game;
		DefaultBuildSettings = BuildSettingsVersion.V5;
		IncludeOrderVersion = EngineIncludeOrderVersion.Unreal5_8;
		ExtraModuleNames.Add("Merge");
	}
}
