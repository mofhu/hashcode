# print(fin)
n = int(input())

photos = []
ph = [] # H
pv = [] # V
phs = []

# s1 = set(["a","b","c"])
# s2 = set(["d","b","c"])
def score(s1, s2):
    ins = s1.intersection(s2)
    s12 = s1-s2
    s21 = s2-s1
    # if len(ins) > 0:
    #     print(s1, s2,len(ins), len(s12), len(s21))
    # print(ins)
    # rint(s12)
    # print(s21)
    return min(len(ins), len(s12), len(s21))
# score(s1, s2)

for i in range(n):
    p = input().split(" ")
    photos.append([i]+ p)
    if p[0] == "H":
        ph.append([i]+ p)
        phs.append(set(p[2:]))
    else:
        pv.append([i]+ p)
# print(phs)

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
pi = phs[i]
st = 0
# set to random init later
while len(ph) > 0:  # for b
    # print("cycle count:", len(ph))
    t = 0
    # print(pi, phs[k])
    # break
    st = score(pi, phs[0])
    # print(st)
    for j in range(min(1000,len(ph))):
        # print(j)
        # j is index
        sj = score(pi, phs[j])
        if sj > st:
            t = j
            st = sj
    # print("best score:" , st, ph[t][0])
    print(ph[t][0]) # index
    pi = phs[t]
    del ph[t]
    del phs[t]


