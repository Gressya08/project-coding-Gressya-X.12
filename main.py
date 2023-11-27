from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

token = "6707090884:AAGqMoNwgTssFxRFn331-43BBcUkROlPhTk"
username_bot = "@gsyyaaa_bot"

async def start_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(' Gunakan /help untuk menampilkan apa yang dapat saya berikan.. ')

async def help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Kirim pesan, bot akan membalas pesan..')

async def text_message( update : Update, context : ContextTypes.DEFAULT_TYPE ):
    text_diterima : str = update.message.text
    print( "Text diterima : ", text_diterima)

    if 'hallo' in text_diterima:
        await update.message.reply_text('Hallo juga...')
    elif 'selamat malam' in text_diterima:
        await update.message.reply_text('Selamat malam juga')
    elif 'siapa kamu?' in text_diterima:
        await update.message.reply_text('Saya adalah bot...')
    else:
        await update.message.reply_text('Saya tidak mengerti')

async def error( update : Update, context : ContextTypes.DEFAULT_TYPE ):
    print(f"Error... : {context.error}")

if __name__ == '__main__':
    print('Mulai')

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler ('start', start_command ))
    app.add_handler(CommandHandler ('help', help_command ))

    app.add_handler(MessageHandler(filters.TEXT, text_message))

    app.add_error_handler(error)

    app.run_polling(poll_interval=1)