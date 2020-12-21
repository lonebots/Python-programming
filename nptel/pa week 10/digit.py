n=list(map(int, input())) 
c0 = 0
c1 = 0
for r in n:
  if r == 0:
    c0 = c0 +1
  else:
    c1 = c1 +1
if c0 == 1 or c1 ==1:
  print("YES",end="")
else:
  print("NO",end="")
