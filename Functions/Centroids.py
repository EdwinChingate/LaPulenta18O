from MaxIntCentroids import *
import gc
def Centroids(SignalsMat,AdjacencyMatrix,FeaturesNumber=500,MinSignals=3,MinIntKernel=3e4,MaxDeep=3):
    TempSignalsMat=SignalsMat.copy()
    TempAdjacencyMatrix=AdjacencyMatrix.copy()
    KernelIDs=[]
    features=0
    features=MaxIntCentroids(SignalsMat=TempSignalsMat,AdjacencyMatrix=TempAdjacencyMatrix,Fragment=1,KernelIDs=KernelIDs,features=features,FeaturesNumber=FeaturesNumber,MinSignals=MinSignals,MinIntKernel=MinIntKernel,MaxDeep=MaxDeep) 
    features=MaxIntCentroids(SignalsMat=TempSignalsMat,AdjacencyMatrix=TempAdjacencyMatrix,Fragment=2,KernelIDs=KernelIDs,features=features,FeaturesNumber=FeaturesNumber,MinSignals=MinSignals,MinIntKernel=MinIntKernel,MaxDeep=MaxDeep) 
    del TempSignalsMat
    del TempAdjacencyMatrix
    gc.collect()
    return KernelIDs
