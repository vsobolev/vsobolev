import os
import requests
#import telebot
import wget
import logging
#import aiogram
from aiogram import Bot, Dispatcher, executor, types
#from aiogram import FSInputFile

logging.basicConfig(level=logging.INFO)

token = '1457669053:AAHHfEhi9RYudegV2xGjuWOKHnWBn2oiqLs'

bot = Bot(token)
dp = Dispatcher(bot)
# num = 0
scilink = 'http://sci-hub.do/'


@dp.message_handler()
async def echo(message: types.Message, chat_id: object = None):
    """
message: Message,
               chat_id: object = None) -> Coroutine[Any, Any, Optional[Any]]
    :type chat_id: object
    """
    #await message.reply(message.text)
    chat_id = message.chat.id
    # @bot.message_handler(content_types=["text"])
    # def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    global urlx
    #print(message.text)
    if 'doi:' in message.text:
        message.text = message.text[4:]
    elif 'doi: ' in message.text:
        message.text = message.text[5:]
    if 'DOI:' in message.text:
        message.text = message.text[4:]
    elif 'DOI: ' in message.text:
        message.text = message.text[5:]
    if 'Doi:' in message.text:
        message.text = message.text[4:]
    elif 'Doi: ' in message.text:
        message.text = message.text[5:]
    #print(message.text)
    url = str(scilink) + str(message.text)
    response = requests.get(url)  # get-запрос
    longcodepage = response.text
    x = None
    longcodepagesplit = longcodepage.split('"')
   # print (longcodepagesplit)
    for i in longcodepagesplit:
        if 'location.href' in i:
            x = i
        #    print(x)  # строка с кодом и мишурой найдена
         #   x = str(x)
        else:
            continue
    if "location.href='//" in x:
        urlx = x[17: -15: 1]  # чистая прямая ссылка
     #   print(urlx)
    elif "location.href='" in x:
        urlx = x[15: -15: 1]  # чистая прямая ссылка
      #  print(urlx)
    else:
        print('У нас ошибка')
    #urly='https://'+ urlx
    wget.download(urlx, 'article.pdf')


    fileart = open('article.pdf', 'rb')
    #Message = await SendDocument(fileart)
    #await bot.send_document(chat_id=chat_id, document='article.pdf')
    #filearticle = FSInputFile(message.text +'.pdf', filename='article.pdf')
    #print (filearticle)
    await bot.send_document(chat_id, document=fileart)
    #document = 'C:/Users/BrainLaptop/PycharmProjects/SciDownBot2.0/article.pdf'
    #text_file = BufferedInputFile(b"Hello, world!", filename="article.pdf")
    #Bot.send_document(chat_id, fileart)

    os.remove('article.pdf')
 #   await asyncio.sleep(delay)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
# except: pass
