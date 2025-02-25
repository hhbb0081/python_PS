# 5014_스타트링크
from collections import deque
import sys
input = sys.stdin.readline()

f, s, g, u, d = map(int, input.split())

def BFS(F, S, G, U, D):
    if S == G:
        return 0

    queue = deque([(S, 0)])  # (현재 층, 버튼 클릭 횟수)
    visited = set()
    visited.add(S)

    while queue:
        floor, count = queue.popleft()

        for next_floor in (floor + U, floor - D):
            if 1 <= next_floor <= F and next_floor not in visited:
                if next_floor == G:
                    return count + 1
                queue.append((next_floor, count + 1))
                visited.add(next_floor)

    return "use the stairs"

print(BFS(f, s, g, u, d))

print(BFS(f, s, g, u, d))

# 총 f층, 도착층 g층, 현재 s층, u층 위로, d층 아래로 => s -> g로 가려면 버튼을 몇 번 눌러야 하는지?

# 그리디? 스러운 느낌이 나는데 달팽이 문제랑 비슷한 느낌이다.

# 10층 중 1층에서 10층으로 가기. 2층 위로 / 1층 아래로
# 1, 3, 5, 7, 9, 8, 10
# 1에서 0으로 가는 판단을 어떻게 할 수 있을까?
# 1 -> 11 (2, 1)이었으면 0으로 안 가도 됨: [(g - s) % u == 0] -> 5
# 1 -> 10 (3, 1)이었으면 0으로 안 가도 됨: [(g - s) % u == 0] -> 3
# 1 -> 10 (4, 1)이었으면 1, 5, 9, 8, 7, 6, 10: 9 % 4 == 3 // 1
# 이 경우에는 한 번 더가면 층을 초과하기 때문에 (g - s) % u == 0을 만족할 때까지 내려감
# 1 -> 10 (4, 5)이었으면 1, 5, 9, 4, 8, 3, 7, 2, 6, 10
# u < d이면
# u - s % u % (d - u)
# d - u
# 결론: 올라가는 경우에는 층을 초과하기 전까지 올라갔다가, (g - s) % u == 0 조건을 만족할 때까지 내려감
# 근데? u > d인 경우에만 해당. u <= d이면 불가능

# g > s면 g < s가 될 때까지 u, 이 이후에는 d
# g < s면 g > s가 될 때까지 d, 이 이후에는 u
# f층을 넘어가는 경우도 생각해야함
# u나 d가 0인 경우도 생각해야함

# 10 10 1 4 5
# 10, 5, 9, 4, 8, 3, 7, 2, 6, 1
#
# cnt = 0
# if g > s:
#     # 올라가야하는 경우
#     if u == 0:
#         cnt = -1
#     else:
#         # 초과하기 전까지 올라감
#         if (g - s) % u == 0:
#             # 올라가기만 하고 끝
#             cnt += (g - s) // u
#         elif u == d or d == 0:
#             cnt = -1
#         else:
#             cnt += (g - s) // u
#             if u > d:
#                 if (u - s % u) % d != 0:
#                     cnt = -1
#                 else:
#                     cnt += (u - s % u) // d
#                     cnt += 1
#             else:
#                 if (u - s % u) % (d - u) != 0:
#                     cnt = -1
#                 else:
#                     cnt += ((u - s % u) // (d - u)) * 2
#                     cnt += 1
# elif g < s:
#     # 내려가야 하는 경우
#     if d == 0:
#         cnt = -1
#     else:
#         # 초과하기 전까지 내려감
#         if (s - g) % d == 0:
#             # 내려가기만 하고 끝
#             cnt += (s - g) // d
#         elif u == d or u == 0:
#             cnt = -1
#         else:
#             cnt += (s - g) // d
#             if d > u:
#                 if (s % d) % u != 0:
#                     cnt = -1
#                 else:
#                     cnt += (s % d) // u
#                     cnt += 1
#             else:
#                 if (s % d) % (u - d) != 0:
#                     cnt = -1
#                 else:
#                     cnt += ((s % d) // (u - d)) * 2
#                     cnt += 1
# else:
#     cnt = 0
#
# if cnt == -1:
#     print('use the stairs')
# else:
#     print(cnt)