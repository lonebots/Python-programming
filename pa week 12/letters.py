import string
s=input()
sl=list(s)
lower=0
upper=0
for i in sl:
  if(i!= " "):
    if(i.islower()):
      lower+=1
    elif(i.isupper()):
      upper+=1
print(upper,lower,sep=" ",end="")
