numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []  # Создаем пустой список
not_primes = []  # Создаем пустой список
for i in numbers:
    is_prime = True
    if i > 1:  # "1" - не может быть простым числом
        for j in range(2, i):
            if (i % j) == 0:
                is_prime = False
                if is_prime == False:
                    not_primes.append(i)
                break
        else:
            if is_prime == True:
                primes.append(i)
print('Простые числа: ', primes)
print('Составные числа: ', not_primes)