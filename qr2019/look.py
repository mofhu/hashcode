import random
from sys import argv

script, DEBUG, NITER = argv

DEBUG = int(DEBUG)
NITER = int(NITER)

# print(fin)
n = int(input())

photos = []
ph = [] # H
pv = [] # V
phs = []
pvs = []

# s1 = set(["a","e","f"])
# s2 = set(["d","b","c"])
def score_v(s1, s2):
    return len(s1.union(s2))

def score(s1, s2):
    ins = s1.intersection(s2)
    s12 = s1-s2
    s21 = s2-s1
    # print(ins)
    # print(s12)
    # print(s21)
    return min(len(ins), len(s12), len(s21))

# print(score(s1, s2))

for i in range(n):
    p = input().split(" ")
    photos.append([i]+ p)
    if p[0] == "H":
        ph.append([i]+ p)
        phs.append(set(p[2:]))
    else:
        pv.append([i]+ p)
        pvs.append(set(p[2:]))
# print(phs)
print(len(ph))
print(len(pv))

# all H for b.in
i = 0
if len(pvs) > 0:
    pi = pvs[i]
# set to random init later
while len(pv) > 0:
    # print("cycle count:", len(ph))
    pi = pvs[0]
    t = 1
    st = score_v(pi, pvs[1])
    for k in range(1,min(NITER,len(pv))):
        # print(j)
        # j is index
        # choose random one for small search
        j = random.randint(0, len(pv)-1)
        if j == 0:
            j += 1
        sj = score_v(pi, pvs[j])
        if sj > st:
            t = j
            st = sj
    # print(pv[0], pv[t])
    # break
    vtoh = str(pv[0][0]) + " " + str(pv[t][0]) # index
    # print(vtoh)
    phs.append(pvs[0].union(pvs[t]))
    ph.append([vtoh])
    # print(ph)
    del pv[t]
    del pvs[t]
    del pv[0]
    del pvs[0]

# print(photos)
# print(ph)
# print(pv)
# print(len(photos))
print(len(ph))
print(len(pv))
# print(int(round((len(pv)-0.1)/2,0)))

def dist(x, y):
    # dist function using hash maybe.
    return 0

# all H for b.in
nslide = len(ph) + int(round((len(pv)-0.1)/2,0))
print(nslide)
i = 0
pi = phs[i]  # set
# set to random init later
fscore = 0
pi0 = ph[i][0]

scores = {}
best_scores = {}

for i in range(len(ph)):
    si = 0
    for j in range(i, len(ph)):
        sij = score(pi, phs[j])
        if sij not in scores:
            scores[sij] = 1
        else:
            scores[sij] += 1
        if sij > si:
            si = sij
    if i % 100 == 0:
        print(i)
        print(scores)
        print(best_scores)

    if si not in best_scores:
        best_scores[si] = 1
    else:
        best_scores[si] += 1

# sampling!!!
print(scores)
print(best_scores)

if DEBUG:
    print(fscore)

