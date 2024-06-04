import requests
def download_clip(clip):
    index = clip.thumbnail_url.find('-preview')
    clip_url = clip.thumbnail_url[:index] + '.mp4'
    r = requests.get(clip_url)

    if r.headers['Content-Type'] == 'binary/octet-stream':
        if not os.path.exists('files/clips'): os.makedirs('files/clips')
        with open(clip.path, 'wb') as f:
            f.write(r.content)

    else:
        print(f'Failed to download clip from thumb: {clip.thumbnail_url}')