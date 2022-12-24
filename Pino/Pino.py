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

# List-Kelas
@Pinobot.message_handler(commands=['list-kelas'])
def list_kelas(message):
    user_id = message.chat.id
    sql.execute("SELECT chat_id FROM bot_admins WHERE chat_id = {}".format(user_id))
    result = sql.fetchone()
    print(result)
    if(result):
        sql.execute("SELECT * FROM kelas")
        result = sql.fetchall()
        final = ''        
        for data in range (len(result)):
                final = final + str(data+1) + '.)' + 'Kelas : ' + str(result[data][1]) + '\n     ' + 'Nama Grup : ' + str(result[data][2]) + '\n     ' + 'Wali Kelas : ' + str(result[data][3]) + '\n     ' + 'ID Telegram  : ' + str(result[data][4]) + '\n' + '\n'
        # print(final)
        Pinobot.reply_to(message, "Berikut Adalah List Kelas Yang Terdaftar Di Pino Bot :\n\n" + final)
    else :
        Pinobot.reply_to(message, "Anda Belum Terdaftar Sebagai Admin\nHubungi @lumi_novry")

# List-Guru
@Pinobot.message_handler(commands=['list-guru'])
def list_kelas(message):
    user_id = message.chat.id
    sql.execute("SELECT chat_id FROM bot_admins WHERE chat_id = {}".format(user_id))
    result = sql.fetchone()
    print(result)
    if(result):
        sql.execute("SELECT * FROM gurus")
        result = sql.fetchall()
        final = ''        
        for data in range (len(result)):
                final = final + str(data+1) + '.)' + 'NIP : ' + str(result[data][1]) + '\n     ' + 'Nama : ' + str(result[data][2]) + '\n     ' + 'E-Mail : ' + str(result[data][4]) + '\n     ' + 'No.Telp  : ' + str(result[data][5]) + '\n     ' + 'Jenis-Kelamin : '+ str(result[data][6]) + '\n' + '\n'
        # print(final)
        Pinobot.reply_to(message, "Berikut Adalah List Guru Yang Terdaftar Di Pino Bot :\n\n" + final)
    else :
        Pinobot.reply_to(message, "Anda Belum Terdaftar Sebagai Admin\nHubungi @lumi_novry")

# Absensi 
@Pinobot.message_handler(commands=['check-absensi'])
def check_absensi(message):
    user_id = message.chat.id
    sql.execute("SELECT chat_id FROM bot_admins WHERE chat_id = {}".format(user_id))
    result = sql.fetchone()
    print(result)
    if(result):
        texts = message.text.split(' ')
        kelas = str(texts[1])
        kelas = kelas.replace('-',' ')
        mapel = str(texts[2])
        mapel = mapel.replace('-',' ')
        tanggal = str(texts[3])
        sql.execute("SELECT absen_siswas.tanggal, absen_siswas.keterangan, gurus.name, siswas.nama_siswa, kelas.kelas, mapels.pelajaran FROM absen_siswas INNER JOIN gurus ON absen_siswas.guru_id=gurus.id INNER JOIN siswas ON absen_siswas.siswa_id=siswas.id INNER JOIN kelas ON absen_siswas.kelas_id=kelas.id INNER JOIN mapels ON absen_siswas.mapel_id=mapels.id WHERE tanggal LIKE '%{}%' AND kelas.kelas LIKE '%{}%' AND mapels.pelajaran LIKE '%{}%'".format(tanggal, kelas, mapel))
        result = sql.fetchall()
        if(result):
            detail = result[0]
            tanggal_absen = detail[0]
            nama_guru = detail[2]
            mapel = detail[5]
            final = ''        
            for data in range (len(result)):
                final = final + str(data+1) + '.)' + str(result[data][3]) + ' : ' + str(result[data][1]) + '\n'
            print(final)
            pesan_balasan = "Detail Absensi :\nTanggal : {}\nGuru : {}\nMata Pelajaran : {}\n==================\nDaftar Absensi Siswa:\n{}".format(tanggal_absen, nama_guru, mapel, final)
            Pinobot.reply_to(message, pesan_balasan)
        else: 
            Pinobot.reply_to(message, "Data Tidak Ditemukan")
    else :
        Pinobot.reply_to(message, "Anda Belum Terdaftar Sebagai Admin\nHubungi @lumi_novry")

# Absensi 
@Pinobot.message_handler(commands=['check-absensi-alpha'])
def check_absensi(message):
    user_id = message.chat.id
    sql.execute("SELECT chat_id FROM bot_admins WHERE chat_id = {}".format(user_id))
    result = sql.fetchone()
    print(result)
    if(result):
        texts = message.text.split(' ')
        kelas = str(texts[1])
        kelas = kelas.replace('-',' ')
        mapel = str(texts[2])
        mapel = mapel.replace('-',' ')
        tanggal = str(texts[3])
        sql.execute("SELECT absen_siswas.tanggal, absen_siswas.keterangan, gurus.name, siswas.nama_siswa, kelas.kelas, mapels.pelajaran FROM absen_siswas INNER JOIN gurus ON absen_siswas.guru_id=gurus.id INNER JOIN siswas ON absen_siswas.siswa_id=siswas.id INNER JOIN kelas ON absen_siswas.kelas_id=kelas.id INNER JOIN mapels ON absen_siswas.mapel_id=mapels.id WHERE tanggal LIKE '%{}%' AND kelas.kelas LIKE '%{}%' AND mapels.pelajaran LIKE '%{}%' AND absen_siswas.keterangan NOT IN ('Hadir')".format(tanggal, kelas, mapel))
        result = sql.fetchall()
        if(result):
            detail = result[0]
            tanggal_absen = detail[0]
            nama_guru = detail[2]
            mapel = detail[5]
            final = ''        
            for data in range (len(result)):
                final = final + str(data+1) + '.)' + str(result[data][3]) + ' : ' + str(result[data][1]) + '\n'
            print(final)
            pesan_balasan = "Detail Absensi :\nTanggal : {}\nGuru : {}\nMata Pelajaran : {}\n==================\nDaftar Absensi Siswa:\n{}".format(tanggal_absen, nama_guru, mapel, final)
            Pinobot.reply_to(message, pesan_balasan)
        else: 
            Pinobot.reply_to(message, "Data Tidak Ditemukan")
    else :
        Pinobot.reply_to(message, "Anda Belum Terdaftar Sebagai Admin\nHubungi @lumi_novry")

# Keep Update
Pinobot.polling(none_stop=True)