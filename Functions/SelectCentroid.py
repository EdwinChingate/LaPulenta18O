import numpy as np
def SelectCentroid(DistanceMat):
    MinDist=np.min(DistanceMat[:,2])
    MinDistLoc=np.where(DistanceMat[:,2]==MinDist)[0]
    centroid=DistanceMat[MinDistLoc,3]
    return centroid
