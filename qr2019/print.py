# print(fin)
n = int(input())

photos = []
ph = [] # H
pv = [] # V
tags = set()
nt = []
hist_nt = {}
nnt = 0
ctags = {}

for i in range(n):
    p = input().split(" ")
    for tag in p[2:]:
        tags.add(tag)
        if tag not in ctags:
            ctags[tag] = 1
        else:
            ctags[tag] += 1
    nt0 = len(p) - 2
    nt.append(nt0)
    nnt += nt0
    if nt0 not in hist_nt:
        hist_nt[nt0] = 1
    else:
        hist_nt[nt0] += 1
    photos.append([i]+ p)
    if p[0] == "H":
        ph.append([i]+ p)
    else:
        pv.append([i]+ p)
# print(photos)
# print(ph)
# print(pv)
print(len(photos))
print(len(ph))
print(len(pv))
print("tags:", len(tags))
# print(nt)
# print("avarage tag fig:", nnt/n)
# print(hist_nt)
for i in hist_nt:
    print(i, hist_nt[i])
# print(ctags)
hist_ct = {}
for ct in ctags:
    if ctags[ct] not in hist_ct:
        hist_ct[ctags[ct]] = 1
    else:
        hist_ct[ctags[ct]] += 1
print(hist_ct)
for i in hist_ct:
    print(i, hist_ct[i])
# print(tags)
# print(int(round((len(pv)-0.1)/2,0)))
"""

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

"""
