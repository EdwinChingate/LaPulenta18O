from NeoPower import *
import numpy as np
import gc
def JoinSpectra(DataSet,min_mz=200,max_mz=300,minInt=1e2,ML=1,MinDif=2.0038,MaxDif=2.0046,min_RT=0,max_RT=100):
    FirstSpectrum=True
    c=0
    SignalsMat=[]
    for spectrum in DataSet:
        MSLevel=spectrum.getMSLevel()
        RT=spectrum.getRT()/60 #RT in minutes 
        if ((MSLevel==ML)&(RT>min_RT)&(RT<max_RT)): #Checking the MSLevel for the analysis
            RawSpectrum=np.array(spectrum.get_peaks()).T
            SpectrumFilter=np.where((RawSpectrum[:,0]>min_mz)&(RawSpectrum[:,0]<max_mz)&(RawSpectrum[:,1]>minInt))[0]
            SpectrumFil=RawSpectrum[SpectrumFilter,:]
            DifTable=NeoPower(SpectrumFil,MinDif=MinDif,MaxDif=MaxDif)
            LDifTable=len(DifTable)            
            DifTable=np.c_[DifTable,RT*np.ones(LDifTable)]
            DifTable=np.c_[DifTable,c*np.ones(LDifTable)]            
            del RT
            if LDifTable>0:
                if FirstSpectrum:
                    SignalsMat=DifTable.copy()
                    FirstSpectrum=False                    
                else:
                    SignalsMat=np.append(SignalsMat,DifTable,axis=0)
            del RawSpectrum
            del SpectrumFil
            del DifTable
            del LDifTable
            gc.collect()
        del MSLevel
        c+=1
    del c    
    return SignalsMat
