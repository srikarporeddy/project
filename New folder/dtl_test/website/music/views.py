from django.http import Http404
from django.shortcuts import render
#from django.http import HttpResponse
from .models import Album
#from django.template import loader 



def index(request):
	all_albums = Album.objects.all()
	#template = loader.get_template('music/index.html')
	context = {'all_albums': all_albums}
	
	'''html = ''
	for album in all_albums:
		url = '/music/'+ str(album.id) + '/'
		html += '<a href="'+ url +'"> '+ album.album_title + '</a><br>'
	'''
	#return HttpResponse(template.render(context, request)) 
	return render(request,'music/index.html',context)
	#shoetcut we can use render next line '''
	#return render(request,'music/index.html', context)

def detail(request, album_id):
	try:
		album = Album.objects.get(pk=album_id)
	except Album.DoesnotExist:
		raise HttpResponse("Album does not exist")
	return  render(request,'music/detail.html',{ 'album': album})
	'''else:
		pass
	finally:
		pass
	return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")
	''''''try:
		album = Album.objects.get(pk=album_id)
	except Album.DoesnotExist:
		raise Http404("Album does not exist ")
	return render(request,'music/detail.html', context)
	
'''
# Create your views here.
