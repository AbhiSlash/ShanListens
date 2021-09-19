import tweepy
import requests
import time
# from configparser import ConfigParser
import keys as keys

API_KEY = keys.API_KEY
API_SECRET_KEY = keys.API_SECRET_KEY
ACCESS_TOKEN = keys.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = keys.ACCESS_TOKEN_SECRET

auth = tweepy.auth.OAuthHandler(API_KEY,API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
previousSongName = ""
# Fetching the playing song
while(1):
    response = requests.get("https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=derptag&api_key=9b49d26565bb4392f5a2a28b42a84838&format=json")
    recentTracks = response.json()
    lastTrack = recentTracks['recenttracks']['track'][0]
    artistName = lastTrack['artist']['#text']
    albumName = lastTrack['album']['#text']
    songName = lastTrack['name']
    if(songName != previousSongName):
        status = "Abhilash Sadanand is listening to" + "\n" "🔊 " + songName + " by " + artistName + "\n"  + "📀 " + albumName
        try:
            api.update_status(status)
        except:
            print("Same song!")
            previousSongName = songName
    else:
        pass
    time.sleep(200)
