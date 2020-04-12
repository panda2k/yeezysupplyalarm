import pychromecast
from pychromecast.controllers.spotify import SpotifyController
import spotify_token as st
import spotipy
import time

CAST_NAME = 'Michaels room speaker'
def play_music(song_uri):
    devices = pychromecast.get_chromecasts()
    speaker = next(cc for cc in devices if cc.device.friendly_name == CAST_NAME)
    speaker.wait()
    data = st.start_session("little_wang", "Jumbobean123")
    access_token = data[0]
    expires = data[1] - int(time.time())

    client = spotipy.Spotify(auth=access_token)
    sp = SpotifyController(access_token, expires)
    speaker.register_handler(sp)
    sp.launch_app()
    devices_available = client.devices()
    for device in devices_available['devices']:
        if device['name'] == CAST_NAME:
            device_id = device['id']
            break
    speaker.set_volume(0.5)
    client.start_playback(device_id=device_id, uris=[song_uri])

play_music('spotify:track:49fT6owWuknekShh9utsjv')
