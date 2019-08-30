import xml.etree.ElementTree as ET
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
tree = ET.parse(filename)
root = tree.getroot()

counter = 0
IoCs = root[1][0]
#print(root[1][0][0][20].tag)
#print(root[1][0][0][32].tag)
#print(root[1][0][0][41].tag)

def xstr(s):
    return '' if s is None else str(s)
'''
report_Ids =[]
for IoC in IoCs.findall('indicatorsOfCompromise'):
    report_Ids.append(xstr(IoC[20].text)+xstr(IoC[32].text)+xstr(IoC[41].text))

report_Ids = list(dict.fromkeys(report_Ids))
print(report_Ids)
'''
total_count = 0
report_Ids = {}
for IoC in IoCs.findall('indicatorsOfCompromise'):
    total_count += 1
    report_Ids[xstr(IoC[0].text)+xstr(IoC[20].text)+xstr(IoC[32].text)+xstr(IoC[41].text)+xstr(IoC[35].text)] = report_Ids.get((xstr(IoC[0].text)+xstr(IoC[20].text)+xstr(IoC[32].text)+xstr(IoC[41].text)+xstr(IoC[35].text)), 0) +1

#print(report_Ids)
print(total_count)

print(len(report_Ids))

for key in report_Ids:
    if report_Ids[key] != 1:
        print(key,report_Ids[key])

########## reportId+md5+domain+url+ip is unique###################