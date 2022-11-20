
# - 채널 만들기
import telegram
import schedule
import time
import datetime
import pytz

token = "여기 토큰인데 깃헙에서 토큰 가리라고 메일옴;;"
bot = telegram.Bot(token)
public_chat_name = "@ktest2022"

def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return
    text = f"current time = {0}".format(str(now))
    bot.sendMessage(chat_id = public_chat_name, text = "alarm").chat_id
    # print("current time = ", str(now))

schedule.every(1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(30)

# # id_channel = bot.sendMessage(chat_id = public_chat_name, text = "alarm").chat_id
# print(id_channel)