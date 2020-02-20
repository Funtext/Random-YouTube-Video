from googleapiclient.discovery import build
from flask import Flask, Response, request, render_template
from flask_cors import cross_origin
import random
app = Flask(__name__)
DEVELOPER_KEY = 'AIzaSyA-FE1NvE8-0uiGhjlQnXD0DnjrO8CyEBE'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
prefix = ['IMG ', 'IMG_', 'IMG-', 'DSC ']
postfix = [' MOV', '.MOV', ' .MOV']

@app.route('/')
@cross_origin()
def _index():
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
  search_response = youtube.search().list(q=random.choice(prefix) + str(random.randint(999, 9999)) + random.choice(postfix),part='snippet',maxResults=5).execute()
  videos = []
  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      videos.append('%s' % (search_result['id']['videoId']))
      return Response(videos[random.randint(0, 2)]))
