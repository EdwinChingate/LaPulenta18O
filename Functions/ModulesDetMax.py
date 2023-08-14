import numpy as np
def ModulesDetMax(MaxID,AdjacencyMatrix,deep=0,MaxDeep=3,Module=[]):
#This is function also check for neightboors, but not more than 'MaxDeep', which is not a problem, as this function is just a first step in the clustering    
    CurrentModule=list(np.where(AdjacencyMatrix[MaxID,:]>0)[0])
    if len(CurrentModule)>0:       
        AdjacencyMatrix[np.ix_(CurrentModule,CurrentModule)]=0       
        for x in CurrentModule:
            Module.append(x)
            if deep<MaxDeep:
                Module=ModulesDetMax(MaxID=x,AdjacencyMatrix=AdjacencyMatrix,deep=deep+1,MaxDeep=MaxDeep,Module=Module)
    return Module
