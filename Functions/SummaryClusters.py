#Summarizing the clusters. We need additional grouping in between the clusters 
#This will become another function
#Always using mz1 as reference
from ClusterStats import *
import pandas as pd
def SummaryClusters(SignalsMat,ModList,MinNumberCandidatesClustering=3,ReturnDF=True):    
    Summary=[]
    for x in ModList:
        modNet=list(set(x))
        Summary.append(ClusterStats(SignalsMat[modNet,:]))
    SummaryArray=np.array(Summary)
   # ShowDF(pd.DataFrame(SummaryArray))
    SummaryFilter_Loc=np.where(SummaryArray[:,4]>MinNumberCandidatesClustering)[0]
    SummaryArr=SummaryArray[SummaryFilter_Loc,:].copy()
    SummaryArrSort=np.argsort(SummaryArr[:,2])
    if ReturnDF:
        SummaryDF=pd.DataFrame(SummaryArr[SummaryArrSort,:],columns=['RT(min)','std_RT','Mean_mz','std_mz','NSignals','ConfidenceInteval_mz1(Da)','ConfidenceInteval_mz1(ppm)','Mean_mz2','Difference'])    
      #  ShowDF(SummaryDF)
        return SummaryDF
    else:
        return SummaryArr[SummaryArrSort,:]
