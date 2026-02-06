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

def solve_knapsack_1d(N, W_max, items):
    # 1次元配列のみ (dp[w] = 重さwの時の最大価値)
    dp = [0] * (W_max + 1)

    for weight, value in items:
        # 後ろから回すのがコツ！
        # 前から回すと、同じ品物を2回足してしまう（個数制限なしナップサックになってしまう）ため
        for w in range(W_max, weight - 1, -1):
            if dp[w - weight] + value > dp[w]:
                dp[w] = dp[w - weight] + value
                
    return dp[W_max]