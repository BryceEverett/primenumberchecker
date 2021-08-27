num = int(input('Check if prime: '))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, '= not prime')
            print(i, 'x', num // i, 'is', num)
            break
    else:
        print(num, ' = prime')
else:
    print(num, '= not prime')