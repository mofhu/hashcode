# author: mofhu@GitHub

c = int(input())
l = {}
d = {}
for i in range(c):
    # print(i)
    line = input().split(' ')
    # print(line)
    if line[0] != '0':
        l[i] = line[1:]
    line = input().split(' ')
    if line[0] != '0':
        d[i] = line[1:]

lc = {}
for k in l:
    for food in l[k]:
        if food not in lc:
            lc[food] = 1
        else:
            lc[food] += 1
dc = {}
for k in d:
    for food in d[k]:
        if food not in dc:
            dc[food] = 1
        else:
            dc[food] += 1

# print(lc)
# print(dc)

ans = []
for food in lc:
    if food not in dc:
        ans.append(food)
print('{} {}'.format(len(ans), ' '.join(ans)))

