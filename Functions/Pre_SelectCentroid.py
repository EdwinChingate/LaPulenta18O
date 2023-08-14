import numpy as np
def Pre_SelectCentroid(DistanceMat,Kernel,SafetyFactor=4):
    pre_Centroid=[]
    for centID in np.arange(len(DistanceMat[:,0])):
        if DistanceMat[centID,0]<SafetyFactor*Kernel[centID,1] and DistanceMat[centID,1]<SafetyFactor*Kernel[centID,5]: 
            pre_Centroid.append(centID)
    return pre_Centroid
