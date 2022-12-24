import mysql
import mysql.connector
import telebot
from Api import Pinobot

# Database Setup
# Database Setup
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_absensi'
)
sql = db.cursor()

# Check If Admin Bot Command Work Successfully
print("Pino Bot Running Successfully")

# Bot Command
@Pinobot.message_handler(commands=['start'])
def start(message):
    Pinobot.reply_to(message, "Halo👋!  Saya Pino Yang Akan Membantu Kegiatan Layanan Informasi Pendidikan SMK Taruna Bhakti")



# Keep Update
Pinobot.polling(none_stop=True)