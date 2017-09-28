def combination(n, m):

    if m == 0 or n == m:
        return 1

    return combination(n-1, m-1) + combination(n-1, m)

while True:

    try:
        n = int(input("집합의 모든 원소의 갯수를 입력하세요: "))
        m = int(input("고르는 원소의 갯수를 입력하세요: "))
        if n <= 0 or m <= 0:
            print("원소의 개수가 0보다 작습니다. 다시 입력해주세요.")
            continue
        elif n < m:
            print ("n보다 m이 더 큽니다. 다시 입력해주세요.")
            continue

        result = combination(n, m)

        print("%dC%d = %d" %(n, m, result))

    except ValueError:
        print("올바른 정수를 입력하세요")