// Copyright Merge Project. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "MergeAttributeComponent.generated.h"

DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams(FMergeAttributeChanged, float, CurrentValue, float, MaximumValue);
DECLARE_DYNAMIC_MULTICAST_DELEGATE(FMergeCharacterDefeated);

/** Health and stamina resource rules shared by player and AI characters. */
UCLASS(ClassGroup = (Merge), meta = (BlueprintSpawnableComponent))
class MERGE_API UMergeAttributeComponent : public UActorComponent
{
	GENERATED_BODY()

public:
	UMergeAttributeComponent();

	UPROPERTY(BlueprintAssignable, Category = "Attributes|Health")
	FMergeAttributeChanged OnHealthChanged;

	UPROPERTY(BlueprintAssignable, Category = "Attributes|Stamina")
	FMergeAttributeChanged OnStaminaChanged;

	UPROPERTY(BlueprintAssignable, Category = "Attributes|Health")
	FMergeCharacterDefeated OnDefeated;

	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Attributes|Health", meta = (ClampMin = "1.0"))
	float MaximumHealth = 100.0f;

	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Attributes|Stamina", meta = (ClampMin = "0.0"))
	float MaximumStamina = 100.0f;

	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Attributes|Stamina", meta = (ClampMin = "0.0"))
	float StaminaRegenerationPerSecond = 15.0f;

	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Attributes|Stamina", meta = (ClampMin = "0.0"))
	float StaminaRegenerationDelay = 0.5f;

	UFUNCTION(BlueprintPure, Category = "Attributes|Health")
	float GetHealth() const { return Health; }

	UFUNCTION(BlueprintPure, Category = "Attributes|Health")
	float GetHealthPercent() const;

	UFUNCTION(BlueprintPure, Category = "Attributes|Health")
	bool IsDefeated() const { return bIsDefeated; }

	UFUNCTION(BlueprintPure, Category = "Attributes|Stamina")
	float GetStamina() const { return Stamina; }

	UFUNCTION(BlueprintPure, Category = "Attributes|Stamina")
	float GetStaminaPercent() const;

	UFUNCTION(BlueprintCallable, Category = "Attributes|Health")
	float ApplyDamage(float DamageAmount);

	UFUNCTION(BlueprintCallable, Category = "Attributes|Health")
	void RestoreHealth(float Amount);

	/** Returns false and spends nothing when the requested amount is unavailable. */
	UFUNCTION(BlueprintCallable, Category = "Attributes|Stamina")
	bool TrySpendStamina(float Amount);

	UFUNCTION(BlueprintCallable, Category = "Attributes|Stamina")
	void RestoreStamina(float Amount);

protected:
	virtual void BeginPlay() override;
	virtual void TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) override;

private:
	UPROPERTY(VisibleInstanceOnly, BlueprintReadOnly, Category = "Attributes|Health", meta = (AllowPrivateAccess = "true"))
	float Health = 100.0f;

	UPROPERTY(VisibleInstanceOnly, BlueprintReadOnly, Category = "Attributes|Stamina", meta = (AllowPrivateAccess = "true"))
	float Stamina = 100.0f;

	float TimeSinceStaminaSpend = 0.0f;
	bool bIsDefeated = false;
};
