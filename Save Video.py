import requests

response = requests.get(url="https://parsinger.ru/video_downloads/videoplayback.mp4", stream=True)
with open('filee.mp4', 'wb') as video:
    for piece in response.iter_content(chunk_size=100000):
        video.write(piece)