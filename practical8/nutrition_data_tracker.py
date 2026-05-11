class food_item:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

def calculate_daily_nutrition(food_list):
    total_calories = 0.0
    total_protein = 0.0
    total_carbs = 0.0
    total_fat = 0.0

    for item in food_list:
        total_calories += item.calories
        total_protein += item.protein
        total_carbs += item.carbs
        total_fat += item.fat

    print("Total Calories:", total_calories)
    print("Total Protein:", total_protein)
    print("Total Carbs:", total_carbs)
    print("Total Fat:", total_fat)

    if total_calories > 2500:
        print("Warning: Calories exceed 2500 kcal")
    if total_fat > 90:
        print("Warning: Fat exceeds 90g")

if __name__ == "__main__":
    apple = food_item("Apple", 60, 0.3, 15, 0.5)
    egg = food_item("Egg", 78, 6.3, 0.6, 5.3)
    pizza = food_item("Pizza", 285, 12, 30, 14)
    burger = food_item("Burger", 520, 26, 40, 28)

    print("=== Example 1: Normal Diet ===")
    diet1 = [apple, egg]
    calculate_daily_nutrition(diet1)

    print()
    print("=== Example 2: High-Calorie Diet ===")
    diet2 = [pizza, burger, pizza, burger]
    calculate_daily_nutrition(diet2)