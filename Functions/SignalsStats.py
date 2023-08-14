from scipy.stats import t
import numpy as np
def SignalsStats(SignalsMat,Isotopomer=0,alpha=0.01): #Isotopomer refers to either the most abundant isotopomer, or the one with 18O
    IntensityCol=5+Isotopomer
    SumIntens=sum(SignalsMat[:,IntensityCol])
    RelativeInt=SignalsMat[:,IntensityCol]/SumIntens
    AverageMZ=sum(SignalsMat[:,Isotopomer]*RelativeInt)
    AverageRT=sum(SignalsMat[:,7]*RelativeInt)
    l=len(SignalsMat[:,1])    
    VarianMZ=sum(RelativeInt*(SignalsMat[:,Isotopomer]-AverageMZ)**2)*l/(l-1)  
    StdMZ=np.sqrt(VarianMZ)
    VarianRT=sum(RelativeInt*(SignalsMat[:,7]-AverageRT)**2)*l/(l-1)    
    StdRT=np.sqrt(VarianRT)    
    tref=t.interval(1-alpha, l-1)[1]
    ConfidenceIntervalDa=tref*StdMZ/np.sqrt(l)
    ConfidenceInterval=ConfidenceIntervalDa/AverageMZ*1e6
    SignalsStats=[AverageRT,StdRT,AverageMZ,StdMZ,l,ConfidenceIntervalDa,ConfidenceInterval,SumIntens]
    return SignalsStats
