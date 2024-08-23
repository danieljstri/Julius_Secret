import calendar
import os

def to_percentages(values):
    total = len(values)
    percentage_dict = {}
    for value in values:
        percentage = (values.count(value) / total) * 100
        percentage_dict[value] = percentage
    return percentage_dict

def expenses_per_week(file_path, column_list):

    file_name = os.path.basename(file_path)
    # Alguns processos para pegar separadamente o mês e o ano, que estão contidos no nome do arquivo
    file_split = file_name.split('.')
    file_split = file_split[0].split('-')
    # Ano e mês em variáveis separadas
    year = file_split[1]
    month = file_split[2]
    # Função que encontra o número de dias de um mês em um determinado ano
    num_days = calendar.monthrange(int(year), int(month))[1]

    past_month = [date for date in column_list if (int(date[6]) == int(month) - 1 )]
    actual_month = [date for date in column_list if (int(date[6]) == int(month))]

    buys_per_week = []
    weeks = []
    data = []

    for date in range(1, num_days + 1):
        if date % 7 == 0 or date == 31:
            data.append(date)
            weeks.append(data)
            data = []
        else:
            data.append(date)
    buys_per_week = []

    for week in weeks:
        counter = 0
        for date in week:
            for buy_date in past_month:
                date_split = buy_date.split('-')
                if int(date_split[2]) == date:
                    counter += 1
        buys_per_week.append(counter)

    for week in weeks:
        counter = 0
        for date in week:
            for buy_date in actual_month:
                date_split = buy_date.split('-')
                if int(date_split[2]) == date:
                    counter += 1
        buys_per_week[4] += counter

    return buys_per_week

        