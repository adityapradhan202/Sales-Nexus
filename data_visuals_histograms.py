import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

processed_df = pd.read_csv('preprocessed_data.csv')
fig,axes = plt.subplots(nrows=2, ncols=2, figsize=(10,10), dpi=150)

axes[0][0].set_title('Avg weekly expense')
sns.histplot(x='Avg weekly expense', data = processed_df, ax=axes[0][0], bins=20)

axes[0][1].set_title('Radio ads')
axes[0][1].set_xlabel('Weekly radio advertisements')
sns.histplot(x='Radio', data = processed_df, ax=axes[0][1], bins=20)

axes[1][0].set_title('Online advertisements')
axes[1][0].set_xlabel('Online Ads expense')
sns.histplot(x='Online Ads expense', data = processed_df, ax=axes[1][0], bins=20)

axes[1][1].set_title('Televison advertisements')
axes[1][1].set_xlabel('TV ads expense')
sns.histplot(x='TV ads expense', data = processed_df, ax=axes[1][1], bins=20)

fig.subplots_adjust(wspace=0.5, hspace=0.65)
fig.suptitle('Histograms!', fontsize=15)

if __name__ == "__main__":
    plt.savefig('data_visuals_histograms.png')
    plt.show()