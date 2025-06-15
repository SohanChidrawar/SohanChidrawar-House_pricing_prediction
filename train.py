# train.py
import numpy as np
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Loading data from CSV
data = pd.read_csv('Housing.csv')

# # Handle missing values if any
# data = data.fillna(data.mean())  

# Convert 'yes'/'no' to 1/0
yes_no_columns = ['mainroad', 'guestroom', 'basement',
                   'hotwaterheating', 'airconditioning', 'prefarea']

for col in yes_no_columns:
    data[col] = data[col].apply(lambda x: 1 if x == 'yes' else 0)

# Convert furnishingstatus to dummy variables
data = pd.get_dummies(data, columns=['furnishingstatus'], drop_first=True)

# Separate into features and target
X = data.drop('price', axis=1) 
y = data['price']

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Save Model
with open('app/model/trained_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved.")



