#!/usr/bin/env python3

import os
import spotipy

OFFSET = 0

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
username = os.getenv('SPOTIFY_USERNAME')

print(f'Client ID: {client_id}')
print(f'Client Secret: {client_secret}')

scope = 'user-library-read user-library-modify playlist-modify-public playlist-modify-private'

token = spotipy.util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

sp = spotipy.Spotify(auth=token)

for _ in range(100):
    to_remove = []
    try:
        liked_songs:dict = sp.current_user_saved_tracks(limit=50, offset=OFFSET)
        for id, song in enumerate(liked_songs['items']):
            to_remove.append(song['track']['id'])
            print(f'Listing {song["track"]["name"]} by {song["track"]["artists"][0]["name"]}')
        if len(to_remove) == 0:
            print('No songs to remove')
            break
        if len(to_remove) == 1:
            print(f'Removing {len(to_remove)} song')
        else:
            print(f'Removing {len(to_remove)} songs')
        sp.current_user_saved_tracks_delete(tracks=to_remove)
    except Exception as e:
        print(f'Error: {e}')
        exit()