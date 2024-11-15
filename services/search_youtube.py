import innertube

client = innertube.InnerTube("WEB")

def search_youtube(query):
  data = client.search(query=f'{query} lyrics')
  print(data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'])
  return data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']