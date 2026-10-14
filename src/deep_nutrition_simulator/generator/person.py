from src.deep_nutrition_simulator.generator.metabolic_calculator import MetabolicCalculator

from src.deep_nutrition_simulator.generator.constants import Gender, ActivityLevel

class Person():
    def __init__(self, gender: Gender, height: float, weight: float, age: int, activity_level: ActivityLevel):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.activity_level = activity_level

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