🏆 Employee Performance Prediction

📌 Project Overview

This project leverages Machine Learning to predict employee performance based on key features. It implements Linear Regression, Random Forest, and XGBoost models, evaluates their performance, and selects the best one for deployment.

👥 Contributors

Niteesh Kumar - Data collection & Visualizing & Model Building

Jyoti Yadav  -  Data Pre-processing & Application Building.


🚀 Features

Data Collection: Importing and analyzing employee data.

Exploratory Data Analysis (EDA): Data visualization, correlation analysis, and descriptive statistics.

Data Preprocessing: Handling missing values, encoding categorical data, and feature engineering.

Model Training & Evaluation:

Linear Regression

Random Forest

XGBoost

Performance Metrics:

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

R² Score

Best Model Selection & Deployment

Flask API for real-time predictions.

Install Dependencies

pip install -r requirements.txt

Run the Flask Application

python app.py

Open http://127.0.0.1:5000/ in your browser.

📊 Model Performance

![image](https://github.com/user-attachments/assets/56669c49-8a2b-4ddd-ae78-7ea0b19251f1)


🏆 Best Model: XGBoost (Highest R² Score)

🔥 Usage

Train the model using model_training.ipynb

Save the best-performing model (best_model.pkl)

Deploy with Flask (app.py)

Get predictions via API


