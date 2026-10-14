from src.deep_nutrition_simulator.generator.metabolic_calculator import MetabolicCalculator
from src.deep_nutrition_simulator.generator.constants import Gender, ActivityLevel, FitnessGoal
from src.deep_nutrition_simulator.generator.diet import generate_daily_intake

import random

class Person():
    def __init__(self, gender: Gender, height: float, weight: float, age: int, activity_level: ActivityLevel, fitness_goal: FitnessGoal):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.activity_level = activity_level
        self.fitness_goal = fitness_goal

    def get_bmr(self):

        return MetabolicCalculator.calculate_bmr(
            gender=self.gender,
            weight=self.weight,
            height=self.height,
            age=self.age
        )

    def get_tdee(self):

        bmr = self.get_bmr()

        return MetabolicCalculator.calculate_tdee(
            bmr=bmr,
            activity_level=self.activity_level
        )

    def eat(self, sigma=250):

        tdee = self.get_tdee()

        target_calories = tdee + self.fitness_goal.value["caloric_mod"]

        noise = random.gauss(0, sigma)

        target_calories_with_noise = target_calories + noise

        daily_intake = generate_daily_intake(self.fitness_goal, target_calories_with_noise)

        balance = daily_intake["calories"] - tdee

        CALORIES_PER_1KG = 7700

        self.weight += balance / CALORIES_PER_1KG

        return {
            "intake": daily_intake,
            "balance": balance
        }
