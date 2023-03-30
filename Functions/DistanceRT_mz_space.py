import numpy as np
def DistanceRT_mz_space(SignalsMat):
    NumberofCandidates=len(SignalsMat)
    DifMat=np.zeros([NumberofCandidates,NumberofCandidates])
    FirstCandidate=True
    for candidatePos in np.arange(NumberofCandidates):
        mz_candidate=SignalsMat[candidatePos,0]
        mz_Dif=(mz_candidate-SignalsMat[:,0])**2
        RT_candidate=SignalsMat[candidatePos,5]
        RT_Dif=(RT_candidate-SignalsMat[:,5])**2
        Dif=RT_Dif+mz_Dif
        DifMat[candidatePos,:]=Dif
        #if FirstCandidate:
       #     DifMat=Dif
       #     FirstCandidate=False
       # else:
        #    DifMat=np.append(DifMat,Dif,axis=0)
    return DifMat
#Normalize! Very important!!!!!!!!
#add weight for the diference
