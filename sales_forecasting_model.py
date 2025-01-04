import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load the datasets
train_data = pd.read_csv('c:/Users/HP 830 G6/Desktop/KAIM/week-4/data/train.csv', low_memory=False)  # Update with your actual path
store_data = pd.read_csv('c:/Users/HP 830 G6/Desktop/KAIM/week-4/data/store.csv', low_memory=False)  # Update with your actual path

# Merge the training data with the store data
merged_data = pd.merge(train_data, store_data, on='Store', how='left')

# Convert date column to datetime format and extract features
merged_data['Date'] = pd.to_datetime(merged_data['Date'])
merged_data['Year'] = merged_data['Date'].dt.year
merged_data['Month'] = merged_data['Date'].dt.month
merged_data['Day'] = merged_data['Date'].dt.day

# Prepare the data
X = merged_data.drop(['Sales', 'Date'], axis=1)  # Drop non-numeric columns

# Convert categorical variables to numeric using one-hot encoding
X = pd.get_dummies(X, drop_first=True)

y = merged_data['Sales']  # Target variable

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make Predictions
predictions = model.predict(X_test)

# Evaluate the Model
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Function to make predictions
def predict_sales(input_data):
    return model.predict(input_data)