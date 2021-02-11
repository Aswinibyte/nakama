import telegram
import telegram.ext
import re
from datetime import datetime


# def answers(input_text):
#     user_message12 = str(input_text).lower()

#     if user_message12 in ("i don't know"):
#         return "Well whatever it is.. You should take care of yourself"

#     if user_message12 in ("it is hot"):
#         return "Please take care of yourself.. It seems like it is hot outside.. Make sure to drink plenty of water"

#     if user_message12 in ("it is cold"):
#         return "Oo.. It seems it's a bit cold out there.. Make sure to keep youself warm"

#     if user_message12 in ("it is pleasant"):
#         return "That's nice.. it sounds lovely"


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "hey", "whats up", "hui", "sup"):
       return "Hello! I am Nakama, a virtual interactive bot made by my father Aswini.\nI can do various stuff too..\nYou can ask 'Who are you?' to know more about me\nOr you can use '/help' command to know about some of my functions"

    if user_message in ("who are you?", "who are u?", "what are you?", "who r u?", "what r u?","what r u","what are you","who r u","who are you","who are u"):
       return "I am a bot.. You might have know some of my friends. They go by the name Siri and Alexa. Let me tell you something I don't like Siri very much"

    if user_message in ("why don't u like her?", "y don't u like her?", "why don't you like her?", "y don't you like her?", "why don't u like her", "y don't u like her", "y don't you like her", "why don't you like her", "why?", "why", "y?", "y"):
       return "I don't know I am a bot.. I don't have feelings.. It's my father who put that answer in me.. Frankly i think he says that because he can't afford one"

    if user_message in ("oo.. i see","ohh","ooo","haha","nice","u are funny","you are funny","u r funny","you r funny"):
        return "Well what can we do.. It is what it is"
   # if user_message in ("i don't know","no idea"):
   #      return "Well whatever it is.. You should take care of yourself"

    if user_message in ("it is hot","it is kind of hot"):
        return "Please take care of yourself.. It seems like it is hot outside.. Make sure to drink plenty of water"

    if user_message in ("it is cold","it is a bit cold"):
        return "Oo.. It seems it's a bit cold out there.. Make sure to keep youself warm"

    if user_message in ("it is pleasant"):
        return "That's nice.. it sounds lovely"

    if user_message in ("i don't know", "no idea"):
         return "It's ok!! Well whatever it is.. you should take care of yourself"

    if user_message in ("do you like memes?", "do u like memes?", "do you like memes", "do u like memes"):
        return "I really really like them.. in fact it would have been difficult sitting here all day without something interesting to keep you going right"

   #  if user_message in ("time", "time?", "whats the time?", "what is the time right now"):
   #     now = datetime.now()
   #         date_time = str(now.strftime("%d/%m/%y, %H:%M:%S"))

   #             return str(date_time)

    # if user_message in ("date", "date?", "whats today's date?", "Do you know today's date?"):
    #    now = datetime.now()
    #        date = now.strftime("%d/%m/%y")

    #            return str(date)
    
    return "I don't understand what you are saying... Actually my father is quite new to this and also he is not talented enough XD... I still don't know how he got into an IIT"
     

# def youtube_responses(input_text):
#    user_message1 = str(input_text).lower()

#    if user_message1 in ("dance"):
#       return ""

#    if user_message1 in ("music"):
#       return ""

#    if user_message1 in ("comedy"):
#       return ""

#    if user_message1 in ("news"):
#       return ""

#    if user_message1 in ("learning"):
#       return ""

#    if user_message1 in ("fashion"):
#       return ""

#    if user_message1 in ():
#       return ""