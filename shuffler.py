import random
from boltons import iterutils

members = ["Pappa", "Mummy", "Parth", "khushal", "Jash", "Pratham", "Maha", "Bhung", "Chiki",
           "Hasrh", "Cookie", "Ramu", "Bhabhi", "Bhabhiji", "Ram", "Shyam", "Chotu", "Mama", "Mami"]
print("In previous order : ", end=" ")
print(members)

print("Shuffled form : ", end=" ")
random.shuffle(members)
print(members)

print(iterutils.chunked(members, 3))
# [lo[i:i+3] for i in range(0,len(lo),10)]
# print("Sublist : ", end=" ")
# print(lo)

# teamA = list(map(list, lo[:1]))
# print(teamA)
# c = [lo[i] for i in range(2)]
# print(c)
for xs in iterutils.chunked(members, 10):
    print(" ".join(map(str, xs)))
