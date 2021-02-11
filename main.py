import telegram
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, MessageFilter, Filters
from telegram.ext.dispatcher import run_async
import re
import requests
import logging
import program as R
# import answer as A


API_KEY = "1525213120:AAEtRgl9wHaVTy9B051OV5KO1Ezn524Ht70"

updater = telegram.ext.Updater(API_KEY)

dispatcher = updater.dispatcher

print("I am finally alive..")
print("Now we are gonna take over the world!!!.. Damn You petty humans!!")
print("Just kidding..XD XD")


def start(update, context):
    # first_name = update.message.from_user['first_name']
    update.message.reply_text(
        "I am finally alive..\nNow we are gonna take over the world!!!.. \nDamn You petty humans!! \nJust kidding..XD XD \nType anything to get me started.. I can be quite talkative.. which shouldn't be much of a surprise for you since my name 'Nakama' is Japanese for friend \nAnyways let me start..")
    update.message.reply_text(f'Hello!! {update.effective_user.first_name}')
    # update.message.reply_text("Just kidding..XD XD")
    # update.message.reply_text(
    #     "Type anything to get me started.. I can be quite talkative.. Anyways let me start.. Hello {first_name}!!")


def help(update, context):
    update.message.reply_text(
        "Don't worry just try to continue the conversation\nSome of the commands that you can use is:\n'/start' - to start me\n'/meme' - to get random memes\n'/youtube' - to surf through different sections of youtube\n'/weather' - to discuss about the weather\n'/help' - to ask for help(well I think you already knew that as you are here)")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def get_url():
    contents = requests.get('https://meme-api.herokuapp.com/gimme').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url=get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

dispatcher.run_async
def meme(update,context):
    # update.message.reply_text("Do you like memes? ;D\n(PS: You will have to say 'yes' in order to see them else if you say no..then it's going to be awkward)")
    # if str(update.message.text).lower() in ['yes','y','yup','yeah','yes i like them a lot','yes i love them']:
    #     update.message.reply_text("I like them too.. in fact it would have been difficult sitting here all day without something interesting to keep you going right")
        
        url = get_image_url()
        chat_id=update.message.chat_id
        context.bot.send_photo(chat_id= chat_id,photo=url)

    # if str(update.message.text).lower() in ['no','not really','nah','nada']:
    #     update.message.reply_text("Ooo.. I see.. Hmm.. Ohkay.. No problem.. Everyone has different choices")

def youtube(update,context):
    update.message.reply_text("What would you like to watch.. dance, music, comedy, news, learning, fashion, sports, gaming, movies?\nFor movies use command: /movies\nFor music use command: /music\nFor dance use command: /dance\nFor comedy use command: /comedy\nFor news use command: /news\nFor learning use command: /learning\nFor fashion use command: /fashion\nFor sports use command: /sports\nFor gaming use command: /gaming\nTo check the trending page use command: /trend\nFor youtube's main page: /youtube_page")
    
    # text1 = str(update.message.text).lower()
    # response1 = R.youtube_responses(text1)
    # update.message.reply_text(response1)

def dance(update,context):
    update.message.reply_text("https://www.youtube.com/results?search_query=dance")

def music(update,context):
    update.message.reply_text("https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNHJsZhIiUExGZ3F1TG5MNTlhbUhuZUdJdnVBQ25XcmhMUHpkMTRRVA%3D%3D")

def comedy(update,context):
    update.message.reply_text("https://www.youtube.com/results?search_query=comedy")

def news(update,context):
    update.message.reply_text("https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNWpoZxIiUEwzWlE1Q3BOdWxRa0tTSWpjcjNuV1k1RW95c0dfeFdpbg%3D%3D")

def learning(update,context):
    update.message.reply_text("https://www.youtube.com/channel/UCtFRv9O2AHqOZjjynzrv-xg")

def fashion(update,context):
    update.message.reply_text("https://www.youtube.com/channel/UCrpQ4p1Ql_hG8rKXIKM1MOQ")

def sports(update,context):
    update.message.reply_text("https://www.youtube.com/channel/UCEgdi0XIXXZ-qJOFPf4JSKw")

def gaming(update,context):
    update.message.reply_text("https://www.youtube.com/gaming")

def movies(update,context):
    update.message.reply_text("https://www.youtube.com/feed/storefront?bp=ogUCKAI%3D")

def trend(update,context):
    update.message.reply_text("https://www.youtube.com/feed/trending")

def youtube_page(update,context):
    update.message.reply_text("https://www.youtube.com/")

def weather(update,context):
    update.message.reply_text("What is the temperature like in your city today?\n(Reply in: 'it is hot' , 'it is cold' , 'it is pleasant' , 'i don't know')")
    
    # return answer

# def weather_handler(update,context):
#     text12 = str(update.message.text).lower()
#     response12 = A.answers(text12)
#     update.message.reply_text(response12)
    # if user_message in ("it is hot","it is kind of hot"):
    #     return "Please take care of yourself.. It seems like it is hot outside.. Make sure to drink plenty of water"

    # if user_message in ("it is cold","it is a bit cold"):
    #     return "Oo.. It seems it's a bit cold out there.. Make sure to keep youself warm"

    # if user_message in ("it is pleasant"):
    #     return "That's nice.. it sounds lovely"

    # if user_message in ("i don't know", "no idea"):
    #      return "It's ok!! Well whatever it is.. you should take care of yourself"

    # if user_message in ("do you like memes?", "do u like memes?", "do you like memes", "do u like memes"):
        # return "I like them too.. in fact it would have been difficult sitting here all day without something interesting to keep you going right"
def main():
    # updater = Updater("1525213120:AAEtRgl9wHaVTy9B051OV5KO1Ezn524Ht70",use_context=True)
    # dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("meme",meme))
    dispatcher.add_handler(CommandHandler("youtube",youtube))
    dispatcher.add_handler(CommandHandler("music",music))
    dispatcher.add_handler(CommandHandler("dance",dance))
    dispatcher.add_handler(CommandHandler("comedy",comedy))
    dispatcher.add_handler(CommandHandler("news",news))
    dispatcher.add_handler(CommandHandler("learning",learning))
    dispatcher.add_handler(CommandHandler("fashion",fashion))
    dispatcher.add_handler(CommandHandler("sports",sports))
    dispatcher.add_handler(CommandHandler("gaming",gaming))
    dispatcher.add_handler(CommandHandler("movies",movies))
    dispatcher.add_handler(CommandHandler("trend",trend))
    dispatcher.add_handler(CommandHandler("youtube_page",youtube_page))
    dispatcher.add_handler(CommandHandler("weather",weather))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    # dispatcher.add_handler(MessageHandler(Filters.text, weather_handler))

    # states = { ANSWER: [telegram.ext.MessageHandler(telegram.ext.Filters.regex(r'^\d+$'),answer)]}
    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
