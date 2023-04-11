from SignalsStats import *
from WelchTest import *
import numpy as np
def ClusterStats(SignalsMat,alpha=0.05):               
    #Difference=AverageMZ2-AverageMZ
    #Light isotopomer mz1
    LightSignalsSum=SignalsStats(SignalsMat,Isotopomer=0,alpha=alpha)
    HeavySignalsSum=SignalsStats(SignalsMat,Isotopomer=1,alpha=alpha) 
    WelchVec=WelchTest(SignalsStats1=LightSignalsSum,SignalsStats2=HeavySignalsSum,alpha=alpha)
    ClusterStats=LightSignalsSum
    ClusterStats.extend(HeavySignalsSum)
    ClusterStats.extend(WelchVec)
    #print(PeakStats)
    return ClusterStats
