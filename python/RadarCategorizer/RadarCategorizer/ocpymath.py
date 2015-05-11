def getPairwiseDistances(arrx, arry, arrvar) : 
    '''
    Pairwise Distance
    each array MUST have same length.
    this method uses standard deviation on feature scaling
    '''
    devMax ,devMin = max(arrvar), min(arrvar)
    devran = devMax - devMin
    fsvar = [1 - (dev - devMin) / devran for dev in arrvar]#arrvar

    d = 0.

    param = []
    for i in range(len(fsvar)) : 
        param.append([arrx[i], arry[i], arrvar[i], fsvar[i]])
    
    for (x, y, dev, fs) in param :
        d += dev != 0 and fs * ((x - y) ** 2) / dev or 0

    return d ** 0.5

def getMatchAccuracy(arrx, arry, arrdev) : 
    '''
    each array MUST have same length.
    this method uses standard deviation on feature scaling
    '''
    
    devMax ,devMin = max(arrdev), min(arrdev)
    devran = devMax - devMin
    fsdev = [1 - (dev - devMin) / devran for dev in arrdev]#arrdev#
    
    param = []
    for i in range(len(fsdev)) : 
        param.append([arrx[i], arry[i], arrdev[i], fsdev[i]])

    d = 0.
    for (x, y, dev, fs) in param :
        d += dev != 0 and fs * ((x - y) ** 2) / dev or 0
    
    return d ** 0.5
    
