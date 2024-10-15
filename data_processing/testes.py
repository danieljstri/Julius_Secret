import pandas as pd
from keys import FILE_PATH
from utils import expenses_per_week, to_percentages

file = pd.read_csv(FILE_PATH)
column_date = file['date']
column_category = file['category']
column_list2 = column_category.to_list()
column_list1 = column_date.to_list()

print(expenses_per_week(file_path=FILE_PATH, column_list=column_list1))
print(to_percentages(column_list2))
