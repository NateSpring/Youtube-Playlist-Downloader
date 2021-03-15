from pytube import Playlist, YouTube
import os
from PIL import Image
import requests

dirname = os.path.dirname(__file__)

urls = [
    'playlist url here',
    'playlist url here',
    'playlist url here',
]

for url in urls:
    try:
        # Get palylist, then make directory with its name.
        playlist = Playlist(url)
        if os.path.exists(
                os.path.join(dirname + '/output_folder/' + playlist.title)):
            dl_dir = os.path.join(dirname + '/output_folder/' + playlist.title)
        else:
            new_dir = os.mkdir(
                os.path.join(dirname + '/output_folder/' + playlist.title))
            dl_dir = os.path.join(dirname + '/output_folder/' + playlist.title)
        # Loop through the playlists videos and download them.
        for video in playlist.video_urls:
            video = YouTube(video)
            title = video.title
            title = title.replace('/', '')
            thumb = video.thumbnail_url
            thumb_name = thumb.split('/')[-1]

            print(thumb)
            try:
                print('Thumbnail Downloading...')
                bg_img_name = thumb_name.replace('maxresdefault', title)
                bg_img = Image.open(requests.get(thumb, stream=True).raw)
                bg_img.save(dl_dir + '/' + bg_img_name)
                print('Thumbnail Save Successful: {}'.format(bg_img_name))

            except Exception as e:
                print(e)
                print('Failed: Thumbnail download:  {}'.format(bg_img_name))
                pass

            print("Downloading: %s" % title)
            # video.streams.get_highest_resolution().download(dl_dir)
            print("----Done Downloading: %s" % title)
    except Exception as e:
        print(e)
        continue
    print('All downloads complete')
