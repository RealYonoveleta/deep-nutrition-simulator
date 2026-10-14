from src.deep_nutrition_simulator.generator.person import Person
from src.deep_nutrition_simulator.generator.constants import Gender, ActivityLevel, FitnessGoal

p1 = Person(
    gender=Gender.MALE,
    height=169,
    weight=69.3,
    age=28,
    activity_level=ActivityLevel.LIGHTLY_ACTIVE,
    fitness_goal=FitnessGoal.BULK
)

print(f"BMR: {p1.get_bmr()} kcal")
print(f"TDEE: {p1.get_tdee()} kcal")

for i in range(200):
    daily_info = p1.eat(sigma=250)
    print(
        f"Daily balance: {daily_info["balance"]:.2f} / Balance: {daily_info["balance"]:.2f} / Weight: {p1.weight:.2f}"
    )