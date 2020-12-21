n=int(input())
l=[]
for i in range (n):
  s=input()
  sl=list(s)
  for j in range(len(sl)):
    if(sl[j]!=" "):
      sl[j]=sl[j].upper()
  r=""
  r=r.join(sl)
  l.append(r)
print(*l,sep="\n",end="")
    
