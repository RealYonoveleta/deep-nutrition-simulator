from enum import Enum

class Gender(Enum):
    MALE = "male",
    FEMALE = "female"

class ActivityLevel(Enum):
    SEDENTARY = 1.2        # Little to no exercise
    LIGHTLY_ACTIVE = 1.375 # Light exercise 1-3 days/week
    MODERATELY_ACTIVE = 1.55 # Moderate exercise 3-5 days/week
    VERY_ACTIVE = 1.725    # Hard exercise 6-7 days/week
    EXTRA_ACTIVE = 1.9     # Very hard exercise, physical job or 2x training

class FitnessGoal(Enum):
    BULK = {
        "protein": 0.25,
        "carbohydrates": 0.50,
        "fats": 0.25,
        "caloric_mod": 500 
    }
    CUT = {
        "protein": 0.40,
        "carbohydrates": 0.35,
        "fats": 0.25,
        "caloric_mod": -400
    }
    MAINTAIN = {
        "protein": 0.30,
        "carbohydrates": 0.45,
        "fats": 0.25,
        "caloric_mod": 0.00
    }