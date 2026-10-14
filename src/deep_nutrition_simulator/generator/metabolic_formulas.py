from src.deep_nutrition_simulator.generator.constants import BmrFormula, Gender

def mifflin_st_jeor(gender: Gender, age: int, height: float, weight: float, **kwargs) -> float:
    match gender:
        case Gender.MALE:
            return (10 * weight) + (6.25 * height) - (5 * age) + 5

        case Gender.FEMALE:
            return (10 * weight) + (6.25 * height) - (5 * age) - 161

        case _:
            raise ValueError(f"Unsupported gender: {gender!r}")

def katch_mcardle(weight: float, body_fat_pctg: float, **kwargs) -> float:
    lbm = weight * (1 - body_fat_pctg)

    return 370 + (21.6 * lbm) 

BMR_FORMULAS = {
    BmrFormula.MSJ: mifflin_st_jeor, 
    BmrFormula.KM: katch_mcardle
}