# use metadata to get track info

#example files:
#TRBSLNR128F4228FAA defaultdict(<type 'float'>, {'RELAXING': 100.0})
#TRPYHPC128F930F9B0 defaultdict(<type 'float'>, {'RELAXING': 33.0})
#TRUNRIQ128F92FEB73 defaultdict(<type 'float'>, {'RELAXING': 26.0})
#TRULSUT128F425E4EA defaultdict(<type 'float'>, {'MOODY': 100.0})
#TRMUSHP12903D09451 defaultdict(<type 'float'>, {'HAPPY': 15.0, 'LOVE': 2.0, 'RELAXING': 11.0, 'SAD': 2.0})
#TROPSUR128E0789916 defaultdict(<type 'float'>, {'LOVE': 4.0})

import sqlite3
import trim2 
import ChosenTags as CT

#tidList = ['TRBSLNR128F4228FAA', 'TRPYHPC128F930F9B0', 'TRULSUT128F425E4EA', 'TRMUSHP12903D09451', 'TROPSUR128E0789916']

def getMetadata(tid):
    dbFile = 'track_metadata.db'
    conn = sqlite3.connect(dbFile)
    
    sql = "SELECT title, artist_name FROM songs WHERE track_id = '%s'" % tid
    res = conn.execute(sql)
    metadata = res.fetchone()
    print "tid: ", tid, "metadata: ", metadata
    conn.close()
    return metadata
    
#for tid in tidList:
#    getMetadata(tid)