def factorial(a):
    result = 1
    if a == 0:
        return 1
    while a > 0:
        result *= a
        a -= 1
    return result


while 1:
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("x")
        continue
    if n == -1:
        break
    elif n == 0:
        print("%d! =" % n, factorial(n))
    elif n < 0:
        print("x")
    else:
        print("%d! =" % n, factorial(n))

"""
- code review를 하는 과정에서 while문으로 똑같은 코드를 계속 사용하는 것이 비효율적이라 판단했습니다.
- def문으로 factorial 코드를 구현하고, while문으로 예외 처리를 해주는 방법이 가장 빠르고 보기 좋을 것이라고 생각했습니다.
- python coding guideline을 참고하여 어법에 맞지 않는 구문을 고치려 해보았습니다.
- 더욱 간결한 코드를 만들 수 있도록 하겠습니다.
"""