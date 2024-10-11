from Signals_Stats import *
from WelchTest import *
import numpy as np
import gc
def Cluster_Stats(SignalsMat,alpha=0.01,TheoricalDif=2.0042449932959006):               
    SignalsStats_LightSignalsSum=Signals_Stats(SignalsMat,Isotopomer=0,alpha=alpha)
    SignalsStats_HeavySignalsSum=Signals_Stats(SignalsMat,Isotopomer=1,alpha=alpha)
    WelchVec=WelchTest(SignalsStats1=SignalsStats_LightSignalsSum,SignalsStats2=SignalsStats_HeavySignalsSum,alpha=alpha)
    Dif=WelchVec[0]
    CI_Dif=WelchVec[1]
    v=0
    if abs(TheoricalDif-Dif)<CI_Dif:
        v=1 
    ClusterStats=SignalsStats_LightSignalsSum
    ClusterStats.extend(SignalsStats_HeavySignalsSum)
    ClusterStats.extend(WelchVec)    
    ClusterStats.insert(0,v)
    del SignalsStats_LightSignalsSum
    del SignalsStats_HeavySignalsSum
    del WelchVec
    gc.collect()
    return ClusterStats
