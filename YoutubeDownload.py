from pytube import YouTube
#link = input("link : ")

def just_video_download(link):
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    video_stream = yt.streams.filter(only_video=True, res="1080p", subtype="mp4").first()
    video_stream.download()

def just_audio_download(link):
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    video_stream = yt.streams.filter(only_audio=True, subtype="mp3").first()
    video_stream.download()

def video_download(link):
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    video_stream = yt.streams.filter(res="1080p", subtype="mp4").first()
    video_stream.download()
