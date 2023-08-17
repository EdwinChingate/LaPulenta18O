from ClusterStats import *
import pandas as pd
def RawKernel(SignalsMat,KernelIDs,alpha=0.01):    
    Kernel=[]
    counter=0
    for cent in KernelIDs:
        Kernel.append(SignalsStats(SignalsMat[cent,:],Isotopomer=0,alpha=alpha))        
        counter+=1
    KernelArray=np.array(Kernel)
    return KernelArray
