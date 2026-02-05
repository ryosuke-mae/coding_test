class Imos1D:
    """
    1次元いもす法
    範囲 [s, e) への加算を O(1) で行い、
    最後に累積和をとることで O(N) で全区間の値を復元する。
    注意: e は「半開区間」の終わり（eを含まない）とするのが一般的
    """
    def __init__(self, max_idx):
        # max_idx: 記録する最大の時刻や座標
        self.size = max_idx + 2 # 余裕を持って確保
        self.data = [0] * self.size
        self.built = False

    def add(self, s, e, value=1):
        """
        区間 [s, e) に value を加算する
        s: 開始インデックス (inclusive)
        e: 終了インデックス (exclusive, この時刻にはもういない)
        """
        if s >= self.size or e < 0: return
        self.data[s] += value
        if e < self.size:
            self.data[e] -= value

    def build(self):
        """累積和を計算して結果を確定させる"""
        for i in range(1, self.size):
            self.data[i] += self.data[i-1]
        self.built = True
        return self.data

# --- 使用例 ---
if __name__ == '__main__':
    # 0時から10時までを管理したい
    imos = Imos1D(10)
    
    # 1時から4時(の手前)まで +1
    imos.add(1, 4) 
    
    # 2時から5時(の手前)まで +1
    imos.add(2, 5)
    
    result = imos.build()
    print(result[:6]) 
    # 出力: [0, 1, 2, 2, 1, 0]
    # 1時:1人, 2時:2人, 3時:2人, 4時:1人...