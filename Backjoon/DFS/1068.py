# # 1068 트리
#
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
#
# n = int(input())
# nodes = [int(input()) for _ in range(n)]
# rv = int(input())
#
# # -1 0 0 1 1, 2 => 2
# # -1 0 0 1 1, 1 => 1
# # -1 0 0 1 1, 0 => 0
# # -1 0 0 2 2 4 4 6 6, 4 => 2
#
# # 리프노드 조건 : 자신을 부모노드로 하는 노드가 없어야 함
# # -> nodes에 자신의 노드 번호가 포함되어 있으면 안 됨
# # rv로 주어지는 노드를 포함한 자식 노드들은 계산에 포함되면 안 됨
#
# def dfs(node):
