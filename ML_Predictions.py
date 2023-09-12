import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load your data
rtgData = pd.read_csv('tour_guide_data.csv')

# Convert 'Date' from string to datetime format
rtgData['Date'] = pd.to_datetime(rtgData['Date'])

# Check unique years in the dataset
print("Unique years in the dataset:", rtgData['Date'].dt.year.unique())

# Separate the data for training (2023) and for making predictions (2024)
train_data = rtgData[rtgData['Date'].dt.year == 2023]
predict_data = rtgData[rtgData['Date'].dt.year == 2023]

assert not train_data.empty, "Training data for 2023 is empty!"
assert not predict_data.empty, "Prediction data for 2024 is empty!"

# Convert 'Date' to the number of days since the first date in the dataset
first_date = train_data['Date'].min()
train_data['Date'] = (train_data['Date'] - first_date).dt.days
predict_data['Date'] = (predict_data['Date'] - first_date).dt.days

# Extract the features and target variable for training
X = train_data[['Date', 'Temperature', 'Holiday']]
y = train_data['Number of river tour guides']

# Create the model
model = DecisionTreeClassifier()

# Fit the model to the data
model.fit(X, y)

# Make predictions for 2024 using the model
predictions_2024 = model.predict(predict_data[['Date', 'Temperature', 'Holiday']])

# Output predictions
for date, prediction in zip(pd.date_range(start='2024-01-01', end='2024-12-31'), predictions_2024):
    print(f"Date: {date.strftime('%Y-%m-%d')} -> Prediction: {prediction}")


