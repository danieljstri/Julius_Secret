import pandas as pd
from keys import FILE_PATH
from utils import expenses_per_week

file = pd.read_csv(FILE_PATH)
column = file['date']
column_list = column.to_list()

print(expenses_per_week(file_path=FILE_PATH, column_list=column_list))
 
