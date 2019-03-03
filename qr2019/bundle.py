import os
from sys import argv
import datetime

script, case, DEBUG, NITER, THRESHOLD = argv
if case == "b":
    case = "< b_lovely_landscapes.txt > b.out"
    check = "b_lovely_landscapes.txt b.out"
elif case == "c":
    case = "< c_memorable_moments.txt > c.out"
    check = "c_memorable_moments.txt c.out"
elif case == "d":
    case = "< d_pet_pictures.txt > d.out"
    check = "d_pet_pictures.txt d.out"
elif case == "e":
    case = "< e_shiny_selfies.txt > e.out"
    check = "e_shiny_selfies.txt e.out"

print(datetime.datetime.now())
os.system("python opt.py {} {} {} {}".format(DEBUG, NITER, THRESHOLD, case))
os.system("./checker {} 0".format(check))
print(datetime.datetime.now())
