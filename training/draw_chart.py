import matplotlib.pyplot as plt
import os
import re
import numpy as np

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def getLogData(dir):
    f = open(dir)
    lostlist = []
    maplist = []
    maplist.append(0)
    listlines = f.readlines()
    regex = re.compile("\d[:]")
    
    for line in listlines:
        if regex.search(line):
            loss = line.split(",")[0]
            loss = float(loss.split(":")[1].strip())
            lostlist.append(loss)
        if "mean average precision (mAP@0.50)" in line:
            mAP = float(line.split(",")[1].replace("or", "").replace("%","").strip())
            maplist.append(mAP)

    return lostlist, maplist



def drawChart(ll, ml):
    iterations = [i for i in range(0,25000)]
    mapiterations = [i for i in range(0,25001,1000)]
    ml = np.array(ml) / 10
    
    plt.xlabel('Iteraciones')
    plt.ylabel('Perdida')
    plt.axis([0, 25000, 0, 2])
    plt.yticks(np.arange(0, 11, 1))
    plt.xticks(np.arange(0, 25000, 2500))
    plt.minorticks_on()
    plt.grid(True, color='grey', ls = '-.', lw = 0.25, which='minor')
    plt.grid(True, color='grey', ls = '-', lw = 0.5, which='major')
    plt.plot(iterations, ll, 'ro', markersize=0.3, color = "blue")
    plt.plot(mapiterations, ml, markersize=0.3, color = "orange")
    
    for i, element in enumerate(ml):
        truc = truncate(element * 10, 1)
        plt.text(mapiterations[i], element, truc)

    plt.show()
    















if __name__ == "__main__":
    ll, ml = getLogData("training/logs/log.txt")
    drawChart(ll, ml)
    