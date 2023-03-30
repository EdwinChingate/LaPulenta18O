import numpy as np
#Add filter for minimum distances
def SelectNeightbors(CandidateRow,MinNumberCandidatesClustering=5):
    MinListLoc=np.argsort(CandidateRow)[:MinNumberCandidatesClustering]
    NumberofCandidates=len(CandidateRow)
    NeightborsSelected=np.zeros(NumberofCandidates)
    NeightborsSelected[MinListLoc]=1
    return NeightborsSelected
