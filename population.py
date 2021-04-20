import random
import time
import numpy as np
import matplotlib.pyplot as plt
from dna import dna

char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
pltdata = []


class population:
    def __init__(self, end, pop, rate):
        self.end = end
        self.length = len(end)
        self.pop = pop
        self.rate = rate
        self.gen = 1
        self.reach = True
        self.pool = []

        for _ in range(pop):
            self.pool.append(self.randinit())
            # print(self.pool[_].str)
        self.pool = np.array(self.pool)

    def randinit(self):
        temp = "".join(random.choices(char, k=self.length))
        return dna(temp)

    def eva(self):
        for j in self.pool:
            count = 0

            for i in range(self.length):

                if j.str[i] == self.end[i]:
                    count += 1 * self.gen

            if count <= 0:
                count = 0.0001

            j.score = count

        sorted(self.pool, key=lambda x: x.score)

        if self.length == self.pool[self.pop - 1].score / self.gen:
            self.reach = False

        # np.append(pltdata,[self.pool[self.pop-1].score])
        pltdata.append([self.pool[self.pop - 1].score])
        print(self.pool[self.pop - 1].str, self.pool[self.pop - 1].score, self.gen)

    def breedprep(self):
        tmpSum = 0
        self.pool = self.pool[::-1]
        for i in self.pool:
            tmpSum += i.score
        fitsum = 0
        for i in self.pool:
            i.SkiwFitness = i.score / tmpSum + fitsum
            fitsum = i.SkiwFitness

    def selection(self, n):
        for i in self.pool:
            if i.SkiwFitness > n:
                # print(i.SkiwFitness,"    ",n)
                return i
        return i

    def breed(self):
        pool2 = np.array([dna(" ") for i in range(self.pop)])
        for i in range(0, self.pop, 2):
            # print(self.pool[i].SkiwFitness,end=",")
            p1 = random.random()
            p2 = random.random()
            while p1 == p2:
                p2 = random.random()
            p1 = self.selection(p1)
            p2 = self.selection(p2)
            h1 = p1.cross(p2)
            h2 = p2.cross(p1)
            mutchance = random.random()
            if mutchance <= self.rate:
                h1.mutate()
                h2.mutate()
            pool2[i] = h1
            pool2[i + 1] = h2
        self.pool = pool2

    def sticfac(self):
        self.gen += 1
        return self.reach
