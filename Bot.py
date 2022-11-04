import telebot
from telebot import types
from datetime import datetime as dt
import complex as opCom
import rational as oprat


API_TOKEN="5685436926:AAGExvN7xReI2ehQvnV9HILo_E3yBXAhXek"
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Калькулятор запущен')
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Комплексные числа"))
    markup.add(types.KeyboardButton("Рациональные числа"))
    bot.send_message(message.chat.id,'С какими числами будем работать:',reply_markup=markup)

@bot.message_handler(func= lambda message: message.text =='Комплексные числа' or message.text =='/complex')
def message_co(message):
    bot.send_message(message.from_user.id, 'Введите первое комплексное число по образцу: 2 + 5i')
    bot.register_next_step_handler(message, message_co1)
    global idCom
    idCom=message.chat.id
    print(message.chat.id)

def message_co1(message):
    global user_komplex1
    user_komplex1 = message.text

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("+"))
    markup.add(types.KeyboardButton("-"))
    markup.add(types.KeyboardButton("/"))
    markup.add(types.KeyboardButton("*"))

    bot.send_message(message.from_user.id, 'Выберите действие',reply_markup=markup)
    bot.register_next_step_handler(message, message_co2)

def message_co2(message):
    global operation
    operation = message.text
    bot.send_message(message.from_user.id, 'Введите второе комплексное число по образцу: 2 + 5i')
    bot.register_next_step_handler(message, message_co3)

def message_co3(message):
    global user_komplex2
    user_komplex2 = message.text
    insert_rec()
    compl()
    print(*resCom)
    bot.send_message(message.from_user.id, f'*Ответ: {"".join(resCom)}*', parse_mode= 'Markdown')

def insert_rec():
    # Функция записывает введенные данные пользователя
    time = dt.now().strftime('%d.%m.%Y %H:%M:%S')
    with open('results.json', 'a') as data:
        data.write(f'{time} {idCom} : ({user_komplex1}){operation}({user_komplex2}) = ')
    data.close()



def compl():
    operands = [user_komplex1, user_komplex2, operation]
    global resCom
    if operands[2] == "+":
        resCom=opCom.record_in_file(opCom.addition(opCom.take_rational_part(operands[0]),
                                            opCom.take_symbol(operands[0]),
                                            opCom.take_imaginary_part(operands[0]),
                                            opCom.take_rational_part(operands[1]),
                                            opCom.take_symbol(operands[1]),
                                            opCom.take_imaginary_part(operands[1])))
    elif operands[2] == "-":
        resCom=opCom.record_in_file(opCom.deduction(opCom.take_rational_part(operands[0]),
                                             opCom.take_symbol(operands[0]),
                                             opCom.take_imaginary_part(operands[0]),
                                             opCom.take_rational_part(operands[1]),
                                             opCom.take_symbol(operands[1]),
                                             opCom.take_imaginary_part(operands[1])))
    elif operands[2] == "*":
        resCom=opCom.record_in_file(opCom.multiply(opCom.take_rational_part(operands[0]),
                                            opCom.take_symbol(operands[0]),
                                            opCom.take_imaginary_part(operands[0]),
                                            opCom.take_rational_part(operands[1]),
                                            opCom.take_symbol(operands[1]),
                                            opCom.take_imaginary_part(operands[1])))
    else:
        resCom=opCom.record_in_file(opCom.division(opCom.take_rational_part(operands[0]),
                                            opCom.take_symbol(operands[0]),
                                            opCom.take_imaginary_part(operands[0]),
                                            opCom.take_rational_part(operands[1]),
                                            opCom.take_symbol(operands[1]),
                                            opCom.take_imaginary_part(operands[1])))
    print('dfg', resCom)


@bot.message_handler(func= lambda message: message.text =='Рациональные числа' or message.text =='/rational')

def message_vid(message):
    bot.send_message(message.from_user.id, 'Введите первое число с плавающей точкой:')
    bot.register_next_step_handler(message, message_re)
    global idRat
    idRat = message.chat.id
    print(message.chat.id)
def message_re(message):
    global firstnum
    firstnum = message.text
    print("1", firstnum)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("+")), markup.add(types.KeyboardButton("-"))
    markup.add(types.KeyboardButton("/")), markup.add(types.KeyboardButton("*"))

    bot.send_message(message.from_user.id, 'Выберите действие', reply_markup=markup)
    bot.register_next_step_handler(message, message_reply2)

def message_reply2(message):
    global operat
    operat = message.text
    print("2", operat)
    bot.send_message(message.from_user.id, 'Введите второе число с плавающей точкой:')
    bot.register_next_step_handler(message, message_re2)

def message_re2(message):
    global secondnum
    secondnum = message.text
    print(secondnum)
    asd = oprat.mainterminal(firstnum, operat, secondnum, idRat)
    print('asd', asd)
    bot.send_message(message.from_user.id, f'*Ответ: {asd}*', parse_mode= 'Markdown')


bot.infinity_polling()