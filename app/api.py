import spotipy
import random
import os

from spotipy.oauth2 import SpotifyClientCredentials


#os.environ["SPOTIPY_CLIENT_ID"] = 'b744b689be034874b6ca5f446ef730e2'
#os.environ["SPOTIPY_CLIENT_ID"] = '7d32b9bd1c8a4ebda4b3b158bee501fc'
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)
#export SPOTIPY_CLIENT_ID='b744b689be034874b6ca5f446ef730e2'
#export SPOTIPY_CLIENT_SECRET='7d32b9bd1c8a4ebda4b3b158bee501fc'


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
    return spotify_link