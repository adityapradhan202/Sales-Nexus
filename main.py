import pandas as pd
import numpy as np
from predicting_model import sales_nexus
from predicting_model import X
from predicting_func import predict_nsales


avg_week_exp = float(input('Enter the average weekly expense you are willing to spend for your product (On a scale of 0-60): '))
telivision_ads_exp = float(input('Enter the weekly expense on TV ads you are willing to spend for your product (On a scale of 0-200): '))
radio_ads = float(input('Enter the number of weekly radio ads you are willing to do for your product (On a scale of 0-3000): '))
online_ads_exp = float(input('Enter the weekly expense on online ads you are willing to spend for your product (On a scale of 0-3000): '))

userinput = [avg_week_exp, telivision_ads_exp, radio_ads, online_ads_exp]
print(predict_nsales(userinput_list=userinput))
