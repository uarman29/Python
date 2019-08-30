import os
import argparse
import operator
from send2trash import send2trash


parser = argparse.ArgumentParser(description="File Deleter")
parser.add_argument('-n', required=True, action='store', help='How many files do you want to keep?')
parser.add_argument('-f', required=True, action='store', help='What format do you want to limit?')
args = parser.parse_args()

MAXIMUM_FILES = int(args.n)
FILE_TYPE = args.f
DIRECTORY = "C:\\Users\\auddin\\Desktop\\Mandiant Output"

names = os.listdir(DIRECTORY)
dates = {}

for name in names:
    if not name.endswith("." + FILE_TYPE):
        names.remove(name)

if len(names) > MAXIMUM_FILES:
    for name in names:
        creation_time = os.path.getctime(DIRECTORY + "\\" + name)
        dates[DIRECTORY + "\\" + name] = creation_time

sorted_dates = sorted(dates.items(),key=operator.itemgetter(1))

while len(sorted_dates) > MAXIMUM_FILES:
    send2trash(sorted_dates[0][0])
    sorted_dates.pop(0)



