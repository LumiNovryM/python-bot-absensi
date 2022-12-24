import Server
import Database
from Api import Adminbot
from datetime import date, datetime
# Database Setup
db = Database.db
sql = db.cursor()



# Bot Command
# Start Server & Database
@Adminbot.message_handler(commands=['start'])
def start(message):
    Adminbot.send_chat_action(message.chat.id, 'typing')
    if(message.chat.id == 1789786125):
        Server.runXampp()
        Adminbot.reply_to(message, "Starting Apache...\nStarting MySQL...\nBot Sudah Terkoneksi Ke Server & Database")
    else :
        Adminbot.reply_to(message, "Command Ini Hanya Untuk Developer\nDeveloper Saya Adalah @lumi_novry")

# Stop Server & Databse 
@Adminbot.message_handler(commands=['stop'])
def stop(message):
    Adminbot.send_chat_action(message.chat.id, 'typing')
    if(message.chat.id == 1789786125):
        Server.stopXampp()
        Adminbot.reply_to(message, "Stopping Apache...\nStopping MySQL...\nBot Memutuskan Koneksi Ke Server & Database")
    else :
        Adminbot.reply_to(message, "Command Ini Hanya Untuk Developer\nDeveloper Saya Adalah @lumi_novry")

# Start Pino Bot
@Adminbot.message_handler(commands=['start-pino'])
def start_pino(message):
    Server.runPino()
    Adminbot.send_message(message, "Pino Bot Start")

# Profile
@Adminbot.message_handler(commands=['profile'])
def profile(message):
    nama = message.from_user.first_name
    id = message.from_user.id
    Adminbot.reply_to(message, "Berikut Profile Telegram Kamu : \nUsername Telegram : {}\nID Telegram : {}".format(nama, id))

# Daftar 
@Adminbot.message_handler(commands=['daftar'])
def daftar(message):
    user_id = message.chat.id
    sql.execute("SELECT chat_id FROM admin WHERE chat_id = {}".format(user_id))
    result = sql.fetchone()
    print(result)
    if(result):
        print("Data Ada")
        if user_id in result:
            Adminbot.reply_to(message, "Anda Sudah Terdaftar Menjadi Admin")
    else:
        print("Data Kosong Then Daftar")
        texts = message.text.split(' ')
        chat_id = message.chat.id
        nama = texts[1]
        nama = nama.replace('-', ' ')
        email = texts[2]
        status = texts[3]
        tanggal = datetime.now()
        tanggal = tanggal.strftime("%d/%m/%y, %H:%M:%S")
        # Setup Query
        insert = "INSERT INTO admin(chat_id, nama, email, status, tanggal) VALUES(%s,%s,%s,%s,%s)"
        val = (chat_id, nama, email, status, tanggal)
        sql.execute(insert, val)
        db.commit()
        Adminbot.reply_to(message, "Pendaftaran Berhasil\nSekarang Anda Adalah Admin")


# Keep Update
Adminbot.polling()