# Bakery Loaf Prediction with KNN Regression

## Overview

Starting from a bakery dataset with weather, weekend/holiday status, and game information, students will implement K-Nearest Neighbors regression to predict how many loaves of bread to bake for a given day. This assignment demonstrates practical machine learning by solving a real-world business problem using historical sales data to make informed predictions about future demand.

## Learning Objectives

- Demonstrate regression using K-Nearest Neighbors to predict numerical outcomes
- Extract features and target variables from a pandas DataFrame
- Train a KNN regression model using scikit-learn
- Make predictions for new data points using a trained model
- Apply machine learning to solve a practical business problem (predicting number of loaves to bake)

## Requirements

1. Implement the `prepare_features_and_target()` function to extract feature columns (weather, weekend_holiday, game_on) into X and target column (loaves) into y as numpy arrays
2. Implement the `train_knn_model()` function to create and train a KNeighborsRegressor with k=4 neighbors
3. Implement the `predict_loaves_for_today()` function to make predictions for new conditions using the trained model
4. Complete all TODO items in the function bodies to enable the main program to run successfully

## Getting Started

The starter code provides a complete framework for a bakery prediction system. It already includes:
- A `load_bakery_data()` function that creates a pandas DataFrame with 20 days of historical bakery data
- A main function that loads data, displays it, and attempts to make a prediction for today's conditions (weather=4, weekend_holiday=1, game_on=0)
- Visualization code to create a scatter plot of weather vs loaves sold
- All necessary imports for pandas, numpy, scikit-learn, and matplotlib

The bakery dataset contains 20 historical records with features for weather (1-5 scale), weekend/holiday status (0/1), game status (0/1), and the number of loaves sold on each day.

## Implementation Steps

### Extract Features and Target from DataFrame

In the `prepare_features_and_target()` function, you need to separate the input features from the target variable. The features are the three columns that help predict sales: weather, weekend_holiday, and game_on. The target is the loaves column that we want to predict.

For example, if the DataFrame has weather=[3,5,2], weekend_holiday=[0,1,0], game_on=[0,1,0], and loaves=[42,95,30], then X should be a 3×3 array containing the first three columns, and y should be a 1D array [42,95,30].

```python
def prepare_features_and_target(df):
    # Extract the feature columns (weather, weekend_holiday, game_on) into X
    X = df[['weather', 'weekend_holiday', 'game_on']].values
    
    # Extract the target column (loaves) into y
    y = df['loaves'].values
    
    return X, y
```

### Create and Train KNN Regression Model

In the `train_knn_model()` function, you need to create a K-Nearest Neighbors regression model and train it on the historical data. KNN regression works by finding the k closest data points to a new input and averaging their target values.

For this bakery problem, when predicting loaves for today (weather=4, weekend_holiday=1, game_on=0), the model will find the 4 most similar historical days and average their loaf sales.

```python
def train_knn_model(X, y, k=4):
    # Create a KNeighborsRegressor with n_neighbors=k
    model = KNeighborsRegressor(n_neighbors=k)
    
    # Fit the model using X and y
    model.fit(X, y)
    
    return model
```

### Make Predictions for New Conditions

In the `predict_loaves_for_today()` function, you need to format today's conditions as a feature array and use the trained model to make a prediction. The model expects a 2D array even for a single prediction, so you'll need to reshape the input appropriately.

For today's conditions (weather=4, weekend_holiday=1, game_on=0), the function should return approximately 70.5 loaves based on the 4 nearest neighbors in the historical data.

```python
def predict_loaves_for_today(model, weather, weekend_holiday, game_on):
    # Create a feature array for today's conditions
    today_features = np.array([[weather, weekend_holiday, game_on]])
    
    # Use the model to predict loaves for today
    prediction = model.predict(today_features)[0]
    
    return prediction
```

## Complete Program

