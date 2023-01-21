# 이 파일은 OPENAPI 사이트를 참고하여서 이를 만들게 되었습니다. 자세한 것이 필요하신 분들은 (https://openai.com/api/)를 참고해주시기 바랍니다.

#  파이썬에 적용할 모듈을 이용합니다.
import os
import openai
import dotenv
import argparse
from apiclient.errors import HttpError
from youtube_search_song import youtube_search

# OPENAI중 CHAT 봇 중 text-davinci-003이 채팅의 머신러닝을 가진 봇이므로 이를 이용하여 AI 봇을 만듭니다.
# 마지막으로 AI 봇이 "Enjoy"문장이 포함되면 이에 따라 자동적으로 음원 다운로드가 되며, 재생됩니다.
def openai_davinchi():
  # 자신이 OPENAI 계정에 있는 API-KEY를 복사하여서 여기에다가 붙여 놓습니다.
  config = dotenv.dotenv_values(".env")
  openai.api_key = config['OPENAI_API_KEY']
  # AI와 Human의 주체를 생성합니다.
  start_sequence = "\nAI:"
  chat_question = "\nHuman: "
  # AI와 Human의 주체를 생성합니다.
  start_sequence = "\nAI Assistant:"
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
    if "Enjoy" in my_prompt or "relax" in my_prompt:
      parser = argparse.ArgumentParser()
      parser.add_argument("--q", help="Search term", default=chat_answer)
      parser.add_argument("--max-results", help="Max results", default=5)
      args = parser.parse_args()
      try:
        youtube_search(args)
      except HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
        for action in parser._actions:
          opts = action.option_strings
          if (opts and opts[0] == "q") or action.dest == "q":
            parser._remove_action(action)
            break
        for action in parser._action_groups:
          for group_action in action._group_actions:
            if group_action.dest == "q":
                action._group_actions.remove(group_action)
        for action in parser._actions:
          opts = action.option_strings
          if (opts and opts[0] == "max-results") or action.dest == "max-results":
            parser._remove_action(action)
            break
        for action in parser._action_groups:
          for group_action in action._group_actions:
            if group_action.dest == "max-results":
                action._group_actions.remove(group_action)
      openai_continue_question = input("Do you want to continue to use AI Assistant? [yes or no?]")
      if openai_continue_question == "yes":
        my_prompt = "What do you want to listen to music?" + start_sequence
        continue
      elif openai_continue_question == "no":
        print("Thank you for using AI Assistant!")
        break

if __name__ == "__main__":
  openai_davinchi()

      
    



  