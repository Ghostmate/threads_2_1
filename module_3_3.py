def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params(b = 25)
print_params(c = [1,2,3])
print_params()

values_list = ["эт строка", 4, False]
values_dict = {'a' : 0, 'b' : 'и это строка', 'c' : 'не True'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = values_list
values_list_2.pop(1)
print_params(*values_list_2, 42)