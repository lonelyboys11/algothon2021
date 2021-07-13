#!/usr/bin/envblah python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

nInst=100
currentPos = np.zeros(nInst)

def getMyPosition(prcSoFar):
    global currentPos
    (nins,nt) = prcSoFar.shape
    currentPos = np.zeros(100)

    new = prcSoFar / np.roll(prcSoFar, (1, 0), axis=1)
    new[:, 0] = np.ones(shape=new[:, 0].shape)
    price_move = np.log(new)

    currentPos[0:50] = np.where(np.log(prcSoFar[0:50, -1]/prcSoFar[0:50, 0])/nt > np.log(1 + 0.00075), 10000000000, np.where(np.log(prcSoFar[0:50, -1]/prcSoFar[0:50, 0])/nt < np.log(1 - 0.00075), -10000000, 0))
    currentPos[50:100] = np.where(price_move[50:100, -1] > np.log(1.00), -10000000, np.where(price_move[50:100, -1] < np.log(1.0), 10000000, 0))

    # The algorithm must return a vector of integers, indicating the position of each stock.
    # Position = number of shares, and can be positve or negative depending on long/short position.
    return currentPos
