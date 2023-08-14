import numpy as np
def EmptyModules(ModulesNumber):
    Modules=[]
    for mod in np.arange(ModulesNumber+1):
        Modules.append([])
    return Modules
