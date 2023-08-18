from O2Omachine import *
from ChargeDataSet import *
from JoinSpectra import *
import gc
import os
def O2OData(Folder='Data',min_mz=80,max_mz=1000,minInt=1e4,MinSignalsSpectra=10,ML=1,MinDif=2.0038,MaxDif=2.0046,min_RT=0,max_RT=100,max_mz_Tol=5e-3,max_RT_Tol=0.3,FeaturesNumber=500,MinSignals=3,MinIntKernel=5e4,alpha=0.01,MaxDeep=3,SafetyFactor=4,TheoricalDif=2.0042449932959006,MinNumberCandidatesClustering=3):
    home=os.getcwd()
    DataFolder=home+'/'+Folder #Also consider OS
    for DataSetName in os.listdir(DataFolder):
        print(DataSetName)
        DataSet=ChargeDataSet(DataSetName=DataSetName) #Add flexibility in the folder
        SignalsMat=JoinSpectra(DataSet=DataSet,min_mz=min_mz,max_mz=max_mz,minInt=minInt,ML=ML,MinDif=MinDif,MaxDif=MaxDif,min_RT=min_RT,max_RT=max_RT)
        DataSet.reset()
        if len(SignalsMat)>MinSignalsSpectra:
            O2Omachine(DataSetName=DataSetName,SignalsMat=SignalsMat,min_mz=min_mz,max_mz=max_mz,minInt=minInt,MinSignalsSpectra=MinSignalsSpectra,MinSignals=MinSignals,ML=ML,MinDif=MinDif,MaxDif=MaxDif,min_RT=min_RT,max_RT=max_RT,max_mz_Tol=max_mz_Tol,max_RT_Tol=max_RT_Tol,FeaturesNumber=FeaturesNumber,MinIntKernel=MinIntKernel,alpha=alpha,MaxDeep=MaxDeep,SafetyFactor=SafetyFactor,TheoricalDif=TheoricalDif,MinNumberCandidatesClustering=MinNumberCandidatesClustering)  
        del SignalsMat
        gc.collect()      
