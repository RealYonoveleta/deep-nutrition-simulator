from src.deep_nutrition_simulator.generator.metabolic_calculator import MetabolicCalculator
from src.deep_nutrition_simulator.generator.constants import Gender, ActivityLevel, FitnessGoal, BmrFormula, CALORIES_PER_1KG
from src.deep_nutrition_simulator.generator.diet import generate_daily_intake

import random

class Person():
    def __init__(self, gender: Gender, height: float, weight: float, age: int, body_fat_pctg: float, activity_level: ActivityLevel, fitness_goal: FitnessGoal):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.activity_level = activity_level
        self.fitness_goal = fitness_goal
        self.body_fat_pctg = body_fat_pctg

    def get_bmr(self):

        args = {
            "gender": self.gender,
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            "body_fat_pctg": self.body_fat_pctg
        }

        return MetabolicCalculator.calculate_bmr(**args)

    def get_tdee(self):

        bmr = self.get_bmr()

        return MetabolicCalculator.calculate_tdee(
            bmr=bmr,
            activity_level=self.activity_level
        )

    def eat(self, target_calories_sigma=250, fat_partition_sigma=0.03):

        tdee = self.get_tdee()

        target_calories = tdee + self.fitness_goal.value["caloric_mod"]

        noise = random.gauss(0, target_calories_sigma)

        target_calories_with_noise = target_calories + noise

        daily_intake = generate_daily_intake(self.fitness_goal, target_calories_with_noise)

        balance = daily_intake["calories"] - tdee

        weight_change = balance / CALORIES_PER_1KG

        current_fat_kg = self.weight * self.body_fat_pctg

        base_fat_partition = self.fitness_goal.value["fat_partition"]

        partition_noise = random.gauss(0, fat_partition_sigma)
        final_fat_partition = base_fat_partition + partition_noise

        final_fat_partition = max(0, min(1, final_fat_partition))

        fat_change = weight_change * final_fat_partition

        new_weight = self.weight + weight_change
        new_fat_kg = current_fat_kg + fat_change

        self.weight = new_weight

        self.body_fat_pctg = new_fat_kg / new_weight if new_weight > 0 else self.body_fat_pctg

        return {
            "intake": daily_intake,
            "balance": balance,
            "weight_after": round(self.weight, 2),
            "bf_after": round(self.body_fat_pctg, 4)
        }
