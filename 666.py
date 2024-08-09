
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Define the /pr command handler
def pr(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    admins = context.bot.get_chat_administrators(chat_id)
    admin_names = [admin.user.first_name for admin in admins]
    mention_admins = ', '.join([f"@{name}" for name in admin_names])
    update.message.reply_text(f"Admins in this chat: {mention_admins}")

# Define the /request command handler
def request(update: Update, context: CallbackContext):
    update.message.reply_text("5")

# Set up the bot
updater = Updater("YOUR_BOT_TOKEN")
dispatcher = updater.dispatcher

# Add command handlers
dispatcher.add_handler(CommandHandler("pr", pr))
dispatcher.add_handler(CommandHandler("request", request))

# Start the bot
updater.start_polling()
updater.idle()