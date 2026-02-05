from collections import deque

def bfs_grid(grid, start, h, w, wall='#'):
    """
    グリッド上の最短経路（幅優先探索）
    :param grid: 迷路のリスト (例: ["...#", ".S.#", ...])
    :param start: スタート地点の座標 (y, x)
    :param h: 高さ
    :param w: 幅
    :param wall: 壁を表す文字
    :return: dist (各地点までの最短距離テーブル。到達不可は-1)
    """
    # 距離テーブル (-1 で初期化)
    dist = [[-1] * w for _ in range(h)]
    
    sy, sx = start
    dist[sy][sx] = 0
    
    queue = deque([start])
    
    # 移動方向（上下左右）
    drc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while queue:
        cy, cx = queue.popleft() # 先頭から取り出す (FIFO)
        
        for dy, dx in drc:
            ny, nx = cy + dy, cx + dx
            
            # 1. 範囲外チェック
            if not (0 <= ny < h and 0 <= nx < w):
                continue
            # 2. 壁チェック
            if grid[ny][nx] == wall:
                continue
            # 3. 訪問済みチェック (distが-1以外なら既に誰かが来ている＝より近い経路がある)
            if dist[ny][nx] != -1:
                continue
            
            # 更新してキューに入れる
            dist[ny][nx] = dist[cy][cx] + 1
            queue.append((ny, nx))
            
    return dist

# --- 使用例 ---
if __name__ == '__main__':
    # .: 通路, #: 壁, S: スタート, G: ゴール
    maze = [
        "......",
        ".#.#..",
        ".S.#.G",
        ".#...."
    ]
    H, W = len(maze), len(maze[0])
    
    # スタート位置を探す
    start_pos = (2, 1) # Sの場所
    
    # BFS実行
    distances = bfs_grid(maze, start_pos, H, W)
    
    # ゴール(2, 5)への距離を表示
    print(distances[2][5]) # 結果: 4