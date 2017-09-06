factorial = 1

while 1:
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("x")
        continue
    if n == -1:
        break
    elif n == 0:
        print("%d! =" % n, factorial)
    elif n < 0:
        print("x")
    else:
        for i in range(1, n+1):
            factorial *= i
        print("%d! =" % n, factorial)
        factorial = 1