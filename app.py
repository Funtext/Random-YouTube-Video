from googleapiclient.discovery import build
from flask import Flask, Response, request, render_template
from flask_cors import cross_origin
import random
app = Flask(__name__)
DEVELOPER_KEY = 'DEVELOPER_KEY'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
prefix = ['IMG ', 'IMG_', 'IMG-', 'DSC ']
postfix = [' MOV', '.MOV', ' .MOV']

@app.route('/')
@cross_origin()
def _index():
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
  search_response = youtube.search().list(q=random.choice(prefix) + str(random.randint(999, 9999)) + random.choice(postfix),part='snippet',maxResults=5).execute()
  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      return Response(search_result['id']['videoId'])

@app.route('/ok')
@cross_origin()
def _ok():
  return Response("server ok")
