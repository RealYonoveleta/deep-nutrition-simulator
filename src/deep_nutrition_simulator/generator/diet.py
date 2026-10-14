from src.deep_nutrition_simulator.generator.constants import FitnessGoal
import random

KCAL_PER_GRAM = {
    "protein": 4,
    "carbohydrates": 4,
    "fats": 9
}

def generate_daily_intake(goal: FitnessGoal, target_calories: float, macro_sigma=0.05):

    base_ratios = goal.value

    random_p = base_ratios["protein"] + random.gauss(0, macro_sigma)
    random_c = base_ratios["carbohydrates"] + random.gauss(0, macro_sigma)
    random_f = base_ratios["fats"] + random.uniform(0, macro_sigma)

    total_random_ratio = random_p + random_c + random_f

    final_ratio_p = random_p / total_random_ratio
    final_ratio_c = random_c / total_random_ratio
    final_ratio_f = random_f / total_random_ratio

    daily_protein_calories = target_calories * final_ratio_p
    daily_carbohydrate_calories = target_calories * final_ratio_c
    daily_fat_calories = target_calories * final_ratio_f 

    daily_protein= daily_protein_calories / KCAL_PER_GRAM["protein"]
    daily_carbohydrates = daily_carbohydrate_calories / KCAL_PER_GRAM["carbohydrates"]
    daily_fats = daily_fat_calories / KCAL_PER_GRAM["fats"]

    total_calories = daily_protein_calories + daily_carbohydrate_calories + daily_fat_calories

    return {
        "calories": round(total_calories, 1),
        "protein": round(daily_protein, 1),
        "carbohydrates": round(daily_carbohydrates, 1),
        "fats": round(daily_fats, 1)
    }