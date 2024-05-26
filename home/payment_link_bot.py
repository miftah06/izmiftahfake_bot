import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Aktifkan", callback_data='enable')],
        [InlineKeyboardButton("Nonaktifkan", callback_data='disable')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Halo! Klik tombol di bawah untuk mengaktifkan atau menonaktifkan link.', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data

    if data == 'enable':
        # Kode untuk mengaktifkan fungsi blokir_nonaktif
        query.answer("Link berhasil diaktifkan!")
    elif data == 'disable':
        # Kode untuk menonaktifkan fungsi blokir_nonaktif
        query.answer("Link berhasil dinonaktifkan!")

def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    # Tambahkan handler command /start
    dispatcher.add_handler(CommandHandler('start', start))

    # Tambahkan handler CallbackQuery
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()