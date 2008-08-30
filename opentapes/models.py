from google.appengine.ext import db
from google.appengine.ext import search
from appengine_django.models import BaseModel


class Playlist(BaseModel):
	title = db.TextProperty(required=True)
	creator = db.StringProperty()
	info = db.StringProperty()
	location = db.StringProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)


class Song(search.SearchableModel):
	title = db.TextProperty(required=True)
	meta = db.StringProperty(required=True)
	info = db.StringProperty()
	location = db.StringProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)
	playlist = db.ReferenceProperty(Playlist, collection_name="songs")

