from ClusterStats import *
import pandas as pd
def RawKernel(SignalsMat,KernelIDs,alpha=0.01,ReturnDF=True,columns=["AverageRT_1","StdRT_1","AverageMZ_1","StdMZ_1","l_1","ConfidenceIntervalDa_1","ConfidenceInterval_1","SumIntensity_1"]):    
    Kernel=[]
    counter=0
    for cent in KernelIDs:
        Kernel.append(SignalsStats(SignalsMat[cent,:],Isotopomer=0,alpha=alpha))        
        counter+=1
    KernelArray=np.array(Kernel)
    #KernelSort=np.argsort(KernelArray[:,0])
    if ReturnDF:
        SummaryDF=pd.DataFrame(KernelArray[KernelSort,:],columns=columns)    
        return SummaryDF
    else:
        return KernelArray#[KernelSort,:]
