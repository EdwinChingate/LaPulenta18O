from SpectraSpectrum import *
import gc
def JoinSpectra(DataSet,min_mz=200,max_mz=300,minInt=1e2,ML=1,MinDif=2.0038,MaxDif=2.0046,min_RT=0,max_RT=100):
    FirstSpectrum=True
    c=0
    JoinedSpectra=[]
    for spectrum in DataSet:
        MSLevel=spectrum.getMSLevel()
        RT=spectrum.getRT()/60 #RT in minutes 
        JoinedSpectra=SpectraSpectrum(MSLevel,RT,min_RT,max_RT,ML,c,min_mz,max_mz,minInt,JoinedSpectra,spectrum)
        del RT        
        del MSLevel
        c+=1
    del c    
    del FirstSpectrum   
    gc.collect()
    return JoinedSpectra 
