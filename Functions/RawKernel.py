from Signals_Stats import *
import pandas as pd
def RawKernel(SignalsMat,KernelIDs,alpha=0.01):    
    Kernel=[]
    counter=0
    for cent in KernelIDs:
        SignalsStats=Signals_Stats(SignalsMat[cent,:],Isotopomer=0,alpha=alpha)
        Kernel.append(SignalsStats)        
        counter+=1
    Kernel=np.array(Kernel)
    return Kernel
