# bot = telebot.TeleBot('5485915394:AAEzU-jJOV7JlUIsSDF4H88nJeXFV6eAiZY')
import telebot
import sys
import mymodule
from telebot import types

#глобальные переменный для работы с данными
test_id = ""
global test2
un_id = 0
const = 0
glob_lat = 0
glob_long = 0


bot = telebot.TeleBot('5582565908:AAH67yJGGhA68f_7b-Gq-alaNr5rGR__vXA')  # Токен бота
user_dict = {}  # {1234567890: {'photo': photo_id, 'caption': some_text}}


    # ------------------------------------------НАЧАЛО РАБОТЫ БОТА, МЕНЮ----------------------------------------------------------

@bot.message_handler(commands=['start'])
def welcome(message):
    # Клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создание фундамента клавиатуры
    driver = types.KeyboardButton("🚘 Driver")  # Создание кнопки
    footer = types.KeyboardButton("🧍🏻 Footer")  # Создание кнопки

    markup.add(driver, footer)  # В фундамента клавиатуры добавляются кнопки
    bot.send_message(message.chat.id, "We Apologize Greatly\nMost of ours buttons works only after you would push them second time\n")
    bot.send_message(message.chat.id, "􀌤 Welcome,{0.first_name}!\nI'm a <b>{1.first_name}</b>,"
                                      "bot designed to help you find a parking spot.\nPlease,choose your role:"
                     .format(message.from_user, bot.get_me()), parse_mode='html',
                     reply_markup=markup)  # Бот выводит сообщение с определенным форматом


@bot.message_handler(content_types=['text'])
def action(message):
    # Клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создание фундамента клавиатуры

    Button_parking_search = types.KeyboardButton(text="Parking search")  # Создание кнопки
    Button_refresh_geo = types.KeyboardButton(text="Refresh Geo")

    Button_Driver_Manual = types.KeyboardButton("Driver Manual")  # Создание кнопки
    Button_Ped_Manual = types.KeyboardButton("Pedestrian Manual")  # Создание кнопки
    Back_To_Menu = types.KeyboardButton("↩︎ Back to menu")  # Создание кнопки

    # Button_Take_A_Picture = types.KeyboardButton('Submit a parking photo')  # Создание кнопки\
    
    Driver = types.KeyboardButton("🚘 Driver")  # Создание кнопки
    Footer = types.KeyboardButton("🧍🏻 Footer")  # Создание кнопки

    if message.chat.type == 'private':  # Если личный чат (Бота и человека) 1 на 1
        if message.text == '🚘 Driver':  # Если прожата данная кнопка


            # переменные id и driver нужны для функций
            us_id = message.from_user.id
            s = 'Driver'
            mymodule.proverka_id(uid=us_id)  # проверка id
            mymodule.update_status(uid=us_id, st=s)  # обновление статуса
            mymodule.status_check(uid=us_id, st=s)  # проверка статуса
            markup.add(Button_parking_search, Button_Driver_Manual, Back_To_Menu)  # В фундамента клавиатуры добавляются кнопки
            bot.send_message(message.chat.id, "📝 Please, be careful while driving, select an action:",
                             reply_markup=markup)  # Бот выводит сообщение


        elif message.text == '🧍🏻 Footer':  # Если прожата данная кнопка

            global un_id
            us_id = message.from_user.id
            un_id = us_id
            s = 'Footer'
            mymodule.proverka_id(uid=us_id)  # проверка id
            mymodule.update_status(uid=us_id, st=s)  # обновление статуса
            mymodule.status_check(uid=us_id, st=s)  # проверка статуса
            mymodule.get_status(uid=us_id)

            markup.add(Button_refresh_geo, Button_Ped_Manual, Back_To_Menu)  # В фундамента клавиатуры добавляются кнопки
            bot.send_message(message.chat.id, "📝 Good walk, select an action:",
                             reply_markup=markup)  # Бот выводит сообщение


            if  message.text == 'Refresh Area':
                
                pass

        # elif message.text == 'Submit a parking photo': #Если прожата данная кнопка
        #     bot.send_message(message.from_user.id, 'Отправьте картинку.') #Бот выводит сообщение
        #     bot.register_next_step_handler(message, photo_handler) #Следующий шаг,вызывается функция photo_handler

        elif message.text == '↩︎ Back to menu':  # Если прожата данная кнопка
            markup.add(Driver, Footer)  # В фундамента клавиатуры добавляются кнопки
            bot.send_message(message.chat.id, "📝 You moved back to <b>menu</b>."
                                              "\n\nPlease, select an action:", parse_mode="html",
                             reply_markup=markup)  # Бот выводит сообщение
        elif message.text == 'Parking search':

            sendto = types.ForceReply(selective=False)
            msg = bot.send_message(message.chat.id,
                                   "Select Radius of Search Circle\nFor example if you input one of these numbers:\n Введи 0.001 чтобы посчитало расстояние между намиы\n2 = 3km-radius\n4 = 1.5km-radius\nBe careful you need to input numbers not a radius", reply_markup=sendto)  # Присвоение переменной функции вывода


            bot.register_next_step_handler(msg, test)  # Ждет сообщения от пользователя и вызывает функцию тест
        elif message.text == 'Refresh Geo':


            mss = bot.send_message(message.chat.id,"Please Share Your Location")
            
            bot.register_next_step_handler(mss, ff)
        elif message.text == "Inactive":
            mss = bot.send_message(message.chat.id, "Search Stopped")
            bot.register_next_step_handler(mss, stop_search)
        
        elif message.text == "Driver Manual":
            bot.send_message(message.chat.id,"<b>Driver Manual</b>\n1.Press button <b>Parking Search</b> if you want to find a place for your car\n2.Lately you need to input a <b>NUMBER</b> for define in which size of radius we'll gonna search for a place\n1=6km\n2=3km\n3=1.5km\nBe careful you need to input <b>NUMBER</b> not a radius or words\4.Send geo - on this step you will send you're location\n5. JUST WAIT\nWe're doing our best to find you best place for parking\nWith love bonch.team"
            .format(message.from_user, bot.get_me()), parse_mode='html')
        
        elif message.text == "Pedestrian Manual":
            bot.send_message(message.chat.id,"<b>Pedestrian Manual</b>\n1.Press button Refresh Geo twice to share you're location with us\n2.Press <b>Send Geo</b> to share your location with us\n3.After you've shared if there are exsist driver around you\nYou will get offer and options to chose Accept/Decline\n4.After Accepting offer you need to take a shot of parking place or upload a photo from your library then add small description which will help driver to find this parking place\n<b>Important</b>: You have button <b>Inactive</b> after you end your offer or if you want to end session you<b>MUST</b> press this button twice or else you'll get a lot of spam\nwith love bonch.team".format(message.from_user, bot.get_me()), parse_mode='html')




