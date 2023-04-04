from scipy.stats import shapiro
from scipy.stats import t
from scipy import stats
import numpy as np
def ClusterStats(SignalsMat,alpha=0.01):       
    SumIntens=sum(SignalsMat[:,5])
    RelativeInt=SignalsMat[:,5]/SumIntens
    AverageMZ=sum(SignalsMat[:,0]*RelativeInt)    
    AverageMZ2=sum(SignalsMat[:,1]*RelativeInt)    
    Difference=AverageMZ2-AverageMZ
    AverageRT=sum(SignalsMat[:,7]*RelativeInt)
    l=len(SignalsMat[:,1])    
    if l<3:
        return np.zeros(9)
    VarianMZ=sum(RelativeInt*(SignalsMat[:,0]-AverageMZ)**2)*l/(l-1)    
    StdMZ=np.sqrt(VarianMZ)
    VarianRT=sum(RelativeInt*(SignalsMat[:,7]-AverageRT)**2)*l/(l-1)    
    StdRT=np.sqrt(VarianRT)    
    tref=stats.t.interval(1-alpha, l-1)[1]
    ConfidenceIntervalDa=tref*StdMZ/np.sqrt(l)
    ConfidenceInterval=ConfidenceIntervalDa/AverageMZ*1e6
    ClusterStats=[AverageRT,StdRT,AverageMZ,StdMZ,l,ConfidenceIntervalDa,ConfidenceInterval,AverageMZ2,Difference]      
    #print(PeakStats)
    return ClusterStats
