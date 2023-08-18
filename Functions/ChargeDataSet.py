import os
from pyopenms import *
def ChargeDataSet(DataSetName,OSLinux=True):
    if OSLinux:
    	ConnectorSym='/'
    else:
    	ConnectorSym='\\'      
    home=os.getcwd()
    path=home+ConnectorSym+'Data'
    DataSet=MSExperiment()
    MzMLFile().load(path+ConnectorSym+DataSetName, DataSet)
    return DataSet
