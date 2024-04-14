import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse

processed_df = pd.read_csv('preprocessed_data.csv')

# Sale - y (That is what we are going to predict)
# Rest of the features comes under X
y = processed_df['Sale']
X = processed_df.drop(['Sale'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)

# ML model
sales_nexus = LinearRegression()
sales_nexus.fit(X_train, y_train)
sales_predictions = sales_nexus.predict(X_test)

# Performance evaluation
mae_value = mae(y_test, sales_predictions)
mse_value = mse(y_test, sales_predictions)

percentage_error_mae = ( mae_value / np.mean(processed_df['Sale']) ) * 100
mse_value = np.sqrt(mse_value)
percentage_error_mse = ( mse_value / np.mean(processed_df['Sale']) ) * 100


if __name__ == "__main__":
    print(f'Percentage error: {percentage_error_mae}')

    
    user_inputs = [59.3, 46.1, 1062, 1081.4]
    user_inputs_arr = np.array([user_inputs,]) # 2d ndarray as data for df
    user_inputs_df = pd.DataFrame(data=user_inputs_arr, columns = X.columns)
    predic_sale = sales_nexus.predict(user_inputs_df)

    print(f'Predicted sale: {round(predic_sale[0])} products might be sold this week!')





