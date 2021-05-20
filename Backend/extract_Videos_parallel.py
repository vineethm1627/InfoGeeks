import urllib.request
import re

def extractYoutubeVideos(query, videos_results):
  temp='+'
  formatted_query = query.lower().split()
  query = temp.join(formatted_query)
  html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+query)
  video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())
  for i in video_ids:
    videos_results.append("https://www.youtube.com/watch?v="+i)
