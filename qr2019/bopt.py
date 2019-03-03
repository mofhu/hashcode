import os
from sys import argv
import datetime

script, DEBUG, THRESHOLD = argv

print(datetime.datetime.now())
os.system("python opt.py {} {} < b_lovely_landscapes.txt > b.out".format(DEBUG, THRESHOLD))
os.system("./checker b_lovely_landscapes.txt b.out 0")
print(datetime.datetime.now())
