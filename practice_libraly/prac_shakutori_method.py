import sys

def two_pointers(N, A, K):
    """
    条件: 区間の和が K 以下になる「最長の長さ」を求める例
    """
    right = 0
    current_sum = 0
    ans = 0 # 答え（最大長など）
    
    # left を 0 から N-1 まで1つずつ進める
    for left in range(N):
        # 1. right を進められるだけ進める
        # 「範囲内」かつ「足してもKを超えない」なら進む
        while right < N and current_sum + A[right] <= K:
            current_sum += A[right]
            right += 1
        
        # --- ここで [left, right) は条件を満たす極大の区間になっている ---
        
        # 2. 答えの更新
        ans = max(ans, right - left)
        
        # 3. left を進める準備（今の left の値を合計から引く）
        # ただし、right が left と同じ場所（区間が空）なら、right も一緒に進める
        if right == left:
            right += 1
        else:
            current_sum -= A[left]
            
    return ans


sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    ans = two_pointers(N, A, K)

    print(ans)

if __name__ == '__main__':
    main()