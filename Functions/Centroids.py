from MaxIntCentroids import *
def Centroids(SignalsMat,AdjacencyMatrix):
    TempSignalsMat=SignalsMat.copy()
    TempAdjacencyMatrix=AdjacencyMatrix.copy()
    KernelIDs=[]
    features=0
    features=MaxIntCentroids(SignalsMat=TempSignalsMat,AdjacencyMatrix=TempAdjacencyMatrix,Fragment=1,KernelIDs=KernelIDs,features=features) 
    features=MaxIntCentroids(SignalsMat=TempSignalsMat,AdjacencyMatrix=TempAdjacencyMatrix,Fragment=2,KernelIDs=KernelIDs,features=features) 
    return KernelIDs
