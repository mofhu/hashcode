# print(fin)
n = int(input())

photos = []
ph = [] # H
pv = [] # V

for i in range(n):
    p = input().split(" ")
    photos.append([i]+ p)
    if p[0] == "H":
        ph.append([i]+ p)
    else:
        pv.append([i]+ p)
# print(photos)
# print(ph)
# print(pv)
# print(len(photos))
# print(len(ph))
# print(len(pv))
# print(int(round((len(pv)-0.1)/2,0)))


def dist(x, y):
    # dist function using hash maybe.
    return 0

nslide = len(ph) + int(round((len(pv)-0.1)/2,0))
print(nslide)
for i in range(len(ph)):
    p = ph[i]
    print(p[0]) # index

i = 0
while i < int(round((len(pv)-0.1)/2,0)):
    p = pv[2*i]
    q = pv[2*i+1]
    print(p[0], q[0]) # index
    i += 1

