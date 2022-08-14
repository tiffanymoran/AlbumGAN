import requests
from bs4 import BeautifulSoup
import os
import lyricsgenius as lg
from lyricsgenius import Genius
import json
from requests.exceptions import Timeout
import pandas as pd

def get_lyrics(album_name, artist_name): #function to search through lyrics on genius.com
    genius.timeout = 15
    genius.sleep_time = 40
    for x, y in zip(album_name, artist_name):
        album = genius.search_album(x, y)
        song_lyrics = album.save_lyrics(filename=x)
    
def write_lyrics(album_name): #function to write all album lyrics to a single .txt file
        for x in album_name:
            with open(x + '.json') as json_file:
                data = json.load(json_file)
            out = x + '.txt'
            f = open(x, 'w+')
            length_key = len(data['tracks'])
            album_range = range(length_key - 1)
            for i in album_range:
                f.write(data['tracks'][i]['song']['lyrics'])
            f.close()

df = pd.read_csv('AlbumList.csv')

df = df.iloc[550:]

albums = list(df['Album'])

artists = list(df['Artist'])

genius = Genius('t_ciOWaV0Hro-pR8_rSRQk_mpGJzn5dpTOhlqRIWKuOkFdmgeLKpc_4tZC3nBuk3')
get_lyrics(albums, artists)