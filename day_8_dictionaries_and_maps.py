phoneBook = {}
n = int(input())
for i in range(n):
    key, value = input().split()
    phoneBook[key] = value

for i in range(n):
    entry  = input()
    if entry not in phoneBook:
        print("Not found")
    else:
        print(entry+"="+phoneBook[entry])
