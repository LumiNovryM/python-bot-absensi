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
    Adminbot.send_chat_action(message.chat.id, 'typing')
    if(message.chat.id == 1789786125):
        Adminbot.reply_to(message, "Pino Bot Start\nKunjungi @starbhak_pino_bot")
        Server.runPino()
    else :
        Adminbot.reply_to(message, "Command Ini Hanya Untuk Developer\nDeveloper Saya Adalah @lumi_novry")

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
    sql.execute("SELECT chat_id FROM bot_admins WHERE chat_id = {}".format(user_id))
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
        insert = "INSERT INTO bot_admins(chat_id, nama, email, status, tanggal) VALUES(%s,%s,%s,%s,%s)"
        val = (chat_id, nama, email, status, tanggal)
        sql.execute(insert, val)
        db.commit()
        Adminbot.reply_to(message, "Pendaftaran Berhasil\nSekarang Anda Adalah Admin")

# List Admin
@Adminbot.message_handler(commands=['list-admin'])
def list_admin(message):
    sql.execute("SELECT * FROM bot_admins")
    result = sql.fetchall()
    print(result)
    final = ''
    for data in range (len(result)):
                final = final + str(data+1) + '.)' + 'ID Telegram : ' + str(result[data][0]) + '\n     ' + 'Nama : ' + str(result[data][1]) + '\n     ' + 'E-Mail : ' + str(result[data][2]) + '\n     ' + 'Status : ' + str(result[data][3]) + '\n     ' + 'Tanggal Pendaftaran : ' + str(result[data][4]) + '\n' + '\n'
    print(final)
    Adminbot.reply_to(message, "Berikut Adalah List Admin Yang Terdaftar Di Pino Bot :\n\n" + final)

# Keep Update
Adminbot.polling()