@bot.message_handler(content_types=["text"])
def stop_search(message):
    message = bot.send_message(message.chat.id, text="Bye-Bye")

    mymodule.unvailable(uid=un_id)

@bot.message_handler(content_types=["text"])
def test(message):

    constant = message.text # присвоение текста от пользователя переменной
  
    global const
    const = float(constant)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    Button_parking_search = types.KeyboardButton(text="Send geo", request_location=True)
    markup.add(Button_parking_search)
    bot.send_message(message.chat.id, 'OK', reply_markup=markup)  # Бот выводит сообщение

@bot.message_handler(commands=['ped'])
def ff(message):
    con = message.text

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Button_Inactive = types.KeyboardButton(text="Inactive")
    Button_refresh_geo= types.KeyboardButton(text="Send Geo", request_location=True )
    markup.add(Button_refresh_geo, Button_Inactive)
    bot.send_message(message.chat.id, 'OK', reply_markup=markup)

    
@bot.message_handler(content_types=["location"])
def location(message):
    uid = message.from_user.id
    if mymodule.get_status(uid=uid) == "Driver":
        bot.send_message(message.chat.id, "Идет поиск...")
        if message.location is not None:  # Если локация есть
            global glob_lat
            global glob_long

            print(message.location)  # Вывод строки
            print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))  # Вывод строки

        #------------------------------------------ПРИНЯТИЕ ГЕОДАННЫХ АВТОМОБИЛИСТА----------------------------------------------------------

            Baz_Latitude_Avto = message.location.latitude  # Latitude нашей гоепозиции
            Baz_Longitude_Avto = message.location.longitude  # Longitude нашей гоепозиции

            glob_lat = (Baz_Latitude_Avto)
            glob_long = (Baz_Longitude_Avto)

              # ID чобы передать локацию конкретного пользователя
            mymodule.update_location(uid=uid, lat=Baz_Latitude_Avto, lon=Baz_Longitude_Avto)  # функция заполнения данных в ячейку юзеры поля геолокации
            flist = []  # название листа не важно можно сделать другой
            mymodule.transition(dri="Footer", lll=flist)  # функция перевода данных из БД в лист
            print(flist)

        #------------------------------------------ПЕРЕМЕННЫЕ-КОНСТАНТЫ----------------------------------------------------------

            const_Tochka__Max_latitude = 6.66  # Константное расстояние отклонения от нашей геопозции до latitude при 0,001 градусах
            const_Tochka_Max_longitude = 6.78  # Константное расстояние отклонения от нашей геопозции до longitude при 0,001 градусах

            global const
            Vo_Skolko_Raz_Um_Radius = const  # Пользователь указывает во - сколько раз уменьшить радиус до latitude/longitude

            Korrektirovka_Gorizontali = 4  # Корректировка горизонатльных отклонений относительно расстояний радиусов вертикальных отклонений

            Pogreshost_Lat = 0.0016667223 # Погрещность latitude

            Pogreshost_Long = 0.0032819739 # Погрешность longitude

            Const_S_zona = 180.6192 # Константное значение площади зоны при 0,001 градусах

            Gradus = 0.001

        # ---------------------------ПОИСК latitude И longitude ВЕРТИКАЛЬНЫХ И ГОРИЗОНТАЛЬНЫХ ОТКЛОНЕНИЙ, СОЗДАНИЕ ЗОНЫ АВТОМОБИЛИСТА--------------------------------------------------

            Vverh_Tochka__Max_latitude = Baz_Latitude_Avto + ((Baz_Latitude_Avto * Gradus) / Vo_Skolko_Raz_Um_Radius)  # Latitude точки вертикального верхнего отклонения

            print("Vverh_Tochka__Max_latitude: ", Vverh_Tochka__Max_latitude)  # latitude точки верхнего отклонения
            print("Vverh_Tochka_Max_longitude: ", Baz_Longitude_Avto)  # longitude точки верхнего отклонения

            Vniz_Tochka__Max_latitude = Baz_Latitude_Avto - ((Baz_Latitude_Avto * Gradus) / Vo_Skolko_Raz_Um_Radius)  # Latitude точки вертикального нижнего отклонения

            print("Vniz_Tochka__Max_latitude: ", Vniz_Tochka__Max_latitude)  # latitude точки нижнего отклонения
            print("Vniz_Tochka_Max_longitude: ", Baz_Longitude_Avto)  # longitude точки нижнего отклонения

            Vpravo_Tochka__Max_longitude = Baz_Longitude_Avto + (((Baz_Longitude_Avto * Gradus) * Korrektirovka_Gorizontali) / Vo_Skolko_Raz_Um_Radius)  # Latitude точки горизонтального правого отклонения

            print("Vniz_Tochka__Max_latitude: ", Baz_Latitude_Avto)  # latitude точки правого отклонения
            print("Vniz_Tochka_Max_longitude: ", Vpravo_Tochka__Max_longitude)  # longitude точки правого отклонения

            Vlevo_Tochka__Max_longitude = Baz_Longitude_Avto - (((Baz_Longitude_Avto * Gradus) * Korrektirovka_Gorizontali) / Vo_Skolko_Raz_Um_Radius)  # Latitude точки горизонтального левого отклонения

            print("Vniz_Tochka__Max_latitude: ", Baz_Latitude_Avto)  # latitude точки левого отклонения
            print("Vniz_Tochka_Max_longitude: ", Vlevo_Tochka__Max_longitude)  # longitude точки левого отклонения

            Vverh_Tochka__Max_latitude_Pogr_Plus = Vverh_Tochka__Max_latitude
            Vverh_Tochka__Max_latitude_Pogr_Plus = Vverh_Tochka__Max_latitude_Pogr_Plus + ((Pogreshost_Lat * Vverh_Tochka__Max_latitude_Pogr_Plus) / 100)  # Отклонение Latitude точки вертикального верхнего отклонения с погрешностью вверх
            print("Vverh_Tochka__Max_latitude_Pogr: ", Vverh_Tochka__Max_latitude_Pogr_Plus)

            Vniz_Tochka__Max_latitude_Pogr_Minus = Vniz_Tochka__Max_latitude
            Vniz_Tochka__Max_latitude_Pogr_Minus = Vniz_Tochka__Max_latitude_Pogr_Minus - ((Pogreshost_Lat * Vniz_Tochka__Max_latitude_Pogr_Minus) / 100)  # Отклонение Latitude точки вертикального нижнего отклонения с погрешностью вниз
            print("Baz_Latitude_Pogr_Minus: ", Vniz_Tochka__Max_latitude_Pogr_Minus)

            Vpravo_Tochka__Max_longitude_Pogr_Plus = Vpravo_Tochka__Max_longitude
            Vpravo_Tochka__Max_longitude_Pogr_Plus = Vpravo_Tochka__Max_longitude_Pogr_Plus + ((Pogreshost_Long * Vpravo_Tochka__Max_longitude_Pogr_Plus) / 100)  # Отклонение Latitude точки горизонтального правого отклонения с погрешностью вправо
            print("Baz_Longitude_Pogr_Plus: ", Vpravo_Tochka__Max_longitude_Pogr_Plus)

            Vlevo_Tochka__Max_longitude_Pogr_Minus = Vlevo_Tochka__Max_longitude
            Vlevo_Tochka__Max_longitude_Pogr_Minus = Vlevo_Tochka__Max_longitude_Pogr_Minus - ((Pogreshost_Long * Vlevo_Tochka__Max_longitude_Pogr_Minus) / 100)  # Отклонение Latitude точки горизонтального левого отклонения с погрешностью влево
            print("Baz_Longitude_Pogr_Minus: ", Vlevo_Tochka__Max_longitude_Pogr_Minus)

        # ----------------------------------------------------ХАРАКТЕРИСТИКИ СОЗДАННОЙ ЗОНЫ------------------------------------------------------------------------------------------

            S_Zona = Const_S_zona / (Vo_Skolko_Raz_Um_Radius * 2)

            print("S_Zona: ", S_Zona, " km")  # Площадь созданной зоны

            Radius_Vverh_Vniz = const_Tochka__Max_latitude / Vo_Skolko_Raz_Um_Radius # Нахождение вертикального радиуса
            Radius_Vlevo_Vpravo = const_Tochka_Max_longitude / Vo_Skolko_Raz_Um_Radius # Нахождение горизонтального радиуса

            print("Vertical radius value: ", Radius_Vverh_Vniz, " km")  # Вертикальный радиус зоны
            print("Gorizontal radius value: ", Radius_Vlevo_Vpravo, " km")  # Горизонтальный радиус зоны

            # ------------------------------------------ПРОВЕРКА ВХОДА ТОЧКИ ПЕШЕХОДА В ЗОНУ АВТОМОБИЛИСТА---------------------------------------
            
            counts = len(flist)
            
            true = 0;
            false = 0;
            count = 0

      
            for count in range(counts):
                
                if((flist[count][1] < Vverh_Tochka__Max_latitude) and (flist[count][1] > Vniz_Tochka__Max_latitude)):
                    #goes to the next checkpoint
                    
                    pass
                elif not ((flist[count][1] < Vverh_Tochka__Max_latitude) and (flist[count][1] > Vniz_Tochka__Max_latitude)):
                    if ((flist[count][1] < Vverh_Tochka__Max_latitude_Pogr_Plus) and (flist[count][1] > Vniz_Tochka__Max_latitude_Pogr_Minus)):
                       
                        pass
                        #goes to the next point
                    else :
                        #marker unusable
                        
                        flist[count].insert(3, 'unusable')
                        pass
                        continue

                        
                if((flist[count][2] > Vlevo_Tochka__Max_longitude) and (flist[count][2] < Vpravo_Tochka__Max_longitude)): 
                    flist[count].insert(3, 'usable')
                   
                    pass
                elif not ((flist[count][2] > Vlevo_Tochka__Max_longitude) and (flist[count][2] < Vpravo_Tochka__Max_longitude)): 
                    if((flist[count][2] > Vlevo_Tochka__Max_longitude_Pogr_Minus) and (flist[count][2] < Vpravo_Tochka__Max_longitude_Pogr_Plus)):
                        

                        flist[count].insert(3, 'unusable')
                        #marker Usable
                    else:
                       
                        #marker unusable
                        flist[count].insert(3, 'unusable')
                        continue
            check = 0

            for i in range(counts):
                if flist[i][3] == "unusable":
                    check += 1
                  

            if check == counts:
                bot.send_message(message.chat.id, "There is none pedestrians around which would fit to your necessaries")

            
        # ------------------------------------------ОТПРАВКА ЗАПРОСА ОТ АВТОМОБИЛИСТА ПЕШЕХОДУ----------------------------------------------------------
            
              # Вводится id пользователя,которому отправляется геопозиция водителя (ID Пешехода)
            markup = types.InlineKeyboardMarkup(row_width=2)
            Button_Yes = types.InlineKeyboardButton("Yes", callback_data='yes')  # В зависимости нажатия, вызывается Yes
            Button_No = types.InlineKeyboardButton("No", callback_data='no')  # В зависимости нажатия, вызывается No
            markup.add(Button_Yes, Button_No)  # В макет добавляются кнопки
            global test2
            test2 = message.chat.id
            for i in range(counts):
                if flist[i][3] == "usable":
                    second_id = flist[i][0]
                    bot.send_location(second_id, message.location.latitude, message.location.longitude)  # Бот пересылает сообщение
                    bot.send_message(second_id, "Accept request ⬆️ ?",
                                    reply_markup=markup)  # Бот пересылает сообщение с запросом принятия заявки (Да/нет)


                else:
                    continue
    else:
        Baz_Latitude_Peshehod = message.location.latitude  # Latitude нашей гоепозиции
        Baz_Longitude_Peshehod = message.location.longitude
        print("Данные пешехода", Baz_Latitude_Peshehod, Baz_Longitude_Peshehod)
        mymodule.update_location(uid=uid, lat=Baz_Latitude_Peshehod, lon=Baz_Longitude_Peshehod)
    # ------------------------------------------ОБРАТНАЯ СВЯЗЬ, ОТВЕТ ПЕШЕХОДА НА ЗАПРОС АВТОМОБИЛИСТА----------------------------------------------------------

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global test2
    main_id = test2 # Мой ID Водителя

    try:
        if call.message:
            # Отправляем Водителю ответ на заявку
            if call.data == 'yes':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Отправьте фото", reply_markup=None)  # Заменяем InLine кнопки на текст
                bot.register_next_step_handler(call, photo_handler)  # Следующий шаг,вызывается функция photo_handler
            elif call.data == 'no':
                bot.send_message(main_id, 'Ваша заявка отклонена')  # Отправляем Водителю ответ

            # Заменяем InLine кнопки на текст
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Запрос отклонен",
                                  reply_markup=None)

            # Уведомление, не знаю пока как реализовать, оставил так
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Вы отклонили запрос")

    except Exception as e:
        print(repr(e))


    # ------------------------------------------ПЕШЕХОД ОТПРАВЛЯЕТ ФОТО С ТЕКСТОМ АВТОМОБИЛИСТУ----------------------------------------------------------

