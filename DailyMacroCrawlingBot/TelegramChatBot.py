import telepot
from telepot.loop import MessageLoop
 
token = '60950303AAGG_IqTO109_rAMP56OMh0_f7P5aOo3G2U43:' # Telebot에게 받은 봇 API 토큰
mychid = '1135987650' # userinfobot에서 받은 값
bot = telepot.Bot(token)
 
 
def handle(message):
    print(message)
    bot.sendMessage(mychid, '멍충이')
 
 
MessageLoop(bot, handle).run_as_thread()
 
while True:
    pass
