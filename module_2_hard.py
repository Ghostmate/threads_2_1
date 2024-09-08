def pairs(num):
    if num < 3:
        return
    temp = list()
    for i in range(1,num//2+1):
        for j in range(1,num):
            if num % (i + j) == 0:
                valid = True
                for k in range(len(temp)):
                    if temp[k] == {i,j}:
                        valid = False
                        break

                if valid:
                    temp.append({i,j})

    result = str()
    # return temp
    for i in range(len(temp)):
        if len(temp[i]) == 1:
            a = ''.join(str(x) for x in temp[i])
            result += a + a # Закомментировать, если одинаковые значения типа 1 и 1 невалидны
            continue
        else:
            result += ''.join(str(x) for x in temp[i])

    return result

try:
    while True:
        print(pairs(int(input('Введите число:'))))
except(ValueError):
    print('Только числа.')