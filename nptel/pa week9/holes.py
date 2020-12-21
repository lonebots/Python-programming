hole = 'ADOPQRabdegopq'
count = 0
word = input()
for i in word:
    if i == "B":
        count += 2
    elif i in hole:
        count += 1
print(count, end="")
