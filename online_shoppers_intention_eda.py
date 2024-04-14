import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('online_shoppers_intention.csv')

profile = ProfileReport(df, title='Online Shoppers Intention')

profile.to_file('online_shoppers_intention_eda.html')