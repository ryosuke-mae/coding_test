import heapq

def dijkstra(N, adj, start_node):
    """
    ダイクストラ法による最短経路探索
    :param N: 頂点数
    :param adj: 隣接リスト (adj[u] = [(v, weight), ...])
    :param start_node: スタート地点
    :return: dist (各頂点への最短距離。到達不可は float('inf'))
    """
    # 距離テーブル (無限大で初期化)
    dist = [float('inf')] * N
    dist[start_node] = 0
    
    # 優先度付きキュー [(距離, 頂点), ...]
    # 距離が小さい順に取り出せる
    queue = [(0, start_node)]
    
    while queue:
        # 最も距離が短い頂点を取り出す
        current_dist, u = heapq.heappop(queue)
        
        # 【重要】ゴミデータのスキップ
        # キューには同じ頂点の情報が複数入る可能性がある（より短い経路が見つかるたびに追加するため）
        # 取り出した情報(current_dist)が、既に確定している最短距離(dist[u])より大きいなら、
        # それは古い情報なので無視する。
        if current_dist > dist[u]:
            continue
        
        # 隣接する頂点を探索
        for v, weight in adj[u]:
            # より短い経路が見つかった場合のみ更新
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(queue, (dist[v], v))
                
    return dist

# --- 使用例 ---
if __name__ == '__main__':
    # 0 -> 1 (コスト2)
    # 0 -> 2 (コスト5)
    # 1 -> 2 (コスト1)  => 0->1->2 の計3コストが最短
    
    N = 3
    adj = [[] for _ in range(N)]
    adj[0].append((1, 2))
    adj[0].append((2, 5))
    adj[1].append((2, 1))
    
    dists = dijkstra(N, adj, 0)
    print(dists) # [0, 2, 3]