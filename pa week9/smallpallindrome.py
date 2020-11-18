word = input()
l = []
for i in range(97, 123):
    l.append(chr(i))
n = 0
while (n <= 25):
    new = word.replace(".", l[n])
    if new == new[::-1]:
        print(new, end="")
        break
    new = word
    n += 1
else:
    print("-1", end="")
