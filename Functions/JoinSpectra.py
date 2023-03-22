from NeoPower import *
import numpy as np

def JoinSpectra(DataSet,min_mz=200,max_mz=300,minInt=1e2,ML=1,MindDif=2.003,MaxDif=2.005):
    FirstSpectrum=True
    c=0
    for spectrum in DataSet:
        MSLevel=spectrum.getMSLevel()
        RT=spectrum.getRT()/60      
        if MSLevel==ML: #Checking the MSLevel for the analysis
            RawSpectrum=np.array(spectrum.get_peaks()).T
            SpectrumFilter=np.where((RawSpectrum[:,0]>min_mz)&(RawSpectrum[:,0]<max_mz)&(RawSpectrum[:,1]>minInt))[0]
            SpectrumFil=RawSpectrum[SpectrumFilter,:].copy()
            DifTable=NeoPower(SpectrumFil,MinDif=MinDif,MaxDif=MaxDif)
            LDifTable=len(DifTable)            
            DifTable=np.c_[DifTable,RT*np.ones(LDifTable)]
            DifTable=np.c_[DifTable,c*np.ones(LDifTable)]            
            if len(DifTable)>0:
                if FirstSpectrum:
                    #JoinedSpectra=SpectrumFil.copy()
                    JoinedSpectra=DifTable.copy()
                    FirstSpectrum=False
                else:
                    #JoinedSpectra=np.append(JoinedSpectra,SpectrumFil,axis=0)
                    JoinedSpectra=np.append(JoinedSpectra,DifTable,axis=0)
        c+=1
    return JoinedSpectra        
