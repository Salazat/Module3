
def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) == 0:
        return 1
    else:
        first = int(str_number[0])
        if first == 0:
            multiplied = get_multiplied_digits(str_number[1:])
            return multiplied
        else:
            first_ = first * get_multiplied_digits(str_number[1:])
            return first_

result = get_multiplied_digits(40203)
print(result)



