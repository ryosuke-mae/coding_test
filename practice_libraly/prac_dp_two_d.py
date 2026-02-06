import sys

sys.setrecursionlimit(10**6)


def dynamic_programming_two_dimension(N: int, W_max: int, items: list) -> int:
    """
    2次元DPのサンプルコード（ナップサック問題）
    items: 各アイテムの (weight, value) のリスト
    """
    dp = [[0] * (W_max + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        weight, value = items[i - 1]
        for w in range(W_max + 1):
            dp[i][w] = dp[i - 1][w]  # アイテムを選ばない場合
            if w >= weight:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weight] + value)  # アイテムを選ぶ場合
    

    # 最大価値を返す
    return dp[N][W_max]



def main():
    input = sys.stdin.readline
    
    N, W_max = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]
    result = dynamic_programming_two_dimension(N, W_max, items)
    print(result)
    
    pass

if __name__ == '__main__':
    main()