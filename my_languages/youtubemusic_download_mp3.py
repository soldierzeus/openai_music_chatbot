import youtube_dl
def download_ytvid_as_mp3(chat_answer):
    # 음성인식을 위해 원하는 대상키워드 적기
    if chat_answer in "SUN GOES DOWN (Prod. R.Tee)":
        video_code = "Qet5daXv06Q"
    elif chat_answer in "RECEIPTS (Prod. by Slom)":
        video_code = "yM5WjkuxbhY"
    elif chat_answer in "WOW (Prod. GroovyRoom)":
        video_code = "rVhjTJMyWJg"
    elif chat_answer in "Be my":
        video_code = "szSvYuSu5n4"
    elif chat_answer in "We Higher(위하여) (Prod. GroovyRoom)":
        video_code = "NMd7u0TEWHU"
    elif chat_answer in "AJUSHI":
        video_code = "jtfSQZsqin8"
    elif chat_answer in "WE (Feat. Jay Park) (Prod. by Slom)":
        video_code = "vswVFvRvrRU"
    elif chat_answer in "MY WAY (Prod. R.Tee)":
        video_code = "R8R-wc4lqc8"
    elif chat_answer in "ERI ERI(으리으리) (Feat. Homies)":
        video_code = "CEq4_q-sKsQ"
    elif chat_answer in "BLUE CHECK (Feat. Jay Park, Jessi) (Prod. by Slom)":
        video_code = "g6EKbho4YnA"
    elif chat_answer in "COMPASS(나침반) (Feat. UNEDUCATED KID, SUPERBEE) (Prod. R.Tee)":
        video_code = "4rFpqDaBKBE"
    elif chat_answer in "BINGO (Feat. meenoi, george) (Prod. by Slom)":
        video_code = "b67TS-VXV0o"
    elif chat_answer in "Burn Up(펄펄) (Feat. Dynamicduo) (Prod. R.Tee)":
        video_code = "r_YtIwfz_cw"
    elif chat_answer in "NOT SORRY (Feat. pH-1) (Prod. by Slom)":
        video_code = "mMrefw3xMEM"
    elif chat_answer in "EYE(눈) (Feat. BIG Naughty, JUSTHIS) (Prod. R.Tee)":
        video_code = "8vnfNZD_E44"
    elif chat_answer in "Vroom (Feat. lIlBOI, Swings) (Prod. GroovyRoom)":
        video_code = "1gekBRKp31M"
    elif chat_answer in "Ugly duckling(미운 오리 새끼) (Feat. sunwoojunga, BOBBY) (Prod. R.Tee)":
        video_code = "TlfBW_tDp8E"
    elif chat_answer in "Name Tag (Feat. Sik-K, Coogie) (Prod. GroovyRoom)":
        video_code = "lAz-rD3SDS4"
    elif chat_answer in "GOBLIN(도깨비) (Feat. Homies) (Prod. R.Tee)":
        video_code = "r_yi7HoWB7g"
    elif chat_answer in "PPAK(빡) (Feat. Paloalto, JUSTHIS) (Prod. R.Tee)":
        video_code = "E9-8T3bz870"
    elif chat_answer in "LIKE WATER (Feat. Loco, HyunA)":
        video_code = "NjBX4r1XiiI"
    elif chat_answer in "LOVE (Feat. Paul Blanco, ASH ISLAND)":
        video_code = "1puIaxhRL6Q"
    elif chat_answer in "WITCH (Feat. Jay Park, So!YoON!) (Prod. by Slom)":
        video_code = "BmDoEJGvuk0"
    elif chat_answer in "HUG (Feat. Zion.T, Wonstein) (Prod. by Slom)":
        video_code = "hSaQk4Grmio"
    elif chat_answer in "ORIGINAL (Feat. Sion) (Prod. R.Tee)":
        video_code = "XGb_ILVNaiQ"
    elif chat_answer in "Chosen 1":
        video_code = "Rm1FdKlVkeA"
    elif chat_answer in "See you ! (Feat. SOLE) (Prod. R.Tee)":
        video_code = "AQia_qn5i2k"
    elif chat_answer in "DEJAVU (Feat. Jay Park) (Prod. by Slom)":
        video_code = "YA-9dmDzEwI"
    elif chat_answer in "Bathtub (Feat. Whee In, JUSTHIS) (Prod. R.Tee)":
        video_code = "CvdHlWZZeSo"
    elif chat_answer in "Diamonds (Feat. lIlBOI, Spray)":
        video_code = "v3waGyIJhVY"
    elif chat_answer in "Way up (Feat. CAMO, JUSTHIS) (Prod. R.Tee)":
        video_code = "KNSabE1xE9Q"
    elif chat_answer in "Go (Prod. GIRIBOY)":
        video_code = "G3BFXyeF6Ck"
        
    # url 기본 정보 적기     
    video_url = "https://www.youtube.com/watch?v=" + video_code
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    
    # file 이름 정하기
    filename = f"my_languages\\music_resources\\{chat_answer}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    
    # 다운로드하기
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])