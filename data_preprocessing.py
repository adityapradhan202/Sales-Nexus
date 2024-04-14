import numpy as np
import pandas as pd

# note - 
# data is already pretty good
# that is why there is not that much need to preprocess it that much!

df = pd.read_csv('market_data.csv')

df = df.drop_duplicates()
drop_cols = ['Discount', 'Price', 'StockRate']
df = df.drop(labels=drop_cols, axis=1)

rename_dict = {'InStrSpending':'Avg weekly expense', 'OnlineAdsSpending':'Online Ads expense', 'TVSpending':'TV ads expense'}
df.rename(rename_dict, inplace=True, axis=1)

# Saving the preprocessed data
df.to_csv('preprocessed_data.csv', index=False)
