from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from .models import Track
import json
# Create your views here.
def default_track_view (request):
  return HttpResponse ('Default Tracks View')

def track_view (request,title):
  track = get_object_or_404(Track, title=title)

  data = {
    'title':track.title,
    'order':track.order,
    'album':track.album.title,
    'artista':{
      'name':track.artist.fris_name,
      'bio':track.artist.biography,
    }
  }

  json_data = json.dumps(data)

  return HttpResponse(json_data,content_type='application/json')
  #return render(request,'track.html',{'track':track})
