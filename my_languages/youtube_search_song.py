# 이 파일은 Youtube DATA API 사이트를 참고하여서 이를 만들게 되었습니다. 자세한 것이 필요하신 분들은 (https://developers.google.com/youtube/v3/)를 참고해주시기 바랍니다.

# youtube 노래 검색을 위한 모듈 생성

from apiclient.discovery import build
import dotenv
# from apiclient.errors import HttpError
# from oauth2client.tools import argparser
from youtube_player import play_song

"""
Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
tab of
  https://cloud.google.com/console
Please ensure that you have enabled the YouTube Data API for your project.
"""

def youtube_search(options):
  # youtube를 위한 가상환경 생성
  youtube_config = dotenv.dotenv_values(".env")
  YOUTUBE_DEVELOPER_KEY = youtube_config['YOUTUBE_API_KEY']
  YOUTUBE_API_SERVICE_NAME = "youtube"
  YOUTUBE_API_VERSION = "v3"
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=YOUTUBE_DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  # videos = []
  videos_id = []
  # channels = []
  # channels_id = []
  # playlists = []
  # playlists_id = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      print(search_result["snippet"]["title"])
      # videos.append("%s (%s)" % (search_result["snippet"]["title"], "https://www.youtube.com/watch?v=" + search_result["id"]["videoId"]))
      videos_id.append(search_result["id"]["videoId"])
    else:
      print("원하시는 음원이 없습니다.")  
    # elif search_result["id"]["kind"] == "youtube#channel":
      # channels.append("%s (%s)" % (search_result["snippet"]["title"], "https://www.youtube.com/channel/" + search_result["id"]["channelId"]))
      # channels_id.append(search_result["id"]["channelId"])
      
    # elif search_result["id"]["kind"] == "youtube#playlist":
      # playlists.append("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["playlistId"]))
      # playlists_id.append(search_result["id"]["playlistId"])

  # print("Videos:\n", "\n".join(videos), "\n")
  for video_id in videos_id:
    play_song(video_id)
    continue_question = input("Do you want to continue? [yes or no?] ")
    if continue_question == 'yes':
      continue
    else:
      print("음원 재생을 종료합니다.")
      break
  # print("Channels:\n", "\n".join(channels), "\n")
  # print("Playlists:\n", "\n".join(playlists), "\n")
  
# if __name__ == "__main__":
#   argparser.add_argument("--q", help="Search term", default=input("원하는 키워드가 무엇입니까? : "))
#   argparser.add_argument("--max-results", help="Max results", default=25)
#   args = argparser.parse_args()

#   try:
#     youtube_search(args)
#   except HttpError as e:
#     print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))