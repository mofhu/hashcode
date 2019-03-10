import random
from sys import argv

script, DEBUG, NITER, THRESHOLD = argv

DEBUG = int(DEBUG)
NITER = int(NITER)
THRESHOLD = int(THRESHOLD)
# print(fin)
n = int(input())

photos = []
ph = [] # H
pv = [] # V
phs = []
pvs = []
tag_dict = {}

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
    if p[0] == "H":
        ph.append([i]+ p)
        tags = set(p[2:])
        phs.append(tags)
        for tag in tags:
            if tag not in tag_dict:
                tag_dict[tag] = set([i])
            else:
                tag_dict[tag].add(i)
        # print(tag_dict)
    else:
        pv.append([i]+ p)
        pvs.append(set(p[2:]))
# print(phs)


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
# print(len(ph))
# print(len(pv))
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
pi0 = ph[i]
used_index = set()
unused_index = [i for i in range(len(ph))]


while len(unused_index) > 0:  # for b
    # print("cycle count:", len(ph))
    index = pi0[0]
    # print(pi0[3:])
    best_friends = {}
    for tag in pi:
        if len(tag_dict[tag]) > 1:
            # print(tag)
            # print(tag_dict[tag])
            for i in tag_dict[tag]:
                if i not in used_index:
                    if i not in best_friends:
                        best_friends[i] = 1
                    else:
                        best_friends[i] += 1
                        if best_friends[i] == 3:  # greedy, 3 is magic number for case b
                            j = i
                            break
    # print(best_friends)
    if j == index:  # no 3 found
        # print(index, best_friends)
        # print("debug")
        best_len = 0
        for k in best_friends:
            if best_friends[k] > best_len:
                best_len = best_friends[k]
                j = k
    if j == index:
        # blank index, new random j
        j = random.randint(0, len(unused_index)-1)
        j = unused_index[j]
    # print(j)
    # print(pi, phs[k])
    # break
    # print(pi, phs[j])
    if DEBUG:
        st = score(pi, phs[j])
        fscore += st
        print("best score:" , st,"using:{}, {}".format(index, j))
        pi0 = ph[j]
    else:
        print(j) # index
    i = j
    pi = phs[j].copy()
    pi0 = ph[j]
    used_index.add(j)
    unused_index.remove(j)


if DEBUG:
    print(fscore)

