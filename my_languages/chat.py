import os
import openai
from playsound import playsound

openai.api_key = input("Enter your API-KEY : ")

start_sequence = "\nAI:"
chat_question = "\nHuman: "

firstchat_response_sentence = "The following is a conversation with an listening music AI assistant. The assistant is helpful, creative, clever, and very friendly.\n"
print(firstchat_response_sentence)
my_prompt = firstchat_response_sentence
while True: 
  chat_answer = input(f"{chat_question}")
  my_prompt = my_prompt + chat_question + chat_answer 
  response = openai.Completion.create(model="text-davinci-003", prompt= my_prompt, temperature=0.6, max_tokens=150, top_p=1, frequency_penalty=0, presence_penalty=0.6, stop=[" Human:", " AI:"])
  print(response["choices"][0]["text"])
  my_prompt += response["choices"][0]["text"]
  if "Enjoy" in my_prompt:
    playsound(f"my_languages\\music_resources\\{chat_answer}.mp3")
    break



  