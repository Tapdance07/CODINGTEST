N = list(input())
N.sort(reverse=True)
# 그리디 알고리즘을 적용한다면 쓸수 있는 가장 큰수를 사용해서 30의 배수가 되는것을 먼저 만든다.
# 30의 배수가 되기 위해서는 10의 배수이면서 3의 배수여야 한다.
# 10의 배수이기 위해서는 0이 존재해야 한다.
if '0' not in N:
    print(-1)
else:
    # 3의 배수이기 위해서는 모든 숫자의 합이 3의 배수여야 한다.
    total = sum(int(digit) for digit in N)
    if total % 3 != 0:
        print(-1)
    else:
        print(''.join(N))