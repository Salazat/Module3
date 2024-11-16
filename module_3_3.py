


def print_params(a = 1, b = 'Стройка', c = True):

    print(a, b, c)
print_params(256, 64 ,'object')
print_params("Present simple", [1+1], 9 )
print_params()

print_params(b=25)
print('Вызов  b=25, Работает')
print_params(c=[1,2,3])
print('Проверка c=[1,2,3] прошла успешно')

values_list = ("single", 99, False)
values_dict = {'a':100, 'b':11, 'c':10 }
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ('one', 9)
print_params(*values_list_2, 42)