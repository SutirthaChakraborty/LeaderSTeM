import os

txt="list2.txt"
with open(txt) as f:
    lines=f.read().splitlines()
for i in lines:
    print(i)
    os.system("python ArrangeDataset.py "+i)