import numpy as np
def JoiningSpectrum(DifTable,RT,SignalsMat,c):
    global FirstSpectrum
    LDifTable=len(DifTable)            
    DifTable=np.c_[DifTable,RT*np.ones(LDifTable)]
    DifTable=np.c_[DifTable,c*np.ones(LDifTable)]            
    if LDifTable>0:
        if FirstSpectrum:
            SignalsMat=DifTable.copy()
            FirstSpectrum=False                    
        else:
            SignalsMat=np.append(SignalsMat,DifTable,axis=0)
    del LDifTable
    return SignalsMat
