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

# --- 以下は動作確認用（提出時は削除不要だが、main内ではないので実行されない） ---
if __name__ == '__main__':
    mh = MaxHeap([10, 30, 20])
    mh.push(50)
    print(mh.pop())  # 50
    print(mh.pop())  # 30