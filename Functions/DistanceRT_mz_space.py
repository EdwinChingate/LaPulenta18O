import numpy as np
def DistanceRT_mz_space(SignalsMat,min_mz_Tol=1e-2,min_RT_Tol=0.3,Penalize=1e8):#With filters for mz and RT
    NumberofCandidates=len(SignalsMat)
    DifMat=np.zeros([NumberofCandidates,NumberofCandidates])
    FirstCandidate=True
    for candidatePos in np.arange(NumberofCandidates):
        mz_candidate=SignalsMat[candidatePos,0]
        mz_Dif=(mz_candidate-SignalsMat[:,0])
        mz_Dif_loc=np.where(mz_Dif>min_mz_Tol)[0]
        mz_Dif[mz_Dif_loc]=Penalize
        RT_candidate=SignalsMat[candidatePos,5]
        RT_Dif=(RT_candidate-SignalsMat[:,5])
        RT_Dif_loc=np.where(RT_Dif>min_RT_Tol)[0]
        RT_Dif[RT_Dif_loc]=Penalize
        Dif=RT_Dif**2+mz_Dif**2
        DifMat[candidatePos,:]=Dif
        #if FirstCandidate:
       #     DifMat=Dif
       #     FirstCandidate=False
       # else:
        #    DifMat=np.append(DifMat,Dif,axis=0)
    return DifMat
#Normalize! Very important!!!!!!!!
#add weight for the diference
