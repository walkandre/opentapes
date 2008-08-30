from google.appengine.ext.db import djangoforms

import models

class PlaylistForm(djangoforms.ModelForm) :
	class Meta:
		model = models.Playlist
		exclude = ['created', 'author']
		
		
class SongForm(djangoforms.ModelForm) :
	class Meta:
		model = models.Song
		exclude = ['created', 'author']