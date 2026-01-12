# DietCraft

DietCraft is a data science–based Python project that generates personalized dietary recommendations using Indian local food nutrition data and individual calorie requirements.

## Objective
To provide culturally relevant and healthy diet recommendations tailored to Indian food habits using data analysis and machine learning.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Machine Learning (Linear Regression)

## Project Workflow

1. **Calorie Calculation**
   - Run `calorie_calculator.py` in the `src/` folder
   - Enter your personal details:
     - Weight (kg)
     - Height (cm)
     - Age (years)
     - Gender (male/female)
     - Activity level (sedentary, light, moderate, active, very active)
   - The script calculates your estimated **daily calorie requirement**.

2. **Meal Recommendation**
   - Run `meal_recommendation.py` in the `src/` folder
   - Enter the **daily calorie requirement** obtained from the previous step
   - The script recommends a list of **Indian meals** from the dataset to meet your calorie needs

## Dataset
- `data/indian_food_nutrition.csv` contains Indian foods and their nutrition details:
  - Food Name
  - Calories
  - Protein
  - Carbohydrates
  - Fats

## Uniqueness
DietCraft stands out by using Indian local food nutrition data instead of generic Western datasets, ensuring that the diet recommendations are **culturally relevant, practical, and personalized** for Indian users.

## Future Scope
- Include regional Indian diet plans
- Develop a web-based user interface
- Add disease-specific diets (e.g., diabetes, obesity)
- Implement advanced machine learning models for better predictions

