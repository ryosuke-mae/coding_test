import sys

def two_pointers(N, A, K):
    """
    条件: 区間の和が K 以下になる「最長の長さ」を求める例
    """
    right = 0
    current_sum = 0
    ans = 0 # 答え（最大長など）
    count_part = 0 # 部分列の数

    for left in range(N):

        while right < N and current_sum + A[right] <= K:
            
            current_sum += A[right]
            right += 1
        count_part += (right - left)

        if right == left:
            right += 1
        else:
            current_sum -= A[left]
            
    return count_part


sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    count_part = two_pointers(N, A, K)

    print(count_part)

if __name__ == '__main__':
    main()