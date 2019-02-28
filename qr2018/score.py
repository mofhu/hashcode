from sys import argv
script, fin, fout = argv
# print(fin)
fin = open(fin)
fout = open(fout)

r, c, f, n, b, tmax = [int(s) for s in fin.readline().split(" ")]
rides = []

def dist(x0,y0,x1,y1):
    return abs(x0-x1) + abs(y0-y1)

for i in range(n):
    ride = [int(s) for s in fin.readline().split()]
    l = abs(ride[0] - ride[2]) + abs(ride[1]- ride[3])
    dt = ride[5] - ride[4]
    rides.append(ride + [l, dt, i])

score = 0
lines = fout.readlines()
# print(lines)
for line in lines:
    if line != "\n":
    # print(line)
        t0 = 0
        x, y = 0,0
        # no bonus
        line = [int(s) for s in line.split(" ")]
        # print(line)
        nride = line[0]
        for i in range(1, nride+1):
            vr = rides[line[i]]
            t = dist(x, y, vr[0], vr[1]) + vr[6]
            t0 += t
            if t <= vr[5]:
                score += vr[6]
        line = fout.readline()

print("{}".format(score))

