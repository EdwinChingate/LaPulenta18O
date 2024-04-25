from SpectraSpectrum import *
import gc
def JoinSpectra(DataSet,Parameters,JoinedSpectra):
    FirstSpectrum=True
    c=0
    for spectrum in DataSet:
        MSLevel=spectrum.getMSLevel()
        RT=spectrum.getRT()/60 #RT in minutes 
        JoinedSpectra=SpectraSpectrum(MSLevel,RT,Parameters,c,JoinedSpectra,spectrum)
        del RT        
        del MSLevel
        c+=1
    del c    
    del FirstSpectrum   
    gc.collect()
    return JoinedSpectra 
