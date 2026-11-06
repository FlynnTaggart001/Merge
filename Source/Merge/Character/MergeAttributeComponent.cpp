// Copyright Merge Project. All Rights Reserved.

#include "Character/MergeAttributeComponent.h"

UMergeAttributeComponent::UMergeAttributeComponent()
{
	PrimaryComponentTick.bCanEverTick = true;
}

void UMergeAttributeComponent::BeginPlay()
{
	Super::BeginPlay();
	Health = FMath::Max(1.0f, MaximumHealth);
	Stamina = FMath::Max(0.0f, MaximumStamina);
	OnHealthChanged.Broadcast(Health, MaximumHealth);
	OnStaminaChanged.Broadcast(Stamina, MaximumStamina);
}

void UMergeAttributeComponent::TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction)
{
	Super::TickComponent(DeltaTime, TickType, ThisTickFunction);
	if (Stamina >= MaximumStamina || StaminaRegenerationPerSecond <= 0.0f)
	{
		return;
	}

	TimeSinceStaminaSpend += DeltaTime;
	if (TimeSinceStaminaSpend >= StaminaRegenerationDelay)
	{
		RestoreStamina(StaminaRegenerationPerSecond * DeltaTime);
	}
}

float UMergeAttributeComponent::GetHealthPercent() const
{
	return MaximumHealth > 0.0f ? Health / MaximumHealth : 0.0f;
}

float UMergeAttributeComponent::GetStaminaPercent() const
{
	return MaximumStamina > 0.0f ? Stamina / MaximumStamina : 0.0f;
}

float UMergeAttributeComponent::ApplyDamage(float DamageAmount)
{
	if (bIsDefeated || DamageAmount <= 0.0f)
	{
		return 0.0f;
	}

	const float PreviousHealth = Health;
	Health = FMath::Clamp(Health - DamageAmount, 0.0f, MaximumHealth);
	const float AppliedDamage = PreviousHealth - Health;
	if (!FMath::IsNearlyZero(AppliedDamage))
	{
		OnHealthChanged.Broadcast(Health, MaximumHealth);
	}
	if (Health <= 0.0f)
	{
		bIsDefeated = true;
		OnDefeated.Broadcast();
	}
	return AppliedDamage;
}

void UMergeAttributeComponent::RestoreHealth(float Amount)
{
	if (bIsDefeated || Amount <= 0.0f)
	{
		return;
	}

	const float PreviousHealth = Health;
	Health = FMath::Clamp(Health + Amount, 0.0f, MaximumHealth);
	if (!FMath::IsNearlyEqual(PreviousHealth, Health))
	{
		OnHealthChanged.Broadcast(Health, MaximumHealth);
	}
}

bool UMergeAttributeComponent::TrySpendStamina(float Amount)
{
	if (Amount < 0.0f || Stamina < Amount)
	{
		return false;
	}
	if (Amount == 0.0f)
	{
		return true;
	}

	Stamina = FMath::Max(0.0f, Stamina - Amount);
	TimeSinceStaminaSpend = 0.0f;
	OnStaminaChanged.Broadcast(Stamina, MaximumStamina);
	return true;
}

void UMergeAttributeComponent::RestoreStamina(float Amount)
{
	if (Amount <= 0.0f)
	{
		return;
	}

	const float PreviousStamina = Stamina;
	Stamina = FMath::Clamp(Stamina + Amount, 0.0f, MaximumStamina);
	if (!FMath::IsNearlyEqual(PreviousStamina, Stamina))
	{
		OnStaminaChanged.Broadcast(Stamina, MaximumStamina);
	}
}
