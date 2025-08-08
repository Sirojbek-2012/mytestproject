from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

photos = {
    "1": "1.jpg",
    "2": "2.jpg",
    "3": "3.jpg",
    "4": "4.jpg",
    "5": "5.jpg",
    "6": "6.jpg",
    "7": "7.jpg",
    "8": "8.jpg",
    "9": "9.jpg",
    "10": "10.jpg",
    "11": "11.jpg"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot ishlayapti. 1 dan 11 gacha raqam yuboring. men sizga rasm yuboraman")

async def send_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text in photos:
        with open(photos[text], 'rb') as photo:
            await update.message.reply_photo(photo)
    else:
        await update.message.reply_text("Iltimos, 1 dan 10 gacha bo‘lgan raqam yuboring.")

app = ApplicationBuilder().token("7985769835:AAEA9BKjbobOdyb_8goV3IGPxpBmT2NtGbw").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_photo))
print("ishladi")
app.run_polling()
