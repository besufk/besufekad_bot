import telebot
from telebot import types

# ቶከንህን እዚህ ጋር አስገባ
API_TOKEN = '9132489288:AAFb0MUNW8EdiQEZ0uZ5eL5mxKns-Gr5jwg'

bot = telebot.TeleBot(API_TOKEN)

# 1. /start ወይም /help ሲሉ የሚሰጥ ምላሽ
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🛠️ አገልግሎቶች')
    btn2 = types.KeyboardButton('📍 አድራሻ')
    btn3 = types.KeyboardButton('🗺️ የካርታ አድራሻ')
    btn4 = types.KeyboardButton('ℹ️ ስለ እኛ')
    btn5 = types.KeyboardButton('📞 አግኙን')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    
    welcome_text = (
        f"ሰላም {message.from_user.first_name}! እንኳን ወደ በሱፍቃድ አጠቃላይ ኤሌክትሮኒክስ ጥገና በደህና መጡ።\n\n"
        "እባክዎ ከታች ካሉት አማራጮች የሚፈልጉትን ይምረጡ፦"
    )
    
    bot.reply_to(message, welcome_text, reply_markup=markup)

# 2. ተጠቃሚው የሚልካቸውን ጽሁፎች እና በተኖች መቀበያ
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    text = message.text
    
    if text == '🛠️ አገልግሎቶች':
        bot.send_message(
            message.chat.id, 
            "🛠️ **የምንሰጣቸው አገልግሎቶች፡**\n\n"
            "• የቲቪ  📺\n"
            "• የጂፓስ 🧭\n"
            "• የስፒከር  🔊\n"
            "• የሚክሰር  🎚️\n"
            "• የአምፕሊፋየር  🎛️\n"
            "• የኮምፒውተር 💻\n"
            "• የስልክ ጥገና 📱\n"
            "• እና ሌሎች የኤሌክትሮኒክስ ጥገናዎች በአስተማማኝ ሁኔታ እንጠግናለን!"
        )
        
    elif text == '📍 አድራሻ':
        bot.send_message(
            message.chat.id, 
            "📍 **አድራሻችን፡**\n"
            "አዳማ፣ አመዴ ግብርና ፊት ለፊት\n"
            "በሱፍቃድ አጠቃላይ ኤሌክትሮኒክስ ጥገና ዎርክሾፕ"
        )
        
    elif text == '🗺️ የካርታ አድራሻ':
        bot.send_message(
            message.chat.id, 
            "🗺️ **የዎርክሾፓችን የጉግል ማፕ አድራሻ፦**\n\n"
            "በዚህ ሊንክ በመጫን በቀጥታ ማግኘት ይችላሉ፦\n"
            "👉 https://maps.app.goo.gl/qfMS3EsB9ofRid8g8"
        )
        
    elif text == 'ℹ️ ስለ እኛ':
        bot.send_message(
            message.chat.id, 
            "ℹ️ **ስለ እኛ፡**\n"
            "በሱፍቃድ አጠቃላይ ኤሌክትሮኒክስ ጥገና - ሁሉንም ዓይነት የኤሌክትሮኒክስ እቃዎች ጥራት ባለበት እና በአስተማማኝ ሁኔታ እንጠግናለን።"
        )
        
    elif text == '📞 አግኙን':
        bot.send_message(
            message.chat.id, 
            "📞 **ለማግኘት እና ለመደወል፦**\n\n"
            "ስልክ ቁጥር፦ 0913433294\n"
            "አድራሻችን፦ አዳማ፣ አመዴ ግብርና ፊት ለፊት\n"
            "በደስታ እናስተናግዳለን!"
        )
        
    else:
        bot.reply_to(
            message, 
            "መልዕክትዎ ደርሶናል። ከታች ካሉት አማራጮች አንዱን በመጫን ወይም ጥያቄዎን በግልፅ በመጻፍ ይተባበሩን!"
        )

print("ቦቱ በአዲስ መልክ ስራ ጀምሯል...")
bot.infinity_polling()
