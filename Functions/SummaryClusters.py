#Summarizing the clusters. We need additional grouping in between the clusters 
#This will become another function
#Always using mz1 as reference
from ClusterStats import *
import pandas as pd
import numpy as np
def SummaryClusters(SignalsMat,Modules,MinNumberCandidatesClustering=3,alpha=0.01,TheoricalDif=2.0042449932959006,ReturnDF=True,columns=["Pass","AverageRT_1","StdRT_1","AverageMZ_1","StdMZ_1","l_1","ConfidenceIntervalDa_1","ConfidenceInterval_1","SumInt_1","AverageRT_2","StdRT_2","AverageMZ_2","StdMZ_2","l_2","ConfidenceIntervalDa_2","ConfidenceInterval_2","SumInt_2",'Difference','ConfidenceInterval','ConfidenceInterval(ppm)_dif','ConfidenceInterval(ppm)_mz1','ConfidenceInterval(ppm)_mz2', "tref","stMix"]):    
    Summary=[]
    for x in Modules:
        modNet=list(set(x))
        Summary.append(ClusterStats(SignalsMat[modNet,:],alpha=alpha,TheoricalDif=TheoricalDif))
    SummaryArray=np.array(Summary)
    SummaryFilter_Loc=np.where(SummaryArray[:,5]>MinNumberCandidatesClustering)[0]
    SummaryArr=SummaryArray[SummaryFilter_Loc,:].copy()
    SummaryArrSort=np.argsort(SummaryArr[:,3])
    if ReturnDF:
        SummaryDF=pd.DataFrame(SummaryArr[SummaryArrSort,:],columns=columns)    
        return SummaryDF
    else:
        return SummaryArr[SummaryArrSort,:]
