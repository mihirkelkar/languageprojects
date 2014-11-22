#Rea input from STDIN. Print output to STDOUT
n = int(raw_input())
v = map(int,raw_input().split())
s = [0,0]
for i in range(2,n+1):
    s.append(s[i-2] ^ (v[i-1] - v[i-2]))
cnt = [dict(), dict()]
res = 0
for i in range(n-2,-1,-1):
    cnt[i&1][s[i+2]] = 1 + cnt[i&1].get(s[i+2],0)
    res += cnt[i&1].get(s[i],0) + cnt[(i^1)&1].get(v[i]^s[i+1],0)
print n*(n-1)/2 - res
