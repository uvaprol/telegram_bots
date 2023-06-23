import telebot
from time import sleep as sleep
from random import randint as rd
bot = telebot.TeleBot('https://t.me/BotFather')
name = ''
surname = ''
age = 0
kms = ('/stone', '/scisor', '/paper')
count = 3
comand = ''


@bot.message_handler(content_types=['text'])
def start_game(message):
    if message.text == '/game' or message.text == '/new_game':
        global count
        global comand
        comand = '\n\nЧто делать?\n/go_to_sleep\n/go_to_panel'
        count = 3
        bot.send_message(message.from_user.id, f"Вы очнулись в неизвестной для вас комнате. Перед вами пульт с кнопочками и лампочками.{comand}")
        bot.register_next_step_handler(message, beyond_of_earth)
    else:
        bot.send_message(message.from_user.id, 'Чтобы начать игру нажмите\n/game')
def beyond_of_earth(message):
    global count
    global comand
    print(message.text)
    print(message.from_user.id)
    if message.text == '/go_to_sleep':
        bot.send_message(message.from_user.id, 'Вы уснули...')
        sleep(1)
        bot.send_message(message.from_user.id, f'...Через не которое время вы опять проснулись.\nСнова эта кномната.{comand}')
        bot.register_next_step_handler(message, beyond_of_earth)
    elif message.text == '/go_to_panel':
        comand = '\n\nЧто дальше?\n/wath_visor\n/pushing_on_buttom'
        bot.send_message(message.from_user.id, f'Перед вами небольшой экранчик, куча кнопочек и лампочек.{comand}')
        bot.register_next_step_handler(message, beyond_of_earth)
    elif message.text == '/pushing_on_buttom' or message.text == '/pushing_on_buttom':
        bot.send_message(message.from_user.id,'Кажется кто-то летит не туда!!!\nЖизнь страшная шутка.')
        sleep(1)
        bot.send_message(message.from_user.id, 'Вы умерли от голода в просторах бесконечного космоса...\n/new_game')
    elif message.text == '/wath_visor':
        comand = '\n\nЧто делать?\n/open_directory\n/pushing_on_buttom'
        bot.send_message(message.from_user.id, f'Вы видите кучу файлов,и вдруг ваш взгляд останавливается на папкe "Return to Earth"{comand}')
        bot.register_next_step_handler(message, beyond_of_earth)
    elif message.text == '/open_directory':
        comand = '\n\n\n/stone\n/scisor\n/paper'
        bot.send_message(message.from_user.id, 'Вы нашли инструкцию по возвращению на землю.')
        sleep(1)
        bot.send_message(message.from_user.id, f'Чтоб активировать автопилот победите Компухтер в stone, scisor...\nУ вас есть {count} попытки!{comand}')
        bot.register_next_step_handler(message, beyond_of_earth)
    elif message.text == '/stone' or message.text == '/scisor' or message.text == '/paper':
        if message.text == kms[rd(0,2)]:
            bot.send_message(message.from_user.id, 'Ура летим на землю!')
            sleep(3)
            bot.send_message(message.from_user.id, '...Несколько лет спустя...\n...Дом!- милый дом!\n\n/new_game')
        elif count == 1:
            bot.send_message(message.from_user.id, 'ERROR!\nУвы система заблокирована!..')
            sleep(2)
            bot.send_message(message.from_user.id, '...Вы замерзли в космосе...\n\n/new_game')
        else:
            count -= 1
            bot.send_message(message.from_user.id, f'ERROR\nУ вас есть {count} попытки!{comand}')
            bot.register_next_step_handler(message, beyond_of_earth)
    else:
        bot.send_message(message.from_user.id, comand)
        bot.register_next_step_handler(message, beyond_of_earth)





bot.polling(none_stop=True, interval=0)


