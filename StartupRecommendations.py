
# coding: utf-8

import trim2
import math
import scipy.spatial.distance as dis

# Purpose of this code:
# 
# Uses a user's profile with established preferences (liked songs, with details connecting to emotional tags) to suggest other songs that are most similar to the ones the user already likes. This is intended to be a supplemental recommender function, that will record all of the preferences a user demonstrates, and gives that user other songs they might like without any current user input. 
# 
# Every time a user rates a song, or requests another song that is more "happy", this portion of the code will update the user's preferences. It will record all of these preferences and try to suggest new songs that most accurately fit the user's preferences. A user's listening history will be recorded and then used to find songs that have similar tag counts. 

# In[ ]:

import json
#plans for future work and functionality
#user will have certain outputs pulled from the user file
    #file will contain each emotional tags and how many times they've liked a song with each tag
    
    #on startup, algorithm gives the top 10 songs that align with their listening habits
        #user can also ask for top 10 songs in line with their preferences within a given emotional tag
            #would be a happy song that has received the same number of happy tags as previously liked songs



#song - song object
#userSongLog - contains liked songs
#userTags - how many songs from each tag the user has liked
def recordSong(song, userSongLog, userTags):
    if song not in userSongLog:
        userSongLog.songs.append(song)
        for tag in userTags:
            userTags[tag] += 1
    return userSongLog
            
def generateTopSuggestions(tag, userSongLog):
    tagGroup = getTagCategory(tag) #returns tag group
    suggestionsDict = {}
    for song in userSongLog:
        suggestionsDict.append(song)
    your5Songs = allCorrelations(suggestionsDict)
    return your5Songs


    
    
    

