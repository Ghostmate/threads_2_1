numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [2]
not_primes = list()

for i in numbers:
    is_prime = True
    if i > 2:
        for j in range(2,primes[len(primes)-1]):
            if i % j == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
        else:
            not_primes.append(i)


print('Primes: ',primes)
print('Not primes: ',not_primes)

