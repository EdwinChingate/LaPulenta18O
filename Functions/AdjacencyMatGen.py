import numpy as np
from mz_Diference import *
from RT_Diference import *
import gc
#Replacing the clustring strategy with the minimum distance
def AdjacencyMatGen(SignalsMat,max_mz_Tol=5e-3,max_RT_Tol=0.3):
    DifRT=RT_Diference(SignalsMat)
    Difmz=mz_Diference(SignalsMat)
    NumberofCandidates=len(DifRT)
    AdjacencyMatrix=np.zeros([NumberofCandidates,NumberofCandidates])
    for candidatePos in np.arange(NumberofCandidates):
        NeighborsLoc=np.where((DifRT[candidatePos,:]<max_RT_Tol)&(Difmz[candidatePos,:]<max_mz_Tol))[0]
        AdjacencyMatrix[candidatePos,NeighborsLoc]=1
    del DifRT
    del Difmz
    gc.collect()
    return AdjacencyMatrix
