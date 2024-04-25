from NeoPower import *
from JoiningSpectrum import *
import numpy as np
import gc
def SpectraSpectrum(MSLevel,RT,Parameters,c,JoinedSpectra,spectrum):
    min_RT=Parameters[]
    max_RT=Parameters[]
    ML=Parameters[]    
    MSLevelCondition=MSLevel==ML
    min_RTCondition=RT>min_RT
    max_RTCondition=RT<max_RT
    SpectFilter=(MSLevelCondition)&(min_RTCondition)&(max_RTCondition)
    if (SpectFilter): #Checking the MSLevel for the analysis
        RawSpectrum=np.array(spectrum.get_peaks()).T
        min_mz=Parameters[]
        max_mz=Parameters[]
        minInt=Parameters[]
        min_mzCondition=RawSpectrum[:,0]>min_mz
        max_mzCondition=RawSpectrum[:,0]<max_mz
        minIntCondition=RawSpectrum[:,1]>minInt
        SpectrumCondition=(min_mzCondition)&(max_mzCondition)&(minIntCondition)
        SpectrumFil=RawSpectrum[SpectrumCondition,:]
        DifTable=NeoPower(SpectrumFil,MinDif=MinDif,MaxDif=MaxDif)        
        JoinedSpectra=JoiningSpectrum(DifTable,RT,JoinedSpectra,c)
        del RawSpectrum
        del SpectrumFil
        del DifTable
        gc.collect()
    return JoinedSpectra
