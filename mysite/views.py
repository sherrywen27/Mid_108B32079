from django.shortcuts import render
from django.http import HttpResponse
from mysite import models


# Create your views here.
def index(request):
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()
    try:
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
    except:
        urid = None

    if urid is not None and urpass == '12345':
        verified = True
    else:
        verified = False

    return render(request, 'index.html', locals())