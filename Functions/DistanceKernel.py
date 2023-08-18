import numpy as np
import gc
def DistanceKernel(Signal,Kernel):
    D_RT=np.abs(Signal[7]-Kernel[:,0])
    D_mz=np.abs(Signal[0]-Kernel[:,2])
    DistanceVec=D_RT/Signal[7]+D_mz/Signal[0]
    DistanceMat=np.c_[D_RT,D_mz,DistanceVec,np.arange(len(Kernel[:,0]))]
    del D_RT
    del D_mz
    del DistanceVec
    gc.collect()
    return DistanceMat
