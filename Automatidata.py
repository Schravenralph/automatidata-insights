# automatidata_linear_regression.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Set visual style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)


def load_data(url):
    """Loads dataset from a given URL into a pandas DataFrame."""
    df = pd.read_csv(url)
    return df


def engineer_features(df):
    """Extracts date/time features and renames columns."""
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    df['hour'] = df['pickup_datetime'].dt.hour
    df['day'] = df['pickup_datetime'].dt.day
    df['month'] = df['pickup_datetime'].dt.month
    df['day_of_week'] = df['pickup_datetime'].dt.dayofweek
    return df


def clean_data(df):
    """Performs basic cleaning: removes invalid fares and distances."""
    df = df.dropna()
    df = df[(df['fare_amount'] > 0) & (df['trip_distance'] > 0)]
    return df


def plot_distributions(df):
    """Visualizes fare and distance distributions."""
    sns.histplot(df['fare_amount'], bins=50, kde=True)
    plt.title('Fare Amount Distribution')
    plt.xlabel('Fare Amount')
    plt.ylabel('Frequency')
    plt.show()

    sns.scatterplot(x='trip_distance', y='fare_amount', data=df)
    plt.title('Fare vs. Trip Distance')
    plt.xlabel('Trip Distance')
    plt.ylabel('Fare Amount')
    plt.show()


def train_model(X, y):
    """Splits data and fits a Linear Regression model."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model, X_train, X_test, y_train, y_test


def evaluate_model(model, X_test, y_test):
    """Evaluates the regression model using R² and RMSE."""
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print(f"R² Score: {r2:.3f}")
    print(f"RMSE: {rmse:.2f}")
    return r2, rmse


def main():
    url = "https://github.com/Schravenralph/automatidata-insights/blob/main/2017_Yellow_Taxi_Trip_Data.csv"

    df = load_data(url)
    df = engineer_features(df)
    df = clean_data(df)

    print(f"Data shape after cleaning: {df.shape}")
    print(df[['fare_amount', 'trip_distance', 'hour', 'day', 'month', 'day_of_week']].describe())

    plot_distributions(df)

    # Select features
    features = ['trip_distance', 'hour', 'day_of_week']
    target = 'fare_amount'

    X = df[features]
    y = df[target]

    model, X_train, X_test, y_train, y_test = train_model(X, y)
    evaluate_model(model, X_test, y_test)


if __name__ == "__main__":
    main()