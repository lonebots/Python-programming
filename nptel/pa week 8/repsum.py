n = input()
l = list(n)
while (len(l) != 1):
    sum = 0
    for i in l:
        sum += int(i)
    l.clear()
    l = list(str(sum))
print(*l, end="")
