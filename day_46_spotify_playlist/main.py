## Requirements
# Build a program that searches for the 100 top songs from this list https://www.billboard.com/charts/hot-100/2000-08-26/
# Collect all the songs, and search for the songs in spotify and add the songs into a playlist
# The playlist should be named: Week: YYYY-MM-DD Billboard 100 -> Example(Week: 2000-08-26 Billboard 100)
# ##
import urllib.parse
import dotenv
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

dotenv.load_dotenv()
# -------------My Variables-------------
WEEK = "2000-08-26"
URL = "https://www.billboard.com/charts/hot-100/2000-08-26/"
SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""
SPOTIFY_REDIRECT_URI = ""
SPOTIFY_SCOPE = "playlist-modify-private"
SPOTIFY_PLAYLIST = "https://api.spotify.com/v1/users/{user_id}/playlists"
SPOTIFY_USER_ID = ""

# -------------Connect to Spotify and Create Playlist-------------
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope=SPOTIFY_SCOPE
))

create_playlist = sp.user_playlist_create(
    user=SPOTIFY_USER_ID,
    name="Week: 2000-08-26 Billboard 100",
    public=False
)

get_playlist_id = create_playlist['id']

# -------------Scrap songs from Billboards-------------
song_list_response = requests.get(url=URL)
website_response = song_list_response.text

# -------------Get the list of songs from Billboard-------------
soup = BeautifulSoup(website_response, "html.parser")

titles_initial_selectors = soup.select(".lrv-u-width-100p ul li h3")

# --- Get Songs ---
songs_title_list_raw_data = [each_song.getText().strip() for each_song in titles_initial_selectors]
songs_title_list_cleaned_data = songs_title_list_raw_data[:20]

# --- Get Artist ---
class_names_for_artist_selector = [
    "c-label",
    "a-no-trucate",
    "a-font-primary-s",
    "lrv-u-font-size-14@mobile-max",
    "u-line-height-normal@mobile-max",
    "u-letter-spacing-0021",
    "lrv-u-display-block",
    "a-truncate-ellipsis-2line",
    "u-max-width-330",
    "u-max-width-230@tablet-only"
]

# Find all elements matching the list of class names
artists_selector = soup.find_all("span", class_=lambda class_value_in_html: all(
    each_class in class_value_in_html.split() for each_class in class_names_for_artist_selector))

artist_list = [each_artist.getText().strip() for each_artist in artists_selector][:20]
song_and_artist_list = zip(songs_title_list_cleaned_data, artist_list)

track_id_list = []

# -------------Search for Songs by artist and add them to Spotify Playlist -------------
for each_track in song_and_artist_list:
    song, artist = each_track
    f"track:{song} artist:{artist}"

    original_query = f"{song} {artist}"
    encoded_query = urllib.parse.quote(original_query)

    search_track = sp.search(q=encoded_query, limit=1, type='track')

    if search_track["tracks"]["items"]:
        track_id = search_track["tracks"]["items"][0]["uri"]
        track_id_list.append(track_id)
    else:
        print(f"No results found for: {song} by artist: {artist}")

sp.playlist_add_items(playlist_id=get_playlist_id, items=track_id_list)

new_playlist_songs = sp.playlist_items(playlist_id=get_playlist_id, limit=20)