import requests
from django.shortcuts import render
from django.conf import settings

def artist_search(request):
    artist_data = None
    top_tracks = []
    similar_artists = []
    top_tags = []
    top_albums = []
    album_image = None
    query = request.GET.get('q', '')

    if query:
        artist_response = requests.get(settings.LASTFM_BASE_URL, params={
            'method': 'artist.getinfo',
            'artist': query,
            'api_key': settings.LASTFM_API_KEY,
            'format': 'json'
        })
        data = artist_response.json()
        if 'artist' in data:
            artist_data = data['artist']

        toptracks_response = requests.get(settings.LASTFM_BASE_URL, params={
            'method': 'artist.gettoptracks',
            'artist': query,
            'api_key': settings.LASTFM_API_KEY,
            'format': 'json',
            'limit': 5,
        })
        toptracks_data = toptracks_response.json()
        if 'toptracks' in toptracks_data:
            top_tracks = toptracks_data['toptracks']['track']



        similar_response = requests.get(settings.LASTFM_BASE_URL, params={
            'method': 'artist.getsimilar',
            'artist': query,
            'api_key': settings.LASTFM_API_KEY,
            'format': 'json',
            'limit': 5,
        })
        similar_data = similar_response.json()
        if 'similarartists' in similar_data:
            similar_artists = similar_data['similarartists']['artist']
        
        tags_response = requests.get(settings.LASTFM_BASE_URL, params={
            'method': 'artist.gettoptags',
            'artist': query,
            'api_key': settings.LASTFM_API_KEY,
            'format': 'json',
            'limit': 5,
        })
        tags_data = tags_response.json()
        if 'toptags' in tags_data:
            top_tags = tags_data['toptags']['tag']

        top_albums_response = requests.get(settings.LASTFM_BASE_URL, params={
            'method': 'artist.gettopalbums',
            'artist': query,
            'api_key': settings.LASTFM_API_KEY,
            'format': 'json',
            'limit': 5,
        })
        top_albums_data = top_albums_response.json()
        if 'topalbums' in top_albums_data:
            top_albums = top_albums_data['topalbums']['album']
            
        for album in top_albums:
            images = album.get('image', [])
            album['cover'] = None
            for img in reversed(images):
                if img.get('#text'):
                    album['cover'] = img['#text']
                    break 

    

    return render(request, 'artists/search.html', {
        'artist': artist_data,
        'top_tracks': top_tracks,
        'similar_artists': similar_artists,
        'top_tags': top_tags,
        'top_albums': top_albums,
        'query': query
    })

    
