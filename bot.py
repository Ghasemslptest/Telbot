import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# تنظیمات لاگ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# دستور استارت
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('🎉 سلام! بات فعال شد!\n\n'
                                  'دستورات موجود:\n'
                                  '/start - نمایش این پیام\n'
                                  '/help - راهنما\n'
                                  'پیام معمولی - بات جواب میده')

# دستور کمک
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('💡 راهنمای بات:\n'
                                  'این یک بات تستی هست\n'
                                  'هر پیامی بفرستی جوابت رو میده!')

# پاسخ به پیام‌های معمولی
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    user_name = update.message.from_user.first_name
    
    # پاسخ هوشمند
    if 'سلام' in user_message:
        response = f'سلام {user_name}!
عزیزم چطوری؟ 😊'
    elif 'چطوری' in user_message:
        response = f'عالیم {user_name} ممنون! تو چطوری? 🌟'
    elif 'خداحافظ' in user_message:
        response = f'خداحافظ {user_name}!
موفق باشی! ✨'
    else:
        response = f'سلام {user_name}!
پیامت رو دریافت کردم: "{user_message}"\n'
                   'چطور می‌تونم کمک کنم? 🤔'
    
    await update.message.reply_text(response)

# مدیریت خطا
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.error(f'خطا: {context.error}')

def main():
    # توکن بات رو از متغیر محیطی بگیر
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    
    if not BOT_TOKEN:
        print("❌ خطا: BOT_TOKEN تنظیم نشده!")
        return
    
    # ساخت اپلیکیشن
    app = Application.builder().token(BOT_TOKEN).build()
    
    # اضافه کردن هندلرها
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # هندلر خطا
    app.add_error_handler(error_handler)
    
    # اجرای بات
    print("🚀 بات تلگرام در حال اجرا...")
    app.run_polling()

if __name__ == '__main__':
    main()
