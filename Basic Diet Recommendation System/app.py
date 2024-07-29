from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Dummy function to simulate diet recommendations
def get_recommendations(gender, food_category, food_type):
    # Here, you would add your actual logic to get diet recommendations
    return [
        {"meal": "Breakfast", "item": "Oatmeal", "calories": 150},
        {"meal": "Lunch", "item": "Grilled Chicken Salad", "calories": 300},
        {"meal": "Dinner", "item": "Steamed Vegetables", "calories": 200},
    ]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    gender = request.form['gender']
    food_category = request.form['food_category']
    food_type = request.form['food_type']
    recommendations = get_recommendations(gender, food_category, food_type)
    return render_template('recommendations.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
