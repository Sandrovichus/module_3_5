def get_multiplied_digits(number):  # рекурсивная функция для подсчета произведения цифр кроме 0
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return int(str_number[0])
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)
print(result)
