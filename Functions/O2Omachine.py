from AdjacencyMatGen import *
from Centroids import *
from RawKernel import *
from ModulesK_Nearst import *
from SummaryClusters import *
from ShowDF import *
import gc
def O2Omachine(DataSetName,SignalsMat,min_mz=80,max_mz=1000,minInt=1e4,MinSignalsSpectra=10,ML=1,MinDif=2.0038,MaxDif=2.0046,min_RT=0,max_RT=100,max_mz_Tol=5e-3,max_RT_Tol=0.3,FeaturesNumber=500,MinSignals=3,MinIntKernel=5e4,alpha=0.01,MaxDeep=3,SafetyFactor=4,TheoricalDif=2.0042449932959006,MinNumberCandidatesClustering=3):
    AdjacencyMatrix=AdjacencyMatGen(SignalsMat=SignalsMat,max_mz_Tol=max_mz_Tol)
    KernelIDs=Centroids(SignalsMat=SignalsMat,AdjacencyMatrix=AdjacencyMatrix,FeaturesNumber=FeaturesNumber,MinSignals=MinSignals,MinIntKernel=MinIntKernel) 
    Kernel=RawKernel(SignalsMat=SignalsMat,KernelIDs=KernelIDs,alpha=alpha)   
    Modules=ModulesK_Nearst(SignalsMat=SignalsMat,Kernel=Kernel,SafetyFactor=SafetyFactor)
    SummaryCluster=SummaryClusters(SignalsMat=SignalsMat,Modules=Modules,MinNumberCandidatesClustering=MinNumberCandidatesClustering,alpha=alpha,TheoricalDif=TheoricalDif) #Add a filter here
    ShowDF(SummaryCluster)	
    SummaryCluster.to_excel(DataSetName+'.xlsx')
    del AdjacencyMatrix
    del KernelIDs
    del Kernel
    del SummaryCluster
    del Modules    
    gc.collect()
