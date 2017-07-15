#https://github.com/rakanalh/pocket-api
from pocket import Pocket, PocketException

#reads keys from text file. Line 1 is consumer key, line 2 is access token. 
with open ("apikey.txt", "r") as apikey:
    data=apikey.readlines()
    cKey=data[0]
    aToken=data[1]

#construct the API connection.
p=Pocket(consumer_key=cKey,access_token=aToken)

try:
	articles=p.retrieve(offset=0, count=20)
except PocketException as e:
	print(e.message)
	articles={}
print("%s items retrieved" % len(articles['list']))

wpm=275 #Assume 275 wpm 

for itemid,details in articles['list'].items():
	wc=None
	readtime=None
	if 'word_count' in details:
		wc=int(details['word_count'])
		readtime=int(round(wc/wpm,0))
		print("Item %s: words: %s, time: %s" % (itemid,wc,readtime))
		tag="%smin" % readtime
		print("Item %s: adding %s" % (itemid,tag))
		p.tags_add(itemid, tag).commit()

p.commit()