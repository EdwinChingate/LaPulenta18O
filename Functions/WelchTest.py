from scipy.stats import t
from scipy import stats
import numpy as np
def WelchTest(SignalsStats1,SignalsStats2,alpha=0.05): 
    #Statistical test to check if two fragments are different
    #SignalsStats1 and SignalsStats2 are vectors that summarize the information on the samples [average,std,size]
    if sum(SignalsStats1)==0:
        return [0]*7
    stError1=SignalsStats1[3]/np.sqrt(SignalsStats1[4])
    stError2=SignalsStats2[3]/np.sqrt(SignalsStats2[4])
    stMix=np.sqrt(stError1**2+stError2**2)
    #t=abs(SignalsStats1[2]-SignalsStats2[2])/np.sqrt(stError1**2+stError2**2)
    FreedomDegrees=(SignalsStats1[3]**2/SignalsStats1[4]+SignalsStats2[3]**2/SignalsStats2[4])**2/(SignalsStats1[3]**4/((SignalsStats1[4]-1)*SignalsStats1[4]**2)+SignalsStats2[3]**4/((SignalsStats2[4]-1)*SignalsStats2[4]**2))
    tref=stats.t.interval(1-alpha, FreedomDegrees)[1]
  #  pValue=0 #I need to include the calculation of the p-value
    mz_Dif=abs(SignalsStats1[2]-SignalsStats2[2])
    ConfidenceIntervalDif=tref*stMix
    ConfidenceIntervalDifPPM_Dif=ConfidenceIntervalDif*1e6/mz_Dif
    ConfidenceIntervalDifPPM_mz1=ConfidenceIntervalDif*1e6/SignalsStats1[2]
    ConfidenceIntervalDifPPM_mz2=ConfidenceIntervalDif*1e6/SignalsStats2[2]
    WelchVec=[mz_Dif,ConfidenceIntervalDif,ConfidenceIntervalDifPPM_Dif,ConfidenceIntervalDifPPM_mz1,ConfidenceIntervalDifPPM_mz2,tref, stMix]
    return WelchVec