@bot.message_handler(content_types=["photo"])
def photo_handler(message):

    try:
        # если изображение есть в словаре - заменяем его и убираем описание
        if user_dict.get(message.chat.id) is not None:
            user_dict[message.chat.id]['photo'] = message.photo[len(message.photo) - 1].file_id
            user_dict[message.chat.id]['caption'] = ''

        else:
            # если фото нет - создаем словарь и добавляем изображение
            user_dict[message.chat.id] = {'photo': '', 'caption': ''}
            user_dict[message.chat.id]['photo'] = message.photo[len(message.photo) - 1].file_id
    except Exception as e:
        bot.reply_to(message, e)
    else:
        bot.send_message(message.chat.id, 'Теперь введите текст к картинке')  # Бот выводит сообщение
        bot.register_next_step_handler(message, text_handler)  # Следующий шаг,вызывается функция text_handler


def text_handler(message):
    global test2
    main_id = test2
    global glob_lat
    global glob_long

    glob_lat = str(glob_lat)+" "+str(glob_long)
    # добавляем описание изображения фото в словарь
    user_dict[message.chat.id]['caption'] = message.text

    #us_id = message.from_user.id
    #main_id = us_id  # Вводится id пользователя,которому отправляется фото (ID Водителя)
    bot.send_photo(
        main_id,
        photo=user_dict[message.chat.id]['photo'],  # Фото
        caption=user_dict[message.chat.id]['caption'],  # Подпись

        parse_mode='HTML'
    )
    bot.send_message(main_id, text="Location"+" "+glob_lat)
    bot.send_message(message.chat.id, 'Ваше фото успешно отправлено')  # Бот выводит сообщение


bot.polling(none_stop=True, interval=0)








