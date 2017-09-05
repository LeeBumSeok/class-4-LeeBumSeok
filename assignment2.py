factorial = 1

while 1:
    n = int(input("Enter a number: "))
    if n == -1:
        break
    elif n <= 0:
        print("x")
    else:
        for i in range(1, n+1):
            factorial *= i
        print("%d! =" % n, factorial)
        factorial = 1