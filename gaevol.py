# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 10:20:16 2020

@author: Abhishek

this script is using GA to guess the given string, the cross over function is
using one random piviot to cross genes (should be 2 or more for better results)
"""

# imports
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from population import population

random.seed(0)


def gaevol(a):
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    pltdata = []
    end = a
    pop = 500
    mutrate = 0.001

    st = time.time()
    driver = population(end, pop, mutrate)

    while driver.sticfac():
        driver.eva()
        # time.sleep(5)
        driver.breedprep()
        driver.breed()
    print(time.time() - st, "sec")
