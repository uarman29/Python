import os
import time
import argparse
from send2trash import send2trash


parser = argparse.ArgumentParser(description="File Deleter")
parser.add_argument('-d', required=True, action='store', help='How many days do you want to keep?')
args = parser.parse_args()

MAXIMUM_DAYS = int(args.d)
DIRECTORY = "C:\\Users\\auddin\\Desktop\\Mandiant Output"
TRASH = ""
CURRENT_TIME = time.time()
CUTOFF_TIME = CURRENT_TIME - MAXIMUM_DAYS * 24 * 60 * 60

names = os.listdir(DIRECTORY)

for name in names:
    if not name.endswith(".xml"):
        names.remove(name)

for name in names:
    creation_time = os.path.getctime(DIRECTORY + "\\" + name)
    if creation_time < CUTOFF_TIME:
        #os.remove(DIRECTORY + "\\" + name)
        send2trash(DIRECTORY + "\\" + name)



