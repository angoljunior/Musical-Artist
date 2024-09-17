from django.shortcuts import render ,redirect
from django.contrib import messages
from .models import Music ,NewReleases ,Album
from django.db .models import Q

# Create your views here.
def home(request):
    musics =  Music.objects.all()
    #For new musics
    releases = NewReleases.objects.all()
    return render(request, 'home.html' ,{'musics':musics, 'releases': releases})  

def listen(request ,pk):
    musics =  Music.objects.get(id=pk)
    return render(request, 'listen.html' ,{'musics':musics})  

def categories(request,cat):
    cat = cat.replace('-' ,'')
    
    try:
        categories   = Album.objects.get(album = cat)
        musics       = Music.objects.filter(album_title =categories)
        return render(request, 'categories.html' ,{'categories':categories ,'musics':musics})  

    except:
        messages.success(request ,"Product Not Found")
        return redirect('home')
    
def search(request):
    if request.method == 'POST':
        searched = request.POST.get('search')

        if searched:
            searched = Music.objects.filter(Q(song_title__icontains = searched) | Q(artist_name__icontains = searched))
            return render(request ,'search.html' , {'searched': searched})
        else:
            messages.info(request ,'Results not found')
            return redirect('search')
    else:    
        return render(request ,'search.html' , {})


