from bs4 import BeautifulSoup
import requests

class SiteMapParser(object):
	"""Parses XML sitemap file to produce a list of video and songs name as per the storage directory"""
	def __init__(self):

		global vidNames, songNames

		vidNames = []
		songNames = []

		self.vidNames = vidNames
		self.songNames = songNames

		page = open('sitemap.xml', 'r')

		sitemap_index = BeautifulSoup(page, 'html.parser')

		urls = [element.text for element in sitemap_index.findAll('loc')]

		for url in urls:
			name = url.split('/')[-1]
			if url.endswith('mp3'):
				self.songNames.append(name)
			elif url.endswith('mp4'):
				self.vidNames.append(name)
			else:
				continue

if __name__ == '__main__':
	parse = SiteMapParser()
	print(parse.vidNames)