def percentage_per_item(array):
    total = len(array)
    percentage_dict = {}
    for item in array:
        counter = array.count(item)
        percentage = (counter / 100) * total
        percentage_dict[item] = percentage * 100
    return percentage_dict
    

minhalista = ['maçã', 'uva', 'pera', 'melancia', 'melancia', 'melancia', 'maçã', 'maçã', 'pera']

porcentagens = percentage_per_item(minhalista)

valores = porcentagens.values()
for valor in valores:
    print(valor)