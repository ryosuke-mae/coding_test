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

# --- 以下、使用例（提出時は削除不要） ---
if __name__ == '__main__':
    # 例: A = [1, 3, 3, 3, 5] の中で "3以上" になる最初のインデックスを探す
    # 条件: index >= 3 ? (値が3以上か？)
    
    A = [1, 3, 3, 3, 5]
    
    # 判定関数: A[x] が 3以上なら True (OK)
    def is_ge_3(idx):
        if idx >= len(A): return True # 範囲外の扱いに注意
        return A[idx] >= 3

    # ok=len(A) (右端は確実に3以上とみなす仮定), ng=-1 (左端は違う)
    # ただし今回は「最小のインデックス」が欲しいので、
    # 条件を満たす側(ok)を右、満たさない側(ng)を左にするか、
    # 逆に設定するかで挙動が変わります。
    
    # シンプルな bisect_left と同じ挙動にする例:
    # ng = -1 (条件を満たさない), ok = len(A) (条件を満たす境界)
    # → これで「条件を満たす最小のindex」が求まる
    print(general_binary_search(is_ge_3, len(A), -1)) # 結果: 1