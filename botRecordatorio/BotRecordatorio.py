
#'6047868660:AAFR9wJxAjKe92hWCumCix7gmK8fMI2-jDs'
import telebot
import datetime
import time

# reemplazar el valor de token con el que recibiste de BotFather
TOKEN = '6047868660:AAFR9wJxAjKe92hWCumCix7gmK8fMI2-jDs'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def responder_mensaje(message):
    # Obtener el texto del mensaje recibido
    texto = message.text

    # Responder con un mensaje que incluya el texto recibido
    bot.send_message(message.chat.id, f'Recibido: {texto}')

@bot.message_handler(commands=['recordar'])
def programar_recordatorio_telegram(message):
    # Obtener el mensaje enviado por el usuario
    mensaje = message.text

    # Dividir el mensaje en sus componentes
    partes = mensaje.split()

    # Obtener la fecha, hora y mensaje del recordatorio
    fecha = partes[1]
    hora = partes[2]
    mensaje = ' '.join(partes[3:])

    # Convertir la hora del recordatorio en un objeto datetime
    hora_dt = datetime.datetime.strptime(hora, '%H:%M')

    # Crear un objeto datetime combinando la fecha y hora del recordatorio
    fecha_hora = datetime.datetime.strptime(fecha + ' ' + hora_dt.strftime('%H:%M'), '%d/%m/%Y %H:%M')

    # Obtener la fecha y hora actuales
    ahora = datetime.datetime.now()

    # Calcular la cantidad de segundos entre la fecha/hora actual y la del recordatorio
    segundos = (fecha_hora - ahora).total_seconds()

    # Esperar la cantidad de segundos necesarios
    if segundos > 0:
        time.sleep(segundos)

        # Enviar un mensaje de recordatorio
        bot.send_message(message.chat.id, mensaje)

        # Responder con un mensaje de confirmación
        bot.send_message(message.chat.id, f'Recordatorio programado para el {fecha} a las {hora} con el mensaje "{mensaje}"')
    else:
        bot.send_message(message.chat.id, 'La fecha y hora del recordatorio deben ser posteriores a la hora actual.')

bot.polling()

