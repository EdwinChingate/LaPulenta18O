from EmptyModules import *
from DistanceKernel import *
from Pre_SelectCentroid import *
from SelectCentroid import *
import gc 
def ModulesK_Nearst(SignalsMat,Kernel,SafetyFactor=4):
    signalID=0
    Modules=EmptyModules(len(Kernel[:,0]))
    for Signal in SignalsMat:
        DistanceMat=DistanceKernel(Signal,Kernel)
        pre_Centroid=Pre_SelectCentroid(DistanceMat,Kernel,SafetyFactor=SafetyFactor)
        if len(pre_Centroid)>0:
            ID=int(SelectCentroid(DistanceMat[pre_Centroid,:]))
        else:
            ID=-1
        Modules[ID].append(signalID)
        signalID+=1
        del DistanceMat
        del pre_Centroid
        gc.collect()
    return Modules
