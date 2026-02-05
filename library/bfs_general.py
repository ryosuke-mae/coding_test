from collections import deque

def bfs_general(N, adj, start_node):
    """
    一般的なグラフの最短経路（幅優先探索）
    :param N: 頂点数
    :param adj: 隣接リスト (adj[u] = [v1, v2, ...] uから行ける頂点のリスト)
    :param start_node: スタート地点の頂点番号
    :return: dist (各頂点までの最短距離リスト。到達不可は-1)
    """
    # 距離リスト (-1 で初期化)
    dist = [-1] * N
    
    # スタート地点の初期化
    dist[start_node] = 0
    queue = deque([start_node])
    
    while queue:
        # 今いる頂点を取り出す
        u = queue.popleft()
        
        # u から行けるすべての頂点 v をチェック
        for v in adj[u]:
            # 未訪問 (distが-1) なら距離を更新してキューに入れる
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
                
    return dist

if __name__ == '__main__':
    # 頂点数 5 (0, 1, 2, 3, 4)
    # 0 -- 1 -- 2
    # |    |
    # 3 -- 4
    
    N = 5
    # 隣接リストを作る
    adj = [[] for _ in range(N)]
    
    # つながりを登録 (無向グラフなら双方向に追加)
    edges = [(0, 1), (0, 3), (1, 2), (1, 4), (3, 4)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    # 頂点0からの距離を計算
    dists = bfs_general(N, adj, start_node=0)
    print(dists) 
    # 出力: [0, 1, 2, 1, 2]
    # 0->0: 0手
    # 0->1: 1手
    # 0->2: 2手 (0->1->2)
    # ...