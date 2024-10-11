import numpy as np
import gc
def mz_Diference(SignalsMat):#With filters for mz and RT
    NumberofCandidates=len(SignalsMat)
    Difmz=np.zeros([NumberofCandidates,NumberofCandidates])
    FirstCandidate=True
    for candidatePos in np.arange(NumberofCandidates):
        mz_candidate=SignalsMat[candidatePos,0]
        mz_Dif=abs(mz_candidate-SignalsMat[:,0])       
        Difmz[candidatePos,:]=mz_Dif
        del mz_Dif
        gc.collect()
    return Difmz
