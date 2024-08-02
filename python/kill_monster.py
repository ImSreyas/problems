# inp = [2, 123, 78, 130, 10, 0]
# inp = [3, 100, 101, 100, 304, 100, 1, 524]

mons = int(input())
exp = int(input())

power = []
bonus = []
for i in range(mons):
    power.append(int(input()))
for i in range(mons):
    bonus.append(int(input()))

count = 0
visited = []

for j in range(mons):
    for i in range(mons):
        if i in visited:
            continue
        if exp >= power[i]:
            visited.append(i)
            exp += bonus[i]
            count += 1
    
print("\nno.of monsters defeated : ", count)