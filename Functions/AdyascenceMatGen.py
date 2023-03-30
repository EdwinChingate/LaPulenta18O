import numpy as np
from DistanceRT_mz_space import *
from SelectNeightbors import *
def AdyascenceMatGen(SignalsMat):
    DifMat=DistanceRT_mz_space(SignalsMat)
    NumberofCandidates=len(DifMat)
    AdyascenceMatrix=np.zeros([NumberofCandidates,NumberofCandidates])
    for candidatePos in np.arange(NumberofCandidates):
        CandidateRow=DifMat[candidatePos,:]
        NeightborsSelected=SelectNeightbors(CandidateRow)
        AdyascenceMatrix[candidatePos,:]=NeightborsSelected
    return AdyascenceMatrix
