import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

processed_df = pd.read_csv('preprocessed_data.csv')
fig,axes = plt.subplots(nrows=2, ncols=2, figsize=(10,10), dpi=150)

sns.kdeplot(x='Avg weekly expense', data = processed_df, fill=True, color='blue', ax=axes[0][0])
sns.kdeplot(x='TV ads expense', data = processed_df, fill=True, color='orange', ax=axes[0][1])
sns.kdeplot(x='Radio', data = processed_df, fill=True, color='pink', ax=axes[1][0])
sns.kdeplot(x='Online Ads expense', data = processed_df, fill=True, color='red', ax=axes[1][1])

fig.subplots_adjust(wspace=0.37, hspace=0.5)
fig.suptitle('Relative probabilty or KDE plots!', fontsize=10)
plt.savefig('data_visuals_kdeplots.png')
