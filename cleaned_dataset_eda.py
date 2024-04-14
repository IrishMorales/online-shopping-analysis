import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('cleaned_dataset.csv')

profile = ProfileReport(df, title='Online Shoppers Intention (Cleaned)')

profile.to_file('cleaned_dataset_eda.html')