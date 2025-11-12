import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv

load_dotenv()

async def start(update, context):
    await update.message.reply_text('سلام! بات فعال شد 🚀')

async def echo(update, context):
    await update.message.reply_text(f'شما گفتید: {update.message.text}')

def main():
    TOKEN = os.getenv('BOT_TOKEN')
    
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("🚀 بات در حال اجرا...")
    app.run_polling()

if __name__ == '__main__':
    main()
