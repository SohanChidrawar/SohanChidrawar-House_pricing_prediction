from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('app/model/trained_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """ Get form data """
    area = float(request.form['area'])
    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])
    stories = float(request.form['stories'])
    mainroad = 1 if request.form['mainroad'].lower() == 'yes' else 0
    guestroom = 1 if request.form['guestroom'].lower() == 'yes' else 0
    basement = 1 if request.form['basement'].lower() == 'yes' else 0
    hotwaterheating = 1 if request.form['hotwaterheating'].lower() == 'yes' else 0
    airconditioning = 1 if request.form['airconditioning'].lower() == 'yes' else 0
    parking = float(request.form['parking'])
    prefarea = 1 if request.form['prefarea'].lower() == 'yes' else 0
    
    furnishing = request.form['furnishingstatus'].lower()
    semi_furnished = 1 if furnishing == 'semi-furnished' else 0
    unfurnished = 1 if furnishing == 'unfurnished' else 0
    
    features = [area, bedrooms, bathrooms, stories, mainroad, guestroom,
                basement, hotwaterheating, airconditioning, parking,
                prefarea, semi_furnished, unfurnished]
    final_features = [np.array(features)]

    """ Perform Prediction """
    prediction = model.predict(final_features)[0]

    return render_template('result.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
