#https://www.hackerrank.com/challenges/longest-mod-path/editorial
#https://www.hackerrank.com/challenges/longest-mod-path/problem

n = input()
adj = [[] for i in xrange(n)]
for i in xrange(n):
    a, b, c = map(int, raw_input().strip().split())
    a -= 1; b -= 1
    adj[a].append((b, c))
    adj[b].append((a, -c))

dist = [None]*n
parents = [set() for i in xrange(n)] # set because of special case: cycle of length 2
dist[0] = 0
stack = [0]
while stack:
    i = stack.pop()
    for j, c in adj[i]:
        if j in parents[i]: continue
        ndist = dist[i] + c
        parents[j].add(i)
        if dist[j] is None:
            dist[j] = ndist
            stack.append(j)
        else:
            cycle = abs(dist[j] - ndist)

from fractions import gcd
for qq in xrange(input()):
    s, e, m = map(int, raw_input().strip().split())
    a = gcd(cycle, m)
    print (m - a + (dist[e-1] - dist[s-1]) % a)