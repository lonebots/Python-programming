s1="jishnu"
s2="jish"
l1=list(s1)
l2=list(s2)
for i in l1:
    for j in l2:
        if i ==j:
            l1.remove(i)
            l2.remove(j)
            continue

print(l1, l2,)
print(len(l1)+len(l2))