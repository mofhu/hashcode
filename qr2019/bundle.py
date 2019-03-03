import os
from sys import argv
import datetime

script, DEBUG, THRESHOLD = argv

print(datetime.datetime.now())
os.system("python opt.py {} {} < b_lovely_landscapes.txt > b.out".format(DEBUG, THRESHOLD))
os.system("./checker b_lovely_landscapes.txt b.out 0")
print(datetime.datetime.now())
os.system("python opt.py {} {} < c_memorable_moments.txt > c.out".format(DEBUG, THRESHOLD))
os.system("./checker c_memorable_moments.txt c.out 0")
print(datetime.datetime.now())
os.system("python opt.py {} {} < d_pet_pictures.txt > d.out".format(DEBUG, THRESHOLD))
os.system("./checker d_pet_pictures.txt d.out 0")
print(datetime.datetime.now())
os.system("python opt.py {} {} < e_shiny_selfies.txt > e.out".format(DEBUG, THRESHOLD))
os.system("./checker e_shiny_selfies.txt e.out 0")
print(datetime.datetime.now())
