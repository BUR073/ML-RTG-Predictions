import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load your data
rtgData = pd.read_csv('tour_guide_data.csv')

# Extract the features and target variable
X = rtgData[['Temperature', 'Holiday']]  # Use double brackets to create a DataFrame
y = rtgData['Number of river tour guides']

# Create the model
model = DecisionTreeClassifier()

# Fit the model to the data
model.fit(X, y)

# Make predictions
new_data = [[-2, True], [64, False], [32, True]]
new_data_df = pd.DataFrame(new_data, columns=['Temperature', 'Holiday'])
predictions = model.predict(new_data_df)
predictions
