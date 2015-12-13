
# coding: utf-8

# In[1]:

LOVE = ['Love', 'romantic', 'love songs', 'love song', 'lovesongs', 'romance', 'lovesong', 'amor']

PRETTY = ['beautiful', 'pretty']

RELAXING = ['chillout', 'chill', 'chill out', 'chilled', 'chill-out', 'chillax', 'relaxed', 'relaxing', 'peaceful', 'Relaxed', 'calm', 'calming']

SAD = ['sad', 'sad song', 'sadness', 'melancholy', 'melancholic', 'depressing']

HAPPY = ['happy', 'feel good', 'feelgood', 'makes me happy', 'good mood', 'cheerful', 'feel good music', 'joyful', 'uplifting']

DREAMY = ['dreamy', 'dream']

NOSTALGIC = ['nostalgia', 'nostalgic', 'sentimental']

MOODY = ['emotional', 'moody', 'emotive', 'mood music']

ANGRY = ['angry']

BREAKUP = ['breakup']

MIS = ['mellow', 'sexy', 'dark', 'bittersweet']

allCategories = [(LOVE, 'LOVE'), (PRETTY, 'PRETTY'), (RELAXING, 'RELAXING'),
                 (SAD, 'SAD'), (HAPPY, 'HAPPY'), (DREAMY, 'DREAMY'), 
                 (NOSTALGIC, 'NOSTALGIC'), (MOODY, 'MOODY'), (ANGRY, 'ANGRY'),
                 (BREAKUP, 'BREAKUP')]

def getAllTags():
    allTags = []
    for catTuple in allCategories:
        for tag in catTuple[0]:
            allTags.append(tag)
    return allTags

def getDictAllTags():
    allTags = {}
    for catTuple in allCategories:
        #print catTuple
        catLabel = catTuple[1]
        allTags[catLabel] = []
        for tag in catTuple[0]:
            allTags[catLabel].append(tag)
    return allTags
                

def getTagCategory(tag):
    # want just category name as string
    # there is probs a more efficient way f doing this?
    for catTuple in allCategories:
        if tag in catTuple[0]:
            return catTuple[1]
        
########## tests ########

# getAllTags()
# buildDict()
#print getTagCategory('happy')
#print getTagCategory('dreamy')

# In[ ]:



