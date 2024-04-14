import numpy as np
import pandas as pd
from predicting_model import sales_nexus
from predicting_model import X

def predict_nsales(userinput_list):

    userinput_array = np.array([userinput_list,])
    userinput_array_df = pd.DataFrame(data = userinput_array, columns = X.columns)
    model_prediction = sales_nexus.predict(userinput_array_df)

    return model_prediction[0]


if __name__ == "__main__":
    print(predict_nsales([59.9, 46.3, 1065, 1081.6]))