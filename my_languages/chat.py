#  파이썬에 적용할 모듈을 이용합니다.
import os
import openai
from playsound import playsound
import youtubemusic_download_mp3

# 자신이 OPENAI 계정에 있는 API-KEY를 복사하여서 여기에다가 붙여 놓습니다.
openai.api_key = input("Enter your API-KEY : ")

# AI와 Human의 주체를 생성합니다.
start_sequence = "\nAI:"
chat_question = "\nHuman: "

# OPENAI중 CHAT 봇 중 text-davinci-003이 채팅의 머신러닝을 가진 봇이므로 이를 이용하여 AI 봇을 만듭니다.
firstchat_response_sentence = "The following is a conversation with an listening music AI assistant. The assistant is helpful, creative, clever, and very friendly.\n"
print(firstchat_response_sentence)
my_prompt = firstchat_response_sentence

# 마지막으로 AI 봇이 "Enjoy"문장이 포함되면 이에 따라 자동적으로 음원 다운로드가 되며, 재생됩니다.
while True: 
  chat_answer = input(f"{chat_question}")
  my_prompt = my_prompt + chat_question + chat_answer 
  response = openai.Completion.create(model="text-davinci-003", prompt= my_prompt, temperature=0.6, max_tokens=150, top_p=1, frequency_penalty=0, presence_penalty=0.6, stop=[" Human:", " AI:"])
  print(response["choices"][0]["text"])
  my_prompt += response["choices"][0]["text"]
  if "Enjoy" in my_prompt:
    youtubemusic_download_mp3.download_ytvid_as_mp3(chat_answer=chat_answer)
    playsound(f"my_languages\\music_resources\\{chat_answer}.mp3")
    
    # 음원 재생이 마치면 이 프로그램은 종료됩니다.
    break



  