import math
C=50
H=30
l=list(map(int,input().split(",")))
ans=[]
for i in l:
  Q=math.sqrt((2*C*i)/H)
  ans.append(round(Q))
print(*ans,sep=",",end="")
