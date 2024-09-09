def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    first = 1 if first == 0 else first
    if len(str_number) > 1:
        return first*get_multiplied_digits(str_number[1:])
    return first

result = get_multiplied_digits(40203)
print(result)