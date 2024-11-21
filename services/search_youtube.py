import innertube

client = innertube.InnerTube("WEB")

def search_youtube(query):
  data = client.search(query=f'{query} lyrics 가사')
  filterdData = data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']
  onlyVideo = [obj for obj in filterdData if obj.get('videoRenderer') is not None]
  videoIds = [onlyVideo[0]['videoRenderer']['videoId'], onlyVideo[1]['videoRenderer']['videoId'], onlyVideo[2]['videoRenderer']['videoId']]
  return videoIds