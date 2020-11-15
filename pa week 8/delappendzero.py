l = list(map(int, input().split(" ")))
for i in range(l.count(0)):
    l.append(0)
l = list(filter(lambda x: x != 0, l))
print(*l, sep=" ", end="")
