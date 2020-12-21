word = input()
if (word.lower() == word[::-1].lower()):
    print("YES", end="")
    exit()
print("NO", end="")
