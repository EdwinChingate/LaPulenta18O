import numpy as np

def NeoPower(DataFiltered,MinDif=2.003,MaxDif=2.005):
    L=len(DataFiltered)
    DifList=[]
    for mz1_id in np.arange(L):
        mz1=DataFiltered[mz1_id,0]        
        for mz2_id in np.arange(mz1_id,L-1):
            mz2=DataFiltered[mz2_id,0]
            if abs(mz2-mz1)>MinDif and abs(mz2-mz1)<MaxDif:
                Intensity_mz1=DataFiltered[mz1_id,1]
                Intensity_mz2=DataFiltered[mz2_id,1]
                DifList.append([mz1,mz2,mz1_id,mz2_id,abs(mz2-mz1),Intensity_mz1,Intensity_mz2])
    return np.array(DifList)
#One of the loops can dissapear by replacing with the np.where() function
#Avoid repetitions with min and max
