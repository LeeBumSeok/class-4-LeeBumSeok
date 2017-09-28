def factorial(a):

    if a == 1 or a == 0:
        return 1
    else:
        return a*factorial(a-1)

while True:

    try:
        n = int(input("집합의 모든 원소의 갯수를 입력하세요: "))
        m = int(input("고르는 원소의 갯수를 입력하세요: "))
        if n < m:
            print ("n보다 m이 더 큽니다. 다시 입력해주세요.")
            continue
        elif n <= 0 or m <= 0:
            print("원소의 개수가 0보다 작거나 같습니다. 다시 입력해주세요.")
            continue
        result = factorial(n) / (factorial(m) * factorial((n - m)))

        print("%dC%d = %d" %(n, m, result))

    except ValueError:
        print("정수를 입력해 주세요")