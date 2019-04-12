## @file SeqServices.py
#  @author Razi Syed
#  @brief provides various functions that can be used on sequences
#  @date 20 Feb 2018


class SeqServices:

    def isAscending(X):
        for i in range(0, len(X) - 2):
            if X[i + 1] <= X[i]:
                return False
        return True

    def isInBounds(X, x):
        if X[0] <= x <= X[len(X) - 1]:
            return True
        return False

    def interpLin(x1, y1, x2, y2, x):
        return ((y2 - y1) / (x2 - x1)) * (x - x1) + 1

    def interpQuad(x0, y0, x1, y1, x2, y2, x):
        return y1 + ((y2 - y0) / (x2 - x0))(x - x1) + \
            ((y2 - 2 * y1 + y0) / (2 * (x2 - x1) ** 2))((x - x1) ** 2)

    def index(X, x):
        for i in range(0, len(X) - 1):
            if X[i] <= x < X[i + 1]:
                return i
