import innertube

client = innertube.InnerTube("WEB")

def search_youtube(query):
  data = client.search(query=f'{query} lyrics 가사')
  print(data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'])
  return data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']

def player_youtube(query):
  data = client.player(query)
  return data['playabilityStatus']['status']