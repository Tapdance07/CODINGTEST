def solution(N, stages):
    stage_user = [0] * (N+2)
    for i in stages:
        stage_user[i] += 1
        
    fail_rate = []
    
    total_user = len(stages)
    
    for i in range(1, N+1):
        if total_user >0:
            rate = stage_user[i] / total_user
            fail_rate.append((i,rate))
            total_user -= stage_user[i]
        else:
            fail_rate.append((i,0))
            
    fail_rate.sort(key=lambda x: (-x[1], x[0]))
    return [s[0] for s in fail_rate]