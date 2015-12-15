# file to retrieve desired songs from the sqlite database
# using chosen tags file

# after trim is run there are 104,049 unique songs in our data set


# author: Taylor Keppler, except as noted

import os
import sys
import sqlite3
import ChosenTags as CT
import collections

allTags = CT.getAllTags()

def sanitize(tag):
    """
    sanitize a tag so it can be included or queried in the db

    author: Thierry Bertin-Mahieux (2011) Columbia University tb2332@columbia.edu
    """
    tag = tag.replace("'","''")
    return tag

def getSongsWithTag(tag, connection):
    # sql request to get all tracks with a given tag
    sql = "SELECT tids.tid FROM tags, tid_tag, tids WHERE tags.ROWID = tid_tag.tag AND tids.ROWID = tid_tag.tid and tags.tag = '%s'" % sanitize(tag)
    res = connection.execute(sql)
    tracks = res.fetchall()
    for track in tracks:
        yield track[0]

def getTagValue(track_id, tag, connection):
    # for a given track and tag, returns the value of the tag for that track
    sql = "SELECT tid_tag.val FROM tid_tag, tids, tags WHERE tags.ROWID = tid_tag.tag AND tid_tag.tid = tids.ROWID AND tids.tid = '%(tid)s' AND tags.tag = '%(tag)s'" % {"tid": track_id, "tag": sanitize(tag)} 
    res = connection.execute(sql)
    val = res.fetchone()
    if val is None:
        return 0.0
    else:
        return val[0]


def makeGenomes():
    # returns a dictionary of songs: {tags: values} aka dictionary of all tag genomes
    allSongs = {}
    
    dbfile = "lastfm_tags.db"
    conn = sqlite3.connect(dbfile)
    for tag in CT.getAllTags():
        for song in getSongsWithTag(tag, conn):
            val = getTagValue(song, tag, conn)
            category = CT.getTagCategory(tag)
            if song in allSongs:
                allSongs[song][category] += val
            else:
                allSongs[song] = collections.defaultdict(float)
                allSongs[song][category] = val

    conn.close()
    return allSongs
