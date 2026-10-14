from src.deep_nutrition_simulator.generator.constants import Gender

def mifflin_st_jeor(gender: Gender, age: int, height: float, weight: float) -> float:
    formulas = {
        Gender.MALE: lambda w, h, a: (10 * w) + (6.25 * h) - (5 * a) + 5,
        Gender.FEMALE: lambda w, h, a: (10 * w) + (6.25 * h) - (5 * a) - 161
    }

    return formulas[gender](weight, height, age)