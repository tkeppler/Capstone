# Author: Taylor Keppler
# Critique Recommender
# file will be used to, given a track and a tag, return tracks similar to the track, 
# similar to that track but more *tag*, and similar to that track but less *tag*

# currently these functions work less than ideally. Asking for more or less *tag*
# often returns similar songs. To fix this we would create a better metric of adding
# or subtracting tag values resulting in a more effective critique.

import trim2 
import calcSimilarity
import ChosenTags as CT
import get_metadata as getMB

songDict = trim2.makeGenomes()

def initialSims(tid):
    # returns original top 5 similar songs for a given track
    baseGenome = songDict[tid]
    return calcSimilarity.allCorrelations(baseGenome)

def critiqueTagMore(baseDict, tag):
    #given a tag, return songs that are similar to inputed tag vector, but more *tag*    
    newBase = baseDict
    if not baseDict.has_key(tag):
        newBase[tag] = 15
    else:
        newBase[tag] += 15
    return calcSimilarity.allCorrelations(newBase)

def critiqueTagLess(baseDict, tag):
    #given a tag, return songs that are similar to inputed tag vector, but less *tag*
    newBase = baseDict
    if not baseDict.has_key(tag):
        newBase[tag] = 0
    else:
        newBase[tag] -=15
    return calcSimilarity.allCorrelations(newBase)
        

    
    


# ------------ tests ------------------------- 
#initial = initialSims('TRMUSHP12903D09451')
#print "initial similarity: ", initial
#thisDict = songDict['TRMUSHP12903D09451']
#result = critiqueTagMore(thisDict, 'LOVE')
#print "new similarities: "
#for thing in result:
#    print thing, songDict[thing], getMB.getMetadata(thing)
#print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#result2 = critiqueTagLess(thisDict, 'LOVE')
#for thing in result2:
#    print thing, songDict[thing], getMB.getMetadata(thing)
