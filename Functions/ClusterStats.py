from SignalsStats import *
from WelchTest import *
import numpy as np
def ClusterStats(SignalsMat,alpha=0.01,TheoricalDif=2.0042449932959006):               
    #Difference=AverageMZ2-AverageMZ
    #Light isotopomer mz1
    LightSignalsSum=SignalsStats(SignalsMat,Isotopomer=0,alpha=alpha)[:-1]
    HeavySignalsSum=SignalsStats(SignalsMat,Isotopomer=1,alpha=alpha)[:-1]
    #print(len(LightSignalsSum),len(LightSignalsSum))
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
    #print(PeakStats)
    return ClusterStats
