from SignalsStats import *
from WelchTest import *
import numpy as np
import gc
def ClusterStats(SignalsMat,alpha=0.01,TheoricalDif=2.0042449932959006):               
    LightSignalsSum=SignalsStats(SignalsMat,Isotopomer=0,alpha=alpha)
    HeavySignalsSum=SignalsStats(SignalsMat,Isotopomer=1,alpha=alpha)
    WelchVec=WelchTest(SignalsStats1=LightSignalsSum,SignalsStats2=HeavySignalsSum,alpha=alpha)
    Dif=WelchVec[0]
    CI_Dif=WelchVec[1]
    v=0
    if abs(TheoricalDif-Dif)<CI_Dif:
        v=1 
    ClusterStats=LightSignalsSum
    ClusterStats.extend(HeavySignalsSum)
    ClusterStats.extend(WelchVec)    
    ClusterStats.insert(0,v)
    del LightSignalsSum
    del HeavySignalsSum
    del WelchVec
    gc.collect()
    return ClusterStats
