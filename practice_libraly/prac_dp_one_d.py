import sys

# 再帰上限引き上げ（今回はループDPなので必須ではないですが、お守りとしてOK）
sys.setrecursionlimit(10**6)

def dynamic_programming(N: int, A: list) -> int:
    """
    動的計画法のサンプルコード（カエルの移動）
    """
    # DPテーブル: dp[i] = 足場 i にたどり着く最小コスト
    # 足場は 0 から N-1 までなので、サイズは N でOK
    dp = [float('inf')] * N
    
    # 1. 初期条件
    dp[0] = 0  # スタート地点のコストは0
    
    # ガード: N=1の場合はジャンプできないので0を返す
    # (制約で N>=2 なら不要だが、安全のため)
    if N == 1: return 0
    
    # 2つ目の足場へのコストは確定
    dp[1] = abs(A[1] - A[0])
    
    # 2. ループ（足場 2 から ゴール N-1 まで）
    for i in range(2, N):
        # 1つ前から vs 2つ前から
        cost1 = dp[i-1] + abs(A[i] - A[i-1])
        cost2 = dp[i-2] + abs(A[i] - A[i-2])
        dp[i] = min(cost1, cost2)

    # ゴール（N-1）のコストを返す
    return dp[N-1]

def main():
    input = sys.stdin.readline
    
    # 入力受け取り（エラーガード付き）
    try:
        line1 = input().strip()
        if not line1: return
        N = int(line1)
        A = list(map(int, input().split()))
    except ValueError:
        return

    result = dynamic_programming(N, A)
    print(result)

if __name__ == '__main__':
    main()