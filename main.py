from src.deep_nutrition_simulator.generator.person import Person
from src.deep_nutrition_simulator.generator.constants import Gender, ActivityLevel

p1 = Person(
    gender=Gender.MALE,
    height=169,
    weight=69.3,
    age=28,
    activity_level=ActivityLevel.LIGHTLY_ACTIVE
)

print(f"BMR: {p1.get_bmr()} kcal")
print(f"TDEE: {p1.get_tdee()} kcal")