# chosen tags for emotional music recommender
# authors: Taylor Keppler and Blais Yokoyama

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
    # returns list of all tags we're using for the recommender
    allTags = []
    for catTuple in allCategories:
        for tag in catTuple[0]:
            allTags.append(tag)
    return allTags

def getDictAllTags():
    # returns dictionary of all tag categories: list of tags
    allTags = {}
    for catTuple in allCategories:
        catLabel = catTuple[1]
        allTags[catLabel] = []
        for tag in catTuple[0]:
            allTags[catLabel].append(tag)
    return allTags
                

def getTagCategory(tag):
    # returns tag category for an inputed tag
    for catTuple in allCategories:
        if tag in catTuple[0]:
            return catTuple[1]
