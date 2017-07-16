import os
import requests
from sitemapParser import SiteMapParser

from bs4 import BeautifulSoup
from flask import Flask, request, render_template
from flask_restful import Resource, Api

"""
Transfer framework from Flask to Django
"""

filesLocation = "https://tricentennial-compo.000webhostapp.com/media/"
songsLocation = filesLocation + "music/"
videosLocation = filesLocation + "videos/"

app = Flask(__name__)
api = Api(app)

parserObj = SiteMapParser()
songs = parserObj.songNames
vids = parserObj.vidNames

class mediaApi(Resource):
	def get(self, query):
		queryToFilename = query + ".mp4"
		if (queryToFilename in vids):
			return { "query" : query,
			"filename": queryToFilename,
			"address": videosLocation + queryToFilename}
		else:
			return {"Error 404": "No file related to query was found. Try a different keyword."}

api.add_resource(mediaApi, '/query/<string:query>')

songsAmount = len(songs)
videos = vids
vidsAmount = len(videos)

@app.route('/')
@app.route('/home')
def index():
	return render_template("index.html",
	 						title = "Home",
	 						songsAmount = songsAmount,
	 						songs = songs,
	 						vidsAmount = vidsAmount,
	 						videos = videos,
	 						songsLocation = songsLocation,
	 						videosLocation = videosLocation)

@app.route('/videos')
def videoList():
	return render_template("videos.html",
							title = "Videos",
							vidsAmount = vidsAmount,
	 						videos = videos,
							videosLocation = videosLocation)

@app.route('/songs')
def songList():
	return render_template("songs.html",
							title = "Songs",
							songsAmount = songsAmount,
	 						songs = songs,
							songsLocation = songsLocation)

@app.route('/video/<filename>')
def video(filename):
	return render_template("vidplayer.html",
							title = "Playing " + filename,
							video = filename,
							loc = filesLocation)

@app.route('/song/<filename>')
def song(filename):
	return render_template("songplayer.html",
							title = "Playing " + filename,
							song = filename,
							loc = filesLocation)
		
app.run(host = "0.0.0.0", debug = True)	