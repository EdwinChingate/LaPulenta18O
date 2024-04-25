import numpy as np
def JoiningSpectrum(DifTable,RT,JoinedSpectra,c):
    global FirstSpectrum
    LDifTable=len(DifTable)            
    DifTable=np.c_[DifTable,RT*np.ones(LDifTable)]
    DifTable=np.c_[DifTable,c*np.ones(LDifTable)]            
    if LDifTable>0:
        if FirstSpectrum:
            JoinedSpectra=DifTable.copy()
            FirstSpectrum=False                    
        else:
            JoinedSpectra=np.append(JoinedSpectra,DifTable,axis=0)
    del LDifTable
    return JoinedSpectra
