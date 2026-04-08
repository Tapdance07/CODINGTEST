import sys

def solve():
    # 입력 받기
    input = sys.stdin.read().split()
    N = int(input[0])
    M = int(input[1])
    B = int(input[2])
    
    # 각 높이의 개수를 저장할 리스트 (0~256)
    height_counts = [0] * 257
    min_h = 256
    max_h = 0
    
    # 높이 빈도수 계산 및 최소/최대 높이 범위 축소
    idx = 3
    for _ in range(N * M):
        h = int(input[idx])
        height_counts[h] += 1
        if h < min_h: min_h = h
        if h > max_h: max_h = h
        idx += 1

    ans_time = float('inf')
    ans_height = 0

    # 목표 높이 i를 전체 범위가 아닌 실제 존재하는 높이 범위 주변에서 탐색 가능
    for target in range(0, 257):
        remove_blocks = 0 # 1번 작업 (제거)
        add_blocks = 0    # 2번 작업 (추가)
        
        # 각 높이별로 필요한 작업량 계산
        for current_h in range(min_h, max_h + 1):
            count = height_counts[current_h]
            if count == 0:
                continue
                
            if current_h > target:
                remove_blocks += (current_h - target) * count
            elif current_h < target:
                add_blocks += (target - current_h) * count
        
        # 인벤토리 체크 (가진 블록 + 깎은 블록 >= 채울 블록)
        if remove_blocks + B >= add_blocks:
            time = remove_blocks * 2 + add_blocks
            
            # 시간이 같으면 더 높은 높이를 선택해야 하므로 <= 사용
            if time <= ans_time:
                ans_time = time
                ans_height = target
                
    print(ans_time, ans_height)

solve()