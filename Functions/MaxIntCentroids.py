import numpy as np
from ModulesDetMax import *
import gc
def MaxIntCentroids(SignalsMat,AdjacencyMatrix,Fragment=1,KernelIDs=[],features=0,FeaturesNumber=500,MinSignals=3,MinIntKernel=3e4,MaxDeep=3):        
    MaxInt=MinIntKernel*1.5
    while features<FeaturesNumber and MaxInt>MinIntKernel:
        MaxInt=np.max(SignalsMat[:,4+Fragment])
        Loc=np.where(SignalsMat[:,4+Fragment]==MaxInt)[0][0]
        Module=ModulesDetMax(MaxID=Loc,AdjacencyMatrix=AdjacencyMatrix,Module=[Loc],MaxDeep=MaxDeep)       
        del Loc
        if len(Module)>MinSignals:
            KernelIDs.append(list(set(Module)))
            features+=1
        SignalsMat[Module,5]=0
        SignalsMat[Module,6]=0
        del Module
        gc.collect()
    del MaxInt     
    gc.collect()
    if features==FeaturesNumber:
        print('There are more features')
    return features
