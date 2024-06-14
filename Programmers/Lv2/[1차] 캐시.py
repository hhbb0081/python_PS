import sys
input = sys.stdin.readline()

def solution(cacheSize, cities):
    answer = 0
    cache = []
    for c in cities:
        c.lower()
        if len(cache) < cacheSize:
            cache.append(c)
            answer += 5
            print(c)
        else:
            if cache.count(c) == 0:
                # cache miss
                cache.append(c)
                cache.pop(0)
                answer += 5
                print(c)
            else:
                # cache hit
                cache.remove(c)
                answer += 1
                cache.append(c)
                print(c)

    return answer

ans = solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	)
print(ans)