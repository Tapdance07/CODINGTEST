N, M = map(int, input().split())
T = [list(input()) for _ in range(N)]  # 체스판 입력 받기

def count_changes(x, y, color):
    changes = 0
    for i in range(8):
        for j in range(8):
            expected_color = color if (i + j) % 2 == 0 else ('B' if color == 'W' else 'W')
            if T[x + i][y + j] != expected_color:
                changes += 1
    return changes

min_changes = float('inf')  # 수정 횟수의 최소값을 무한대로 초기화

# 서브 체스판을 모든 위치에서 확인
for i in range(N - 7):  # 세로 범위
    for j in range(M - 7):  # 가로 범위
        changes_black_start = count_changes(i, j, 'B')  # 흑-백 시작
        changes_white_start = count_changes(i, j, 'W')  # 백-흑 시작
        min_changes = min(min_changes, changes_black_start, changes_white_start)

print(min_changes)  # 최소 수정 횟수 출력
