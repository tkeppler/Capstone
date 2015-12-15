Authors: Taylor Keppler and Blaise Yokoyama

This project contains files for a Emotional Music Recommender. This was built for our Collective Intelligence final project. There are two parts to the project: general recommendations for a user and critique recommendations for a single song.

The critique recommendation file can be found in critiqueRec.py. Currently the critiqueTagMore and critiqueTagLess functions take inputs of a tag:val dictionary and the tag to be critiqued and return the top 5 similar songs in the respective directions.

Will need both the lastfm_tags database and the track_metadata SQLite databases from the million songs dataset to run this code.

Database source:

Thierry Bertin-Mahieux, Daniel P.W. Ellis, Brian Whitman, and Paul Lamere. 
The Million Song Dataset. In Proceedings of the 12th International Society
for Music Information Retrieval Conference (ISMIR 2011), 2011.

Last.fm dataset, the official song tags and song similarity collection for the Million Song
Dataset, available at: http://labrosa.ee.columbia.edu/millionsong/lastfm


