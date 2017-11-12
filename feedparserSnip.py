import feedparser
import functools

python_wiki_rss_url = "http://feeds.feedburner.com/Coindesk?format=xml"
feed = feedparser.parse( python_wiki_rss_url )
print(feed)

#print(feed['entries'][0]['title'])
#print(feed['entries'][0]['links'][0]['href'])

linkLst = []
for i in range(3):
    linkLst.append("<a href="+feed['entries'][i]['links'][0]['href']+">'"+feed['entries'][i]['title']+"'</a>")
print(linkLst)