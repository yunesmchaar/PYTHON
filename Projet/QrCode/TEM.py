import math
from itertools import count

from fontTools.misc.psCharStrings import T2WidthExtractor

import math

def fun_recuit_iter(Tmin,Tmax):
    taux = math.exp(4)
    count = 0
    a = 0

    while Tmin <= Tmax:
        T = Tmin * math.exp(a / -taux)
        Tmin += 0.1
        a += 1
        count += 1
    print("le counteur egale:",count)
    print("T=",T)
print(fun_recuit_iter(9, 10))
