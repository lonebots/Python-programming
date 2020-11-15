str1 = input()
str2 = input()
if (sorted(list(str1.lower())) == sorted(list(str2.lower()))):
    print("anagram")
    exit()
print("not anagram")