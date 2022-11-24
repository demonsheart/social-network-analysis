import pandas as pd

df_csv = pd.read_csv('data/my_csv.csv')

df_csv.to_excel('data/my_saved_excel.xlsx', index=False)

