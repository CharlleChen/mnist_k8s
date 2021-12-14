import matplotlib.pyplot as plt
import numpy as np

num = ['1', '3', '5']
for n in num:
  path = f'3_cpu_{n}node'
  with open(path, 'r') as f:
    lines = f.readlines()
    lines = [l for l in lines if 'seconds' in l]
    times = [float(i.split()[0]) for i in lines]
    print(n, np.mean(times), np.std(times))

