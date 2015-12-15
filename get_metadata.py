# author: Taylor Keppler
# use metadata database to get track title, and artist

import sqlite3

def getMetadata(tid):
    dbFile = 'track_metadata.db'
    conn = sqlite3.connect(dbFile)
    
    sql = "SELECT title, artist_name FROM songs WHERE track_id = '%s'" % tid
    res = conn.execute(sql)
    metadata = res.fetchone()
    #print "tid: ", tid, "metadata: ", metadata
    conn.close()
    return metadata
