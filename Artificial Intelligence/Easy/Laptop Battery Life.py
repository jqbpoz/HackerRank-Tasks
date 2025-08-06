#!/bin/python3

import math
import os
import random
import re
import sys

with open('trainingdata.txt') as file:
    charged = []
    lasted = []

    for line in file:
        if ',' not in line:
            continue
        ch, la = line.strip().split(',')
        ch = float(ch)
        la = float(la)
        charged.append(ch)
        lasted.append(la)

data = sorted(zip(charged, lasted))

if __name__ == '__main__':
    timeCharged = float(input().strip())

    for i in range(len(data)):
        if abs(data[i][0] - timeCharged) < 1e-6:
            print(f"{data[i][1]:.2f}")
            sys.exit()

    for i in range(1, len(data)):
        x0, y0 = data[i - 1]
        x1, y1 = data[i]
        if x0 <= timeCharged <= x1:
            slope = (y1 - y0) / (x1 - x0)
            pred = y0 + slope * (timeCharged - x0)
            print(f"{pred:.2f}")
            sys.exit()

    if timeCharged < data[0][0]:
        print(f"{data[0][1]:.2f}")
    else:
        print(f"{data[-1][1]:.2f}")
