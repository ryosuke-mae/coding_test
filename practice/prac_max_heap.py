import sys
import heapq

class MaxHeap:
    """
    Pythonのheapqは最小値しか扱えないため、値を-1倍して
    最大値を取り出せるようにしたラッパークラス
    """
    def __init__(self, items=[]):
        self.heap = [-x for x in items]
        heapq.heapify(self.heap)

    def push(self, item):
        """要素を追加する O(log N)"""
        heapq.heappush(self.heap, -item)

    def pop(self):
        """最大値を取り出す O(log N)"""
        if not self.heap:
            return None
        return -heapq.heappop(self.heap)

    def peek(self):
        """最大値を削除せずに見る O(1)"""
        if not self.heap:
            return None
        return -self.heap[0]

    def __len__(self):
        return len(self.heap)

# 再帰上限の引き上げ (DFSなどで必須)
sys.setrecursionlimit(10**6)

def main():
    # 高速な入出力
    input = sys.stdin.readline
    # --- ここに処理を書く ---
    N = int(input())
    stones = list(map(int, input().split()))
    mh = MaxHeap(stones)
    while len(mh) > 1:
        x = mh.pop()
        y = mh.pop()
        z = x-y
        
        if z > 0:
            mh.push(z)
    print(mh.pop() if len(mh) == 1 else 0)  
    pass

if __name__ == '__main__':
    main()