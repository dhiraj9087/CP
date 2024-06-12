from collections import deque

def is_bound(point, n, m):
    x, y = point
    return 0 <= x < n and 0 <= y < m

def solve(ttc):
    n, m = map(int, input().split())
    v = [input() for _ in range(n)]
    dirs2 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    g = [[0] * m for _ in range(n)]
    mp = {}
    ans = 0
    x = 1

    def bfs(i, j):
        nonlocal x
        nonlocal ans
        nonlocal mp
        queue = deque([(i, j)])
        mp[x] = 0

        while queue:
            tp = queue.popleft()
            if not is_bound(tp, n, m) or v[tp[0]][tp[1]] == '.' or g[tp[0]][tp[1]] != 0:
                continue
            g[tp[0]][tp[1]] = x
            mp[x] += 1
            for nxt in dirs2:
                queue.append((tp[0] + nxt[0], tp[1] + nxt[1]))

        ans = max(ans, mp[x])
        x += 1

    for i in range(n):
        for j in range(m):
            if v[i][j] == '#' and g[i][j] == 0:
                bfs(i, j)

    for i in range(n):
        for j in range(m):
            ta = 0
            s = set()
            if v[i][j] == '#':
                s.add(g[i][j])
            else:
                ta += 1
                if i > 0 and v[i - 1][j] == '#':
                    s.add(g[i - 1][j])
                if i + 1 < n and v[i + 1][j] == '#':
                    s.add(g[i + 1][j])
            
            for x in s:
                ta += mp[x]
            
            ans = max(ans, ta)

    for j in range(m):
        for i in range(n):
            ta = 0
            s = set()
            if v[i][j] == '#':
                s.add(g[i][j])
            else:
                ta += 1
                if j > 0 and v[i][j - 1] == '#':
                    s.add(g[i][j - 1])
                if j + 1 < m and v[i][j + 1] == '#':
                    s.add(g[i][j + 1])

            for x in s:
                ta += mp[x]
            
            ans = max(ans, ta)

    print(ans)

for _ in range(int(input())):
    solve(1)
