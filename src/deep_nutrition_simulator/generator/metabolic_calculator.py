from src.deep_nutrition_simulator.generator.constants import Gender, ActivityLevel
from src.deep_nutrition_simulator.generator.metabolic_formulas import mifflin_st_jeor

class MetabolicCalculator:

    @staticmethod
    def calculate_bmr(gender: Gender, weight: float, height: float, age: int, bmr_formula = "msj") -> float:

        formulas = {
            "msj": mifflin_st_jeor
        }

        formula = formulas[bmr_formula]

        return formula(gender, age, height, weight)

    @staticmethod
    def calculate_tdee(bmr: float, activity_level: ActivityLevel) -> float:
        return bmr * activity_level.value