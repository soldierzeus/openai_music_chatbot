import youtube_dl
def download_ytvid_as_mp3():
    video_code = ""
    if 
    video_url = "https://www.youtube.com/watch?v=" + video_code
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    music_title = video_info['title'].replace(" ", "")
    filename = f"my_languages\\music_resources\\{music_title}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])