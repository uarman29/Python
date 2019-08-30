import xml.etree.ElementTree as ET
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
tree = ET.parse(filename)
root = tree.getroot()
IoCs = root[1][0]

filename = askopenfilename()
tree_other = ET.parse(filename)
root_other = tree_other.getroot()
IoCs_other = root_other[1][0]


def xstr(s):
    return '' if s is None else str(s)


report_Ids = []
for IoC in IoCs.findall('indicatorsOfCompromise'):
    report_Ids.append(xstr(IoC[0].text)+xstr(IoC[20].text)+xstr(IoC[32].text)+xstr(IoC[41].text)+xstr(IoC[35].text))

report_Ids_other = []
for IoC in IoCs_other.findall('indicatorsOfCompromise'):
    report_Ids_other.append(xstr(IoC[0].text) + xstr(IoC[20].text) + xstr(IoC[32].text) + xstr(IoC[41].text) + xstr(IoC[35].text))

#print(report_Ids)
#print(report_Ids_other)

diff1 = list(set(report_Ids) - set(report_Ids_other))
diff2 = list(set(report_Ids_other) - set(report_Ids))
print(len(report_Ids))
print(len(diff1))
