from sys import argv
script, fin = argv
# print(fin)
fin = open(fin)

r, c, f, n, b, tmax = [int(s) for s in fin.readline().split(" ")]
rides = []

def dist(x0,y0,x1,y1):
    return abs(x0-x1) + abs(y0-y1)

for i in range(n):
    ride = [int(s) for s in fin.readline().split()]
    l = abs(ride[0] - ride[2]) + abs(ride[1]- ride[3])
    dt = ride[5] - ride[4]
    rides.append(ride + [l, dt, i])


# first set cars for earliest rides
rides.sort(key=lambda x:x[4])

# arrange from first car to last, other routes ignored.
for i in range(f):
    # print(rides)
    ans = [0]
    j = 0
    clear = [] # clear all in list
    t0 = 0
    x,y = 0,0
    for j in range(len(rides)):
        rj = rides[j]
        t = t0 + dist(x,y, rj[0], rj[1])
        # print("t, rj4:", t, rj[4])
        if t <= rj[5]-rj[6]:
            ans[0] += 1
            ans.append(str(rj[8]))
            clear.append(j)
            t0 = t + rj[6]
            x, y = rj[2], rj[3]
            # print("t0xy", t0, x,y)
    clear.sort(reverse=True)
    for k in clear:
        del rides[k]
    ans[0] = str(ans[0])

    print(" ".join(ans))
print("\n")

