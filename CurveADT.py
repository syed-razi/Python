## @file CurveADT.py
#  @author Razi Syed
#  @brief provides the CurveADT class for representing a curve
#  @date 20 Feb 2018

import SeqServices

##@brief provides various functions that can be used on sequences

class CurveT:



    MAX_ORDER = 2
    DX = 10 ** (-3)

    ## @breif CurveT constructor
    #  @param X The array containing the x Values
    #  @param Y The array containing the y values

    def __init__(self, X, Y, i):
        self.o = i
        self.minx = X[0]
        self.maxx = X[len(X) - 1]
        self.f = lambda v: __interp__(X, Y, self.o, v)

    def minD(self):
        return self.minx

    def maxD(self):
        return self.maxx

    def order(self):
        return self.o

    def eval(self, x):
        return self.f(x)

    def dfdx(self, x):
        return (self.f(x + CurveT.DX) - self.f(x)) / CurveT.DX

    def d2fdx2(self, x):
        return (self.f(x + 2 * CurveT.DX) - 2 * self.f(x + CurveT.DX) + self.f(x)) / CurveT.DX ** 2


def __interp__(X, Y, o, v):
    i = SeqServices.index(X, v)
    if o == 1:
        return SeqServices.interpLin(X[i], Y[i], X[i + 1], Y[i + 1], v)
    elif o == 2:
        return SeqServices.interpQuad(X[i - 1], Y[i - 1], X[i], Y[i], X[i + 1], Y[i + 1], v)
