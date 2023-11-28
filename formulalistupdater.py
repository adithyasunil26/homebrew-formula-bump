import os
import numpy as np

dir = os.getcwd()

os.chdir('/usr/local/Homebrew/Library/Taps/homebrew/homebrew-core/Formula')

formulas = []

for i in os.listdir():
    for j in os.listdir(i):
        formulas.append(j.split('.')[0])

os.chdir(dir)

with open('formulalist.npy', 'wb') as f:
    np.save(f, formulas)

print("Number of formulas = "+str(np.size(formulas)))
