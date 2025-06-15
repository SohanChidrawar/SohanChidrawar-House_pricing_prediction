# Housing Price Prediction Flask Application

This is a **Flask web application** that lets you predict **house prices** based on properties such as area, number of bedrooms, bathrooms, parking, and more.  
It uses a **Linear Regression** model trained on a CSV of housing data.

---

## 🔹Features

✅ User-friendly form to input property details.  
✅ Machine-learning algorithm (Linear Regression) trained on historical data.  
✅ Displays predicted price instantly.

---

## 🔹Tech Stack

- **Python 3**
- **Flask**
- **Scikit-Learn (Linear Regression)**
- **Pandas, Numpy**
- **Jinja2** (Flask's template engine)

---

## 🔹Installation

1️⃣ **Clone this repository:**


- git clone https://github.com/YOUR_USERNAME/House_pricing_prediction.git
- cd House_pricing_prediction

2️⃣ **Create a virtual environment:**
- python -m venv venv
- source venv/Scripts/activate  # Windows
- source venv/bin/activate  # Mac or Linux

3️⃣ **Install Required Package:**
- pip install -r requirements.txt


🔹**Training Model**
- python train.py
Training model will be saved in: app/model/trained_model.pkl

🔹**Running Application**
python app/app.py

🔹**File Structure**

House_pricing_prediction/
├── Housing.csv
├── train.py
├── app/
│ ├─ app.py
│ ├─ model/
│ └─ templates/
│    ├─ index.html
│    └─ result.html
├── requirements.txt
├── README.md
├── .gitignore

