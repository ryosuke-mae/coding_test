import sys
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
# 再帰上限の引き上げ (DFSなどで必須)
sys.setrecursionlimit(10**6)

def main():
    # 高速な入出力
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    start_node = 0
    dists = bfs_general(N, adj, start_node)
    print(dists[N-1])
    pass

if __name__ == '__main__':
    main()