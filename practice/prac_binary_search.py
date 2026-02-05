import sys

# 再帰上限の引き上げ (DFSなどで必須)
sys.setrecursionlimit(10**6)

def general_binary_search(check_func, ok, ng):
    """
    汎用的な二分探索（めぐる式）。
    ある条件 check_func(x) を満たす（True）最大/最小の x を見つける。
    
    :param check_func: 判定関数。x を受け取り bool を返す。
    :param ok: 条件を満たすことが確実な値（初期値）
    :param ng: 条件を満たさないことが確実な値（初期値）
    :return: 条件を満たす境界の値（ok 側の値）
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if check_func(mid):
            ok = mid
        else:
            ng = mid
    return ok

def main():
    # 高速な入出力
    input = sys.stdin.readline
    
    # --- ここに処理を書く ---
    N, K = map(int, input().split())
    L = list(map(int, input().split()))
    
    def can_make(length):
        if sum(L[i] // length for i in range(N)) >= K or length == 0:
            return True
        else:
            return False
    
    max_length = general_binary_search(can_make, 0, max(L)+1)     
    print(max_length)
    pass

if __name__ == '__main__':
    main()
    