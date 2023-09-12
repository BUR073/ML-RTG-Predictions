import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load your data
rtgData = pd.read_csv('tour_guide_data.csv')

# Convert 'Date' from string to datetime format
rtgData['Date'] = pd.to_datetime(rtgData['Date'])

# Convert 'Date' to the number of days since the first date in your dataset
first_date = rtgData['Date'].min()
rtgData['Date'] = (rtgData['Date'] - first_date).dt.days

# Extract the features and target variable with explicit column naming
X = pd.DataFrame(rtgData['Date'], columns=['Date'])
y = rtgData['Number of river tour guides']

# Create the model
model = DecisionTreeClassifier()

# Fit the model to the data
model.fit(X, y)

# Convert new date to number of days since the first date
new_data_date = pd.to_datetime('2024-01-03')
days_since_first_date = (new_data_date - first_date).days

# Make predictions using the converted date with explicit column naming
new_data_df = pd.DataFrame([[days_since_first_date]], columns=['Date'])
predictions = model.predict(new_data_df)
predictions
