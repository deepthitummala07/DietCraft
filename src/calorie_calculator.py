import pandas as pd

def calculate_bmr(weight, height, age, gender):
    if gender.lower() == 'male':
        bmr = 10*weight + 6.25*height - 5*age + 5
    else:
        bmr = 10*weight + 6.25*height - 5*age - 161
    return bmr

def calculate_calories(weight, height, age, gender, activity_level):
    bmr = calculate_bmr(weight, height, age, gender)
    activity_factors = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very active": 1.9
    }
    return bmr * activity_factors.get(activity_level.lower(), 1.2)

if __name__ == "__main__":
    print("Enter your details to calculate daily calorie needs:")
    weight = float(input("Weight (kg): "))
    height = float(input("Height (cm): "))
    age = int(input("Age (years): "))
    gender = input("Gender (male/female): ")
    activity = input("Activity level (sedentary, light, moderate, active, very active): ")

    calories = calculate_calories(weight, height, age, gender, activity)
    print(f"Your estimated daily calorie requirement is: {calories:.0f} kcal")
