Employee Performance Prediction

📌 Project Overview

This project aims to predict employee performance using Machine Learning models such as Linear Regression, Random Forest, and XGBoost. The model takes various employee-related features as input and forecasts their productivity.

🚀 Features

Data Collection: Loading and analyzing employee-related data.

Exploratory Data Analysis (EDA): Data visualization and correlation analysis.

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

Flask API for real-time predictions

🏗️ Project Structure

📂 employee-performance-prediction
│── 📂 data                     # Dataset files
│── 📂 static                   # Static files (CSS, JS, Images)
│── 📂 templates                # HTML templates (Flask)
│── 📂 models                   # Saved trained models
│── 📜 app.py                   # Flask web application
│── 📜 model_training.ipynb      # Jupyter Notebook for training models
│── 📜 requirements.txt          # Dependencies
│── 📜 README.md                 # Project Documentation

🛠️ Installation

1️⃣ Clone the Repository

git clone https://github.com/your-username/employee-performance-prediction.git
cd employee-performance-prediction

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Flask Application

python app.py

Open http://127.0.0.1:5000/ in your browser.

🏆 Best Model: XGBoost (Highest R² Score)

🔥 Usage

Train the model using model_training.ipynb

Save the best-performing model (best_model.pkl)

Deploy with Flask (app.py)

Get predictions via API
