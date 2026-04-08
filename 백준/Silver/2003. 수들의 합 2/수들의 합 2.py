N,M = map(int, input().split())
A = list(map(int, input().split()))
count = 0
sum = 0
end = 0
for start in range(N):
    # sum이 M보다 작으면 end를 계속 이동하며 더함
    while sum < M and end < N:
        sum += A[end]
        end += 1
    
    # 합이 M과 같으면 카운트 증가
    if sum == M:
        count += 1
    
    # 다음 start로 넘어가기 전에 현재 start 원소를 합에서 제외
    sum -= A[start]

print(count)