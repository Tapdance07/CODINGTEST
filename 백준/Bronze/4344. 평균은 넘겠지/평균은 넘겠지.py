import sys

# 테스트 케이스 개수 C 입력
c = int(sys.stdin.readline())

for _ in range(c):
    # 한 줄을 읽어서 리스트로 변환
    data = list(map(int, sys.stdin.readline().split()))
    
    n = data[0]          # 첫 번째 수는 학생 수
    scores = data[1:]    # 나머지는 학생들의 점수
    
    # 1. 평균 구하기
    avg = sum(scores) / n
    
    # 2. 평균을 넘는 학생 수 구하기
    above_avg_count = 0
    for score in scores:
        if score > avg:
            above_avg_count += 1
            
    # 3. 비율 계산 (백분율)
    ratio = (above_avg_count / n) * 100
    
    # 4. 소수점 셋째 자리까지 출력 (f-string 사용)
    print(f"{ratio:.3f}%")