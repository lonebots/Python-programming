a = list(map(int,input().split()))
m = max(a)
l = []
for i in range(m+1):
  if i in a:
     l.append(i)
  else:
     l.append(-1)
print(*l,sep=" ",end = "")
