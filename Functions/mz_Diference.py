import numpy as np
def mz_Diference(SignalsMat):#With filters for mz and RT
    NumberofCandidates=len(SignalsMat)
    DifMat=np.zeros([NumberofCandidates,NumberofCandidates])
    FirstCandidate=True
    for candidatePos in np.arange(NumberofCandidates):
        mz_candidate=SignalsMat[candidatePos,0]
        mz_Dif=abs(mz_candidate-SignalsMat[:,0])       
        DifMat[candidatePos,:]=mz_Dif
        #if FirstCandidate:
       #     DifMat=Dif
       #     FirstCandidate=False
       # else:
        #    DifMat=np.append(DifMat,Dif,axis=0)
    return DifMat
