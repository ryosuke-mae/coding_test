def dynamic_programming(N: int, A: list) -> int:
    
    dp = [float('inf')] * N
    
    
    dp[0] = 0  
    
    
    if N == 1: return 0
    
    
    dp[1] = abs(A[1] - A[0])
    
    
    for i in range(2, N):
        cost1 = dp[i-1] + abs(A[i] - A[i-1])
        cost2 = dp[i-2] + abs(A[i] - A[i-2])
        dp[i] = min(cost1, cost2)

    
    return dp[N-1]
    