import telebot
from config import TOKEN
from owasp_parse import get_top10, get_top_title, about, get_donate_link, get_contact

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['top'])
def answer_top(message):
    top10 = get_top10()
    answer = f'{get_top_title()}\n\n'
    for item in top10:
        answer += f'{item["title"]} \nLink: {item["link"]}\n\n'
    bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['about'])
def answer_about(message):
    bot.send_message(message.chat.id,  about())

@bot.message_handler(commands=['donate'])
def answer_donate(message):
    answer = f'You can make a donation to the OWASP project using the link: {get_donate_link()}'
    bot.send_message(message.chat.id,  answer)

@bot.message_handler(commands=['contact'])
def answer_contact(message):
    address = get_contact()
    answer = ''
    for item in address:
        answer += f'{item["point"]}\n{item["address"]}'
        answer += "-" * 40 + '\n'
    bot.send_message(message.chat.id, answer)

if __name__ == '__main__':
    bot.polling()