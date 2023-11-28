import os
import numpy as np
from tqdm import tqdm
from datetime import date


with open('formulalist.npy', 'rb') as f:
    a = np.load(f)

with open('formulalist_old.npy', 'wb') as f:
    np.save(f, a)

print("Number of formulas = "+str(np.size(a)))


# Put names of formulas to remove manually in this array
manual_removal_formulas=['redwax-tool']

print("Removing manually selected formulas")
for i in manual_removal_formulas:
    a=np.delete(a,np.where(a==i))
print("Number of formulas = "+str(np.size(a)))

logfilename=str(date.today())

with open(logfilename, 'r') as file:
    op = file.read().split('\n')

auto_removal_formulas=[]

for i in tqdm(op):
    if i!='':
        l=i.split(": ")
        if l[0]!='':
            if l[1] in ['unversioned','latest','discontinued','deprecated','versioned','disabled'] or l[0] in ['Error','Warning','git','fatal'] or l[1].startswith('skipped - '):
                auto_removal_formulas.append(l[0])

print("Removing automatically filtered formulas")
for i in tqdm(auto_removal_formulas):
    a=np.delete(a,np.where(a==i))
print("Number of formulas = "+str(np.size(a)))

with open('formulalist.npy', 'wb') as f:
    np.save(f, a)
