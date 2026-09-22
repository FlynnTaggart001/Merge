// Copyright Merge Project. All Rights Reserved.

using UnrealBuildTool;
using System.Collections.Generic;

public class MergeEditorTarget : TargetRules
{
	public MergeEditorTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Editor;
		DefaultBuildSettings = BuildSettingsVersion.V5;
		CppStandard = CppStandardVersion.Cpp20;
		IncludeOrderVersion = EngineIncludeOrderVersion.Unreal5_8;
		ExtraModuleNames.Add("Merge");
	}
}
