import numpy as np
#sys.setrecursionlimit(100000000) This is a recursive function, you may have some errors from python, as it predefines a maximum number of iterations
def ModulesDet(AdjacencyMatrix,p=0,Mod=0,ModList=[],start=True): #Search for modules inside the AdjacencyMatrix
    #Hashtag
    #print(type(Mod))
    #print('Here',p)
    if type(Mod)==type(int(0)):
        Mod=[]
    NumberofCandidates=len(AdjacencyMatrix)     
    CandidateVec=AdjacencyMatrix[p,:]
    NeighborLoc=np.where(CandidateVec==1)[0]
   # print(len(NeighborLoc))    
    AdjacencyMatrix[p,:]=0
    AdjacencyMatrix[:,p]=0
    for neighbor in NeighborLoc:
       # AdjacencyMatrix[:,neighbor]=0
       # AdjacencyMatrix[neighbor,:]=0
     #   print(p,neighbor)
        Mod.append(neighbor)
        ModList=ModulesDet(AdjacencyMatrix,p=neighbor,Mod=Mod,ModList=ModList,start=False)
    if start and p<NumberofCandidates-1:
       # print(Mod,p)
        if len(Mod)>0:
            Mod.append(p)
            ModList.append(Mod)
        ModList=ModulesDet(AdjacencyMatrix,p=p+1,Mod=[],ModList=ModList,start=True)
    return ModList
