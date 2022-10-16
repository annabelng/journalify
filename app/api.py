import spotipy
import random
import os

from spotipy.oauth2 import SpotifyClientCredentials


auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


id_dict = {
    "fear": "2lkAyQ5IQJ915b1XINnHX3",
    "love": "3dMIEhfffi6N84egPByLIY",
    "happiness": "5yI34GDYLxUxfSrpshdNVE",
    "sadness": "4yXfnhz0BReoVfwwYRtPBm",
    "surprise": "30Zp2r5erHeBJNQi1boSij",
}

def pick_song(emotion):
    id = id_dict['fear'] #gets full detail of tracks in specific emotion playlist
    list_tracks = sp.playlist_tracks(id)
    #print(list_tracks)

    #track = random.choice(list_tracks)
    # print(random.choice(list_tracks['items']))
    items = list_tracks['items']
    item = list_tracks['items'][random.randint(0,len(items))]
    track = item['track']
    #print("track", track)
    #print()
    urls = track['external_urls']
    #print("urls", urls)
    #print()
    spotify_link = urls['spotify']
    #print(spotify_link)
    details = {
        "title": 
        "link": spotify_link
    }
    return spotify_link