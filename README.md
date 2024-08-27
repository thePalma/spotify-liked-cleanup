# Spotify Liked Songs Cleaner

This project was born out of my need to clean up the Liked Songs playlist on Spotify and my obsession about automating anything.
I often end up with 1000+ Liked Songs on Spotify that I eventually get bored listening to, so I needed a way to clean it up quickly.

## Prerequisite

To use this tool, you will need a Spotify for Developers account, which you can get access to https://developer.spotify.com/. You will need to create a new app and that will provide you with a Spotify client id and secret.

## Usage

This is a simple Python script that relies on [Spotipy](https://spotipy.readthedocs.io/en)

```
$ git clone ...
```

Install required modules:

```
$ pip install -r requirements.txt
```

Reference the Spotify API credentials here:

```
$ export SPOTIFY_CLIENT_ID=<<your spotify client id>>
$ export SPOTIFY_CLIENT_SECRET=<<your spotify secret>>
$ export SPOTIFY_USERNAME=<<your spotify username>>
```

Change the OFFSET variable to set which song to start deletion from:

```
OFFSET = <<set offset here>>
```

Running the tool:

```bash
python3 spotify-liked-cleanup.py
```