```python
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def load_bakery_data():
    """
    Load the bakery data with weather, weekend/holiday, game status, and loaves sold.
    Returns a pandas DataFrame with the bakery data.
    """
    # Create the bakery dataset with hardcoded values
    data = {
        'weather': [3, 5, 2, 4, 1, 5, 3, 4, 2, 5, 1, 3, 4, 2, 5, 3, 4, 1, 2, 4],
        'weekend_holiday': [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
        'game_on': [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
        'loaves': [42, 95, 30, 72, 38, 55, 78, 50, 58, 85, 22, 52, 88, 44, 70, 65, 62, 48, 70, 75]
    }
    return pd.DataFrame(data)

def prepare_features_and_target(df):
    """
    Separate the features (weather, weekend_holiday, game_on) from the target (loaves).
    Returns X (features) and y (target) as numpy arrays.
    """
    # Extract the feature columns (weather, weekend_holiday, game_on) into X
    X = df[['weather', 'weekend_holiday', 'game_on']].values
    
    # Extract the target column (loaves) into y
    y = df['loaves'].values
    
    return X, y

def train_knn_model(X, y, k=4):
    """
    Train a KNN regression model with k neighbors.
    Returns the trained model.
    """
    # Create a KNeighborsRegressor with n_neighbors=k
    model = KNeighborsRegressor(n_neighbors=k)
    
    # Fit the model using X and y
    model.fit(X, y)
    
    return model

def predict_loaves_for_today(model, weather, weekend_holiday, game_on):
    """
    Predict how many loaves to bake for today given the conditions.
    Returns the predicted number of loaves.
    """
    # Create a feature array for today's conditions
    today_features = np.array([[weather, weekend_holiday, game_on]])
    
    # Use the model to predict loaves for today
    prediction = model.predict(today_features)[0]
    
    return prediction

def main():
    """
    Main function to demonstrate KNN regression for bakery loaf prediction.
    Today's conditions: weekend day with good weather (weather=4, weekend_holiday=1, game_on=0)
    """
    # Load the bakery data
    df = load_bakery_data()
    print("Bakery Data:")
    print(df)
    print()
    
    # Prepare features and target
    X, y = prepare_features_and_target(df)
    print("Features shape:", X.shape if X is not None else "Not implemented")
    print("Target shape:", y.shape if y is not None else "Not implemented")
    print()
    
    # Train KNN model with k=4
    model = train_knn_model(X, y, k=4)
    print("KNN model trained with k=4")
    print()
    
    # Today's conditions: weekend day with good weather
    today_weather = 4  # Good weather (scale 1-5)
    today_weekend_holiday = 1  # It's a weekend
    today_game_on = 0  # No game today
    
    print(f"Today's conditions: Weather={today_weather}, Weekend/Holiday={today_weekend_holiday}, Game={today_game_on}")
    
    # Predict loaves for today
    predicted_loaves = predict_loaves_for_today(model, today_weather, today_weekend_holiday, today_game_on)
    print(f"Predicted loaves to bake: {predicted_loaves if predicted_loaves is not None else 'Not implemented'}")
    
    # Create a simple visualization of the data
    plt.figure(figsize=(10, 6))
    plt.scatter(df['weather'], df['loaves'], alpha=0.7, label='Historical Data')
    plt.xlabel('Weather (1-5 scale)')
    plt.ylabel('Loaves Sold')
    plt.title('Bakery Sales vs Weather')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.close()
    
if __name__ == "__main__":
    main()
```

## Testing

To test your implementation:
1. Commit and push your changes to your repository
2. Visit your repository on github.com to see the autograder results
3. The autograder will run automatically and show pass/fail status for each test
4. If tests fail, check the error messages and review your implementation

## Grading Rubric

| Test Case | Points | Description |
|-----------|--------|-------------|
| Program executes without errors | 20 | Code runs to completion without exceptions |
| prepare_features_and_target returns correct shapes | 25 | X has shape (20, 3) and y has shape (20,) |
| train_knn_model creates working model | 25 | KNN model trains successfully with k=4 |
| predict_loaves_for_today returns correct prediction | 30 | Prediction for today's conditions returns approximately 70.5 |

## Tips and Hints

- Use `df[['col1', 'col2', 'col3']].values` to extract multiple columns as a numpy array for features
- Use `df['column_name'].values` to extract a single column as a numpy array for the target
- The KNeighborsRegressor constructor takes `n_neighbors` as a parameter to set k
- Remember to call `.fit(X, y)` on your model to train it with the historical data
- When making predictions, wrap single data points in double brackets: `np.array([[value1, value2, value3]])`
- The `.predict()` method returns an array, so use `[0]` to get the first (and only) prediction value
- KNN regression works by finding the k nearest neighbors and averaging their target values - no complex math required!

# Lab Report Template

## Student Information
**Name:** [Your Name]
**Date:** [Date]
**Algorithm Analysis:** K-Nearest Neighbors (KNN) Regression for Bakery Loaf Prediction

---

## Algorithm Understanding

**What type of problem is this algorithm solving?**
[Your answer — supervised learning / regression / prediction problem]

**How does KNN regression differ from KNN classification?**
[Your explanation]

**What does the "K" in KNN represent, and why did we choose k=4 for this problem?**
[Your answer]

**In your own words, explain how the model produces a prediction for a new day.**
[Your explanation — should mention finding the k closest historical days and averaging their loaf counts]

---

## Implementation Questions

**Why do we separate the DataFrame into features (X) and target (y) before training?**
[Your explanation]

**Why must the input to `model.predict()` be a 2D array (e.g., `[[4, 1, 0]]`) instead of a 1D array (`[4, 1, 0]`)?**
[Your explanation]

**What does `.fit(X, y)` actually do for a KNN model? (Hint: it's different from most other ML algorithms.)**
[Your explanation — KNN is a "lazy learner" that mostly just stores the data]

**Why do we use `.values` when extracting columns from the DataFrame?**
[Your explanation]

---

## Extension: Choosing K

**What would happen if we set k=1? What are the risks?**
[Your explanation — overfitting, sensitive to noise]

**What would happen if we set k=20 (the size of the entire dataset)? What does the model become?**
[Your explanation — every prediction would be the global average]

**How would you decide what value of k is best for a given dataset?**
[Your explanation — cross-validation, error metrics on a validation set]

---

## Extension: Distance and Feature Scaling

**KNN uses distance to find "nearest" neighbors. Our features have very different ranges: weather is 1–5, but weekend_holiday and game_on are 0/1. Why could this be a problem?**
[Your explanation — features with larger ranges dominate the distance calculation]

**Give an example of two days where the weather feature would unfairly dominate the distance calculation.**
[Your example]

**How would you modify the data preparation step to fix this? (Hint: look up "feature scaling" or "StandardScaler".)**
[Your explanation]

---

## Reflection Questions

**What is a limitation of KNN regression? Provide a scenario where it would make a poor prediction.**
[Your explanation — e.g., predicting a day with conditions far outside any historical data]

**Our dataset only has 20 days of data. How might the predictions change if we had 2,000 days of data instead?**
[Your explanation]

**What other features (beyond weather, weekend/holiday, and game day) could the bakery collect to improve predictions?**
[Your answer — e.g., temperature, season, local events, day of week, social media buzz]

**KNN is sometimes called a "lazy learning" algorithm because it does almost no work during training. What is the tradeoff at prediction time?**
[Your explanation — slower predictions, must compare against every training point]

**The autograder expects a prediction of approximately 70.5 loaves for today's conditions. Manually look at the dataset and identify which 4 historical days you think the model is averaging. Do their loaf counts average to 70.5?**
[Your analysis]

**Why might a bakery prefer a slightly inaccurate ML prediction over a human guess for daily loaf counts?**
[Your explanation — consistency, scalability, data-driven decisions, reduced waste]

**If the bakery wanted to MINIMIZE waste (unsold loaves) rather than just predict accurately, how might you change the approach?**
[Your explanation — e.g., predict slightly under, use a different loss function, factor in cost of waste vs. lost sales]
