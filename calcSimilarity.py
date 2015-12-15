# function to find the similarity between one track 
# and all other tracks, returns top 5 tracks

# uses scipy correlation() function to calculate similarity

# author: Taylor Keppler

import trim2
import math
import scipy.spatial.distance as dis

allSongsDict = trim2.makeGenomes()

def getSimilarity(baseDict, tidDict):
    # generates vectors for two tracks to be used in similarity function
    #returns similarity between base vector and track vector    
    
    baseVector = []
    tidVector = []
    
    if len(baseDict) >= len(tidDict) :
        for (k,v) in baseDict.iteritems():
            baseVector.append(v)
            if k in tidDict:
                tidVector.append(tidDict[k])
            else:
                tidVector.append(0)
    else:
        for (k,v) in tidDict.iteritems():
            tidVector.append(v)
            if k in baseDict:
                baseVector.append(baseDict[k])
            else:
                baseVector.append(0)
    
    return dis.correlation(baseVector, tidVector)
 


def allCorrelations(baseDict):
    # returns top 5 similar songs to the inputed vector
    allSimilarities = {}
    for (k,v) in allSongsDict.iteritems():
        sim = getSimilarity(baseDict, v)
        allSimilarities[k] = sim
    sortedSimilarities = sorted(allSimilarities, key = allSimilarities.get)
    
    return sortedSimilarities[:5]
