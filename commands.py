def to_percentages(values):
    total = len(values)
    percentage_dict = {}
    for value in values:
        percentage = (values.count(value) / total) * 100
        percentage_dict[value] = percentage
    return percentage_dict

