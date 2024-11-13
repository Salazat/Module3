# count_calls # подсчитывает вызовы остальных функций
# string_info # принимает аргумент - строку и возвращает кортеж из длины этой строки #upper and #lower
# is_contains # Принимает два аргумента: строку и список и возвращает True, если строка находится в этом списке,
#                 # False - если отсутвует, Регистром строки при проверке принеберчь UrbaN - URBAN


calls = 0
def count_calss():
    global calls
    calls += 1
def string_info(string):
        count_calss()
        dlina = str(string)
        result = (len(dlina), dlina.upper(), dlina.lower())
        count_calss()
        return result
def is_contains(string, lis_to_search):
    string = str(string).lower()
    list_to_search = list(lis_to_search)
    count_calss()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Azat'))
print(string_info('Salakhov'))
print(is_contains('Samokat', ['kat', 'SaMo', 'SamOKAT']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
