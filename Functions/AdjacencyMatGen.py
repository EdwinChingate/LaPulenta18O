import numpy as np
from DistanceRT_mz_space import *
from SelectNeightbors import *
def AdjacencyMatGen(SignalsMat,MinNumberCandidatesClustering=5):
    DifMat=DistanceRT_mz_space(SignalsMat)
    NumberofCandidates=len(DifMat)
    AdjacencyMatrix=np.zeros([NumberofCandidates,NumberofCandidates])
    for candidatePos in np.arange(NumberofCandidates):
        CandidateRow=DifMat[candidatePos,:]
        NeightborsSelected=SelectNeightbors(CandidateRow,MinNumberCandidatesClustering=MinNumberCandidatesClustering)
        NeightborsSelected[candidatePos]=0
        AdjacencyMatrix[candidatePos,:]=NeightborsSelected
    return AdjacencyMatrix
