from google.appengine.api import urlfetch
from google.appengine.ext import db
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils import simplejson



from xml.dom import minidom 

from models import Song, Playlist
from forms import PlaylistForm, SongForm


def getText(nodelist):
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data
    return rc

def index(request):
	return render_to_response('index.html')

def create(request):
	if request.method == 'POST':
		url = request.POST.get('playlist_location', '')
		#
		#regexp here!!!!!!!!!
		#
		result = urlfetch.fetch(url + "code/xspf.php")

		if result.status_code == 200:
			xml = minidom.parseString(result.content)
			tracks = xml.getElementsByTagName('track')
			playlist = Playlist(title="lorem ipsum dolor", location=url)
			playlist.save()

			for song in tracks:
				loc = song.getElementsByTagName('location')[0]
				me = song.getElementsByTagName('meta')[0]
				ti = song.getElementsByTagName('title')[0]
				fo = song.getElementsByTagName('info')[0]

				s = SongForm({
					'location': getText(loc.childNodes),
					'meta': getText(me.childNodes),
					'title': getText(ti.childNodes),
					'info': getText(fo.childNodes),
				})
				if s.is_valid():
					s.playlist = playlist
					s.save()

			return render_to_response('create.html', {'flash' : "OK!!!"})

	return render_to_response('create.html')

def search(request, keyword=""):
	return render_to_response('search.html', { 'keyword': keyword })

#########
#
# API
#
#########

def query(request):
	key = request.GET.get('song', '')
	query = Song.all().search(key).fetch(limit=10)
	songs = []
	for s in query:
		songs.append({
			'title' : s.title,
			'location' : s.location,
			'info' : s.info
		})

	enc = simplejson.JSONEncoder()
	data = enc.encode(songs)
	return HttpResponse(data)

def ping(request):
	return HttpResponse("<thanks />")