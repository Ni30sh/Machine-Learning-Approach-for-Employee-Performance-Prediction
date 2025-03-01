from flask import Flask, render_template, request, abort
import numpy as np
import pickle
import logging

app = Flask(__name__)


logging.basicConfig(level=logging.INFO)


try:
    model = pickle.load(open('best_model.pkl', 'rb'))  # Ensure correct filename
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    model = None

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/predict")
def predict_page():
    return render_template('predict.html')

@app.route("/submit")
def submit_page():
    return render_template('submit.html')

@app.route("/pred", methods=['POST'])
def predict():
    if model is None:
        logging.error("Model not loaded properly.")
        abort(500, description="Model not available")

    try:

        def get_input(key, dtype, default=0):
            value = request.form.get(key, default)
            return dtype(value) if value else default

        quarter = get_input('quarter', int)
        department = get_input('department', int)
        day = get_input('day', int)
        team = get_input('team', int)
        targeted_productivity = get_input('targeted_productivity', float)
        smv = get_input('smv', float)
        over_time = get_input('over_time', int)
        incentive = get_input('incentive', int)
        idle_time = get_input('idle_time', float)
        idle_men = get_input('idle_men', int)
        no_of_style_change = get_input('no_of_style_change', int)
        no_of_workers = get_input('no_of_workers', float)
        month = get_input('month', int)


        input_data = np.array([[quarter, department, day, team, targeted_productivity, smv,
                                over_time, incentive, idle_time, idle_men, no_of_style_change,
                                no_of_workers, month]])

        logging.info(f"Received Input Data: {input_data}")


        prediction = model.predict(input_data)
        logging.info(f"Raw Prediction Output: {prediction}")


        pred_value = float(prediction[0]) if isinstance(prediction, (list, np.ndarray)) else float(prediction)


        if pred_value <= 0.3:
            text = 'The employee is averagely productive.'
        elif 0.3 < pred_value <= 0.8:
            text = 'The employee is medium productive.'
        else:
            text = 'The employee is highly productive.'

        return render_template('submit.html', prediction_text=text)

    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        abort(400, description="Error processing request")

if __name__ == '__main__':
    app.run(debug=True)
