m,n=input().split(",")
ans=[]
for i in range(int(m),int(n)+1):
  f=0
  s=list(str(i))
  for j in s:
    if(int(j)%2!=0):
      f=1
      break;
  if(f==0):
    ans.append(i)
print(*ans,sep=",",end="")
