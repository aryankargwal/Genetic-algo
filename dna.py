import random
import time
import numpy as np
import matplotlib.pyplot as plt

char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "

random.seed(0)


class dna:
    def __init__(self, st):
        self.str = st
        self.score = 0
        self.SkiwFitness = 78

    # function to mix two dna objects. selects ranndom piviot and joins them
    def cross(self, p2):
        length = random.randrange(0, len(p2.str))
        return dna(self.str[:length] + p2.str[length:])

    def mutate(self):
        i = self.str
        mm = random.randrange(1, len(i) + 1)
        while mm:
            ch = random.choices(char, k=1)
            pivt = random.randrange(1, len(i) + 1)
            i = i[: pivt - 1] + ch[0] + i[pivt:]
            mm -= 1
        self.str = i
