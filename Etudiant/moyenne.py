from Note import *

def moyenne():
    nt=note()

    if nt ==0:
        return 0
    return sum(nt)/len(nt)

