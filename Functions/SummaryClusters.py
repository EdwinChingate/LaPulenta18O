#Summarizing the clusters. We need additional grouping in between the clusters 
#This will become another function
#Always using mz1 as reference
from ClusterStats import *
import pandas as pd
def SummaryClusters(SignalsMat,ModList,MinNumberCandidatesClustering=3,ReturnDF=True,columns=["AverageRT_1","StdRT_1","AverageMZ_1","StdMZ_1","l_1","ConfidenceIntervalDa_1","ConfidenceInterval_1","AverageRT_2","StdRT_2","AverageMZ_2","StdMZ_2","l_2","ConfidenceIntervalDa_2","ConfidenceInterval_2",'Difference','ConfidenceInterval','ConfidenceInterval(ppm)_dif','ConfidenceInterval(ppm)_mz1','ConfidenceInterval(ppm)_mz2', "tref","stMix"]):    
    Summary=[]
    for x in ModList:
        modNet=list(set(x))
        Summary.append(ClusterStats(SignalsMat[modNet,:]))
    SummaryArray=np.array(Summary)
    #ShowDF(pd.DataFrame(SummaryArray))
    SummaryFilter_Loc=np.where(SummaryArray[:,4]>MinNumberCandidatesClustering)[0]
    SummaryArr=SummaryArray[SummaryFilter_Loc,:].copy()
    SummaryArrSort=np.argsort(SummaryArr[:,2])
    if ReturnDF:
        SummaryDF=pd.DataFrame(SummaryArr[SummaryArrSort,:],columns=columns)    
      #  ShowDF(SummaryDF)
        return SummaryDF
    else:
        return SummaryArr[SummaryArrSort,:]
