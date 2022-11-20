
# - 채널 만들기
import telegram
import schedule
import time

token = "5759317578:AAHB10nZxKvOzsBJBw8aBlWamsMWC7A1Fnk"
bot = telegram.Bot(token)
public_chat_name = "@ktest2022"

def job():
    now = time .localtime()
    text = f"current time = {0}".format(str(now))
    bot.sendMessage(chat_id = public_chat_name, text = "alarm").chat_id
    # print("current time = ", str(now))

schedule.every(1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

# # id_channel = bot.sendMessage(chat_id = public_chat_name, text = "alarm").chat_id
# print(id_channel)




import schedule
import time
import telegram
token = "5759317578:AAHB10nZxKvOzsBJBw8aBlWamsMWC7A1Fnk"
bot = telegram.Bot(token = token)
chat_id = "5776108466"

def job():
    now = time .localtime()
    text = f"current time = {0}".format(str(now))
    bot.sendMessage(chat_id=chat_id, text=text)
    # print("current time = ", str(now))

schedule.every(1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)