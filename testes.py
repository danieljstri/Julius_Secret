import pandas as pd
from keys import FILE_PATH
import calendar
from datetime import datetime
import os

file = pd.read_csv(FILE_PATH)
column = file['date']

column_list = column.to_list()
month8 = [date for date in column_list if (date[6] == '8')]
month7 = [date for date in column_list if (date[6] == '7')]

week1_month7 = [date for date in month7 if date.split('-')[2] in ['01', '02', '03', '04', '05', '06', '07']]
week2_month7 = [date for date in month7 if date.split('-')[2] in ['08', '09', '10', '11', '12', '13', '14']]
week3_month7 = [date for date in month7 if date.split('-')[2] in ['15', '16', '17', '18', '19', '20', '21']]
week4_month7 = [date for date in month7 if date.split('-')[2] in ['22', '23', '24', '25', '26', '27', '28']]
week1_month8 = [date for date in month7 if date.split('-')[2] in ['29', '30', '31']]
for date in month8:
    week1_month8.append(date)

# print(len(week1_month7))
# print('-' * 50)
# print(len(week2_month7))
# print('-' * 50)
# print(len(week3_month7))
# print('-' * 50)
# print(len(week4_month7))
# print('-' * 50)
# print(len(week1_month8))

# Pegar o número de dia através do nome do arquivo
# Guarda o nome do aquivo
file_name = os.path.basename(FILE_PATH)
# Alguns processos para pegar separadamente o mês e o ano, que estão contidos no nome do arquivo
file_split = file_name.split('.')
file_split = file_split[0].split('-')
# Ano e mês em variáveis separadas
year = file_split[1]
month = file_split[2]
# Função que encontra o número de dias de um mês em um determinado ano
num_days = calendar.monthrange(int(year), int(month))[1]

buys_per_week = []
data = []
for date in range(1, num_days + 1):
    if date % 7 == 0:
        data.append(date)
        print(data)
        buys_per_week.append(len(data))
        data = []
    else:
        data.append(date)
print(buys_per_week)