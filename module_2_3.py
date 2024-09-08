my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_iterator = 0
while my_iterator < len(my_list):
    if my_list[my_iterator] < 0:
        break
    if my_list[my_iterator] == 0:
        my_iterator += 1
        continue
    print(my_list[my_iterator])
    my_iterator += 1
