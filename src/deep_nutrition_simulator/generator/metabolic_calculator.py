from src.deep_nutrition_simulator.generator.constants import ActivityLevel, BmrFormula
from src.deep_nutrition_simulator.generator.metabolic_formulas import BMR_FORMULAS

class MetabolicCalculator:

    @staticmethod
    def calculate_bmr(bmr_formula: BmrFormula = BmrFormula.KM, **kwargs) -> float:
        return BMR_FORMULAS[bmr_formula](**kwargs)

    @staticmethod
    def calculate_tdee(bmr: float, activity_level: ActivityLevel) -> float:
        return bmr * activity_level.value