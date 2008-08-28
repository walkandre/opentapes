from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def index(request):
#	query = models.Post.gql("ORDER BY created DESC")

	return render_to_response('index.html')


def create(request):

	return render_to_response('create.html')
#	return render_to_response('search.html', { 'posts': query.run() })


def search(request, keyword=""):
	
#	return render_to_response('search.html', { 'posts': query.run() })
	return render_to_response('search.html', { 'keyword': keyword })
