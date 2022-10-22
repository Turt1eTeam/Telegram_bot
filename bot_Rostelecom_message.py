from email import message
import psycopg2
from telebot import types
import telebot
import config as cf
from time import sleep

print('TOKEN:',cf.TOKEN)
bot = telebot.TeleBot(cf.TOKEN)
get_id=''
all_text=[]
all_text1=""
id_t =""
k=0

wellcome_text='Привет, <b>{0.first_name}</b>! Я - <b>{1.first_name}</b> одноименной команды <b>Turt1e Team</b>. Я Телеграм-Бот👾, созданый для того чтобы <b>помогать людям</b>, а именно <b>отслеживать их задания</b>. Рад быть полезным!👌'
my_func="Мой функционал:\n/help - вывести панель инструментов;\n/about - немного информации обо мне и команде;\n/set_work - запрос вашего ID;\n/get_work - получение заданий с учетом Вашего ID;"
my_team="Turt1e Team - команда интузиастов, состоящая из 3-х четверокурсников и 2-х третикурсников. Ну,а я удобный инструмент в руках моих создателей!"



def post_query(get_id):
        connection = psycopg2.connect(user="postgres", password="12345678",host="127.0.0.1",port="5432",database="user_work")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from user_id where id = "+str(get_id)+";"
        cursor.execute(postgreSQL_select_Query)
        software_records = cursor.fetchall()
        for row in software_records:
            if(row[0]== "" or row[0]== " " ):
                error()
                break
            else:
               all_text.append(row)
            
          
def error(message):
     bot.send_message(message.chat.id,"Ошибочный индекс!")
     print('ERORS')


def about(message):
    bot.send_message(message.chat.id,my_team)
   

def wellcome(message):
    bot.send_message(message.chat.id,wellcome_text.format(message.chat,bot.get_me()),parse_mode="html")
    bot.send_message(message.chat.id,my_func)
    

def go_get(message,id_t):
    print('Выполнился1!')
    get_id = str(message.text)
    d_t = False
    print('Выполнился2!')


@bot.message_handler(commands=['start'])
def event(message):
    wellcome(message)

@bot.message_handler(commands=['help'])
def event(message):
    bot.send_message(message.chat.id,my_func)

@bot.message_handler(commands=['about'])
def event(message):
    bot.send_message(message.chat.id,my_team)

@bot.message_handler(commands=['set_work'])
def event(message):
    bot.send_message(message.chat.id,'Введите ваш ID: ')
    id_t = True

@bot.message_handler(commands=['get_work'])
def event(message):   
    for i in range(3):
        all_text1 = 'Ваш ID: '+str(all_text[i][0])+'\nВаша задача: '+str(all_text[i][1])+'\nВаши действия: '+str(all_text[i][2])+'\nВаши сроки: '+str(all_text[i][3])
    #print(all_text1)
        bot.send_message(message.chat.id,all_text1)
   

@bot.message_handler(content_types=['text'])
def event(message):
    go_get(message,id_t)
    post_query(message.text)
   
        



    
   


bot.polling(none_stop=True)