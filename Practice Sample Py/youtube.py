

try:
    from pytube import YouTube
    from pytube import Playlist
except Exception as e:
    print('Some modules are missing {}'.format(e))


url='https://www.youtube.com/watch?v=2qRt6aFPICg'
ytd = YouTube(url)
print(ytd)