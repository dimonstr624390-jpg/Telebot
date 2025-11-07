import telebot
import time
import threading
import schedule
import random
from logic import gen_pass, ran_em, cflip

bot = telebot.TeleBot("TOKEN GOES HERE")

@bot.message_handler(commands=['start'])
def send_hello(message):
    bot.reply_to(message, "Привет! Для большей онформации введите команду /list или /help.")

@bot.message_handler(commands=['list', 'help'])
def send_welcome(message):
    bot.reply_to(message, '''
Команды: 
/hello - Приветствие
/bye - Прощание
/password - Генератор пароля
/emoji - Случайный эмодзи
/coin - Подбросить монетку
/timer - Информация о таймере
/set - Установить таймер
/unset - Остановить таймер
''')

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['password'])
def send_password(message):
    bot.reply_to(message, gen_pass(12))

@bot.message_handler(commands=['emoji'])
def send_emoji(message):
    bot.reply_to(message, ran_em())

@bot.message_handler(commands=['coin'])
def send_coin(message):
    result = cflip() 
    bot.reply_to(message, result)

@bot.message_handler(commands=['timer'])
def send_timer_help(message):
    bot.reply_to(message, "Привет! Используй /set <seconds> , чтобы создать таймер.")

def beep(chat_id) -> None:
    bot.send_message(chat_id, text='Таймер сработал!')

@bot.message_handler(commands=['set'])
def set_timer(message):
    args = message.text.split()
    if len(args) > 1 and args[1].isdigit():
        sec = int(args[1])
        schedule.every(sec).seconds.do(beep, message.chat.id).tag(message.chat.id)
        bot.reply_to(message, 'Таймер установлен!')
    else:
        bot.reply_to(message, 'Использование: /set <seconds>')

@bot.message_handler(commands=['unset'])
def unset_timer(message):
    schedule.clear(message.chat.id)
    bot.reply_to(message, 'Все таймеры остановлены!')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

def schedule_runner():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    scheduler_thread = threading.Thread(target=schedule_runner, daemon=True)
    scheduler_thread.start()
    
    print("Бот запущен...")
    bot.infinity_polling(skip_pending=True)
