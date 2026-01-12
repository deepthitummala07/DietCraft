import pandas as pd

# Load Indian food dataset
food_data = pd.read_csv("data/indian_food_nutrition.csv")  

def recommend_meals(calories_needed):
    recommended = []
    total_calories = 0
    food_data_sorted = food_data.sort_values(by='calories')
    for idx, row in food_data_sorted.iterrows():
        if total_calories + row['calories'] <= calories_needed:
            recommended.append(row['food_name'])
            total_calories += row['calories']
        if total_calories >= calories_needed:
            break
    return recommended, total_calories

if __name__ == "__main__":
    calories = float(input("Enter your daily calorie requirement: "))
    meals, total = recommend_meals(calories)
    print("\nRecommended Indian meals for the day:")
    for food in meals:
        print("-", food)
    print(f"\nTotal calories: {total} kcal")
