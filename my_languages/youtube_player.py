import pafy
import vlc

"""
    이 파일은 github repository 중 (https://github.com/TamerlanG/Youtube-Console-MP3-Player)를 참조해서 만들었습니다. 자세한 것은 이 리포지토리 홈페이지에서 확인해주시기 바랍니다.
"""


def play_song(videoid : str):
    is_opening = False
    is_playing = False

    video = pafy.new(videoid)
    best = video.getbestaudio()
    play_url = best.url

    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(play_url)
    media.get_mrl()
    player.set_media(media)
    player.play()

    good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
    while str(player.get_state()) in good_states:
        if str(player.get_state()) == "State.Opening" and is_opening is False:
            print("Status: Loading")
            is_opening = True

        if str(player.get_state()) == "State.Playing" and is_playing is False:
            print("Status: Playing")
            is_playing = True

    print("Status: Finish")
    player.stop()