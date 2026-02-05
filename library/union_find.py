class UnionFind:
    """
    Union-Find (DSU) with Path Compression and Union by Size
    計算量: ほぼ O(1) (アッカーマン関数の逆関数)
    """
    def __init__(self, n):
        self.n = n
        # parents[i]: 要素iの親。負の場合は「根」であり、絶対値がグループのサイズを表す
        # 例: -3 なら、自分が根で、配下に自分含め3人いる
        self.parents = [-1] * n

    def find(self, x):
        """xの根（グループの代表）を返す + 経路圧縮"""
        if self.parents[x] < 0:
            return x
        else:
            # 再帰的に親を探し、見つけた根を直接親に設定する（経路圧縮）
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """xとyのグループを統合する"""
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False # 既に同じグループ

        # Union by Size: サイズが大きい方(x)に小さい方(y)をつなぐ
        # parentsの値は負数でサイズを持っているので、小さい方が「サイズが大きい」
        if self.parents[x] > self.parents[y]:
            x, y = y, x # xの方がサイズが大きくなるように入替

        # yをxの子にする
        self.parents[x] += self.parents[y] # サイズ更新
        self.parents[y] = x # yの親をxにする
        return True

    def size(self, x):
        """xが含まれるグループのサイズを返す"""
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """xとyが同じグループか判定"""
        return self.find(x) == self.find(y)

    def roots(self):
        """全ての根（グループの代表）をリストで返す"""
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """グループの総数を返す"""
        return len(self.roots())

# --- 使用例 ---
if __name__ == '__main__':
    uf = UnionFind(5) # 0~4の5人
    uf.union(0, 1)    # 0と1が友達
    uf.union(1, 2)    # 1と2が友達 -> 0,1,2は同じグループ
    uf.union(3, 4)    # 3と4が友達
    
    print(uf.same(0, 2)) # True
    print(uf.same(0, 4)) # False
    print(uf.size(0))    # 3 (0,1,2)