from bs4 import BeautifulSoup
import requests as req
from datetime import datetime
from env import *
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

entering_year = True
while entering_year:
    year_input = input('Which year would you like to travel to? please enter a year in YYYY-MM-DD format:\n')
    try:
        chosen_year_dt_obj = datetime.strptime(year_input, '%Y-%m-%d')
    except ValueError:
        print("please enter a year in YYYY-MM-DD format")
    if chosen_year_dt_obj:
        if chosen_year_dt_obj > datetime.now():
            print('Date must be in the past.')
        else:
            chosen_year_final = datetime.strftime(chosen_year_dt_obj, '%Y-%m-%d')
            entering_year = False
billboard_url = f"https://www.billboard.com/charts/hot-100/{chosen_year_final}/"
res = req.get(billboard_url)
billboard_page = res.text
soup = BeautifulSoup(billboard_page, "html.parser")
song_names = [row.find(id='title-of-a-story').getText().strip() for row in soup.select('.o-chart-results-list-row')]
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
song_uris = []
year = chosen_year_final.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        # print(f"{song} doesn't exist in Spotify. Skipped.")
        pass
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{chosen_year_final} Billboard 100",
    public=False
)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
