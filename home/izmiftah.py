import asyncio
import csv
import datetime
import json
import keyword as acak
import logging
import os
import random
import sqlite3
import subprocess
import threading
import time

import openai
import requests
import telebot
from bs4 import BeautifulSoup
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from tqdm import tqdm

from nulis1 import generate_keywords_pdf_pdfkit, generate_keywords_pdf_fpdf, generate_keywords_pdf_reportlab

from dotenv import load_dotenv

load_dotenv('.env')
TOKEN = os.getenv('token')
passnya = os.getenv('password')
# Load environment variables from .env
api_key = os.getenv('openai')
# Ganti dengan token bot Telegram Anda
API_KEY = '46198aef1648f472d'
keywords_list = []
bot = telebot.TeleBot(TOKEN)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
email_kamu = os.getenv('email') #tolong modifikasi se>
openai.api_key = api_key
admin = os.getenv('idtelegram')
link_jualan = os.getenv('link')
google_apikey = 'AIzaSyCfEbq1hzg3wjnUhq_3-skMnRlWb5MVeX4'
openai.api_key = api_key
api_key_path = 'api.json'
# dapatkan di https://t.me/username_to_id_bot
### JANGAN DI UBAH #####
# ini penentu jumlah jumlah_koinny
# tolong sesuaikan
# Menggunakan nilai jumlah_jumlah_koin untuk menginisialisasi jumlah_credit
# Mengubah nilai jumlah_credit menjadi -1 (jika itu yang Anda inginkan)
### JANGAN DI UBAH #####
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
global jumlah_credit
jumlah_koin_awal = 0  # ini penentu jumlah jumlah_koinnya secara terbalik
jumlah_koin = 15 --15
jumlah_kredit = 0 # ini
# ini penentu jumlah jumlah_koinny
# Inisialisasi variabel-variabel
credit = jumlah_koin_awal
isi_jumlah_koin = +jumlah_koin_awal # tolong sesuaikan
# Menggunakan nilai jumlah_jumlah_koin untuk menginisialisasi jumlah_credit
# Mengubah nilai jumlah_credit menjadi -1 (jika itu yang Anda inginkan)
credit_jumlah_koin = 1  # Ini penentu jumlah jumlah_koinnya
jumlah_koinnya = 10 + jumlah_koin
isi_saldo = jumlah_koinnya
jumlah_jumlah_koin = 15 + +jumlah_koin_awal
saldo_nol = 15
saldonya = saldo_nol
credit_saldo = jumlah_koin_awal
saldo = 100
new_saldo = jumlah_koin_awal
# Inisialisasi identitas
identitas = "mif , seorang peneliti yang penuh dengan rasa penasaran"
midtrans_url = 'https://api.sandbox.midtrans.com/v1/payment-links'
# Fungsi untuk mengambil jawaban dari OpenAI
# Fungsi lainnya dan pengaturan bot dapat dipertahankan
# Handle Command /start
# Diubah menjadi jumlah_koin awalnya
# Variabel jumlah_koin_awal seharusnya dideklarasikan tanpa "global" karena ini adalah variabel biasa
### JANGAN DI UBAH #####
########### UBAH di bagian passnya UNTUK NGATUR
## dan jangan sekali kali ubah baris "Jumlah saldo Anda: " di skrip ini:
# Membuat dictionary passwords untuk menyimpan kata sandi pengguna
# Menonaktifkan pengecekan thread untuk melakukan reset

passwords = {
    5596779909 : '1',
    867977312  : '2',
}

# Data saldo pengguna (contoh data dummy)
saldo_pengguna = {
    'user1': 100,
    'user2': 200,
    'user3': 300,
    '867977312'  : 10000,
}
# Inisialisasi variabel-variabel

# dan jangan sekali kali ubah baris "Jumlah saldo Anda: " di skrip ini:
passnya = 'isi passwordnya di sini!!'
file_skrip = 'skrip.txt'
keyword1_skrip = 'fitur.txt'
keyword2_skrip = 'objek.txt'

# Inisialisasi identitas
identitas = "mif , seorang peneliti yang penuh dengan rasa penasaran"
midtrans_url = 'https://api.sandbox.midtrans.com/v1/payment-links'

# Fungsi lainnya dan pengaturan bot dapat dipertahankan
# Handle Command /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    pengguna = message.from_user.username
    result = inisial
    # If User Doesn't Exist, Insert into Database
    if chat_id:
        bot.send_message(chat_id, f"Welcome back, {pengguna}!")
        record_unblocked_user(id, saldo, jumlah_koin, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, new_saldo, account, koin_awal, account_number, balance)
    if blokir_nonaktif(message):
        unblock_user(id)
        bot.send_message(chat_id, f"Anda sudah terblokir silahkan buka dengan /bukablokir")
        if record_unblocked_user:
            bot.send_message(chat_id, f"Anda sudah terblokir silahkan buka dengan /bukablokir dengan passswirdnya")
    if result:
        bot.send_message(chat_id, "Selamat datang di AI bot buatan saya. silahkan ketik /help atau silakan pilih menu yang tersedia:", reply_markup=main_menu_markup())
    else:
        bot.send_message(chat_id, "Selamat datang di AI bot buatan saya. silahkan ketik /help atau silakan pilih menu yang tersedia:", reply_markup=main_menu_markup())

def generate_ngrok_link(file):
    # Start a local server using PHP built-in web server
    server_process = subprocess.Popen(["/usr/bin/php", "-S", "localhost:880", "-t", f"web/"])

    # Wait for ngrok to generate the public link (you can use Ngrok API/Library to automate this part)
    # Assuming ngrok link is generated as "http://123abc.ngrok.io"
    ngrok_link = f"{link_jualan}"

    # Stop the local server and ngrok
    server_process.terminate()
    return ngrok_link

def generate_payment_link():
    # Generate ngrok link for index.php
    ngrok_link = generate_ngrok_link("web/akun.php")
    payment_link = f"{ngrok_link}/payment.php"
    return payment_link

def test_generate_payment_link():
    payment_link = generate_payment_link()
    assert payment_link == f"{payment_link}"

def send_payment_button_to_user(link):
    # Send Telegram message with payment button
    # Include link in the button
    test_generate_payment_link()

def get_tokenmu_input_from_user(message):
    # Send a message to the user via Telegram
    chat_id = message.from_user
    bot.send_message(message.chat.id, "Please enter your token:")
    token = message.text
    return token

def validate_tokenmu(token):
    # Validate token logic
    with open('/root/izmiftah/web/izmiftah123.json') as f:
        data = json.load(f)
        if token == data['token']:
            nominal = 5000
            return True

def run_command_hidden(message):
    if message.text.startswith("topup "):
        password = f"{passnya}"
        if message.text.split()[1] == password:
            # Run command without user seeing it
            print("Command executed successfully")
        else:
            print("Invalid password, command not executed")
    elif message.text.startswith("payment "):
        password = f"{passnya}"
        if message.text.split()[1] == password:
            # Run command without user seeing it
            print("Command executed successfully")
        else:
            print("Invalid password, command not executed")
    else:
        print("Unknown command")

def bayar_telebot(message):
    chat_id = message.chat.id  # Menggunakan ID obrolan dari pesan yang diterima
    # Generate payment button link
    payment_link = generate_payment_link()

    # Send payment button to user
    send_payment_button_to_user(message.chat.id)

    # Get token input from user
    tokenmu = get_tokenmu_input_from_user(message)

    if validate_tokenmu(tokenmu):
        global saldo_pengguna, new_saldo, jumlah_koin
        saldo_pengguna += 100
        new_saldo = saldo_pengguna
        jumlah_koin += 50
        run_command_hidden(message)


# Handler untuk pesan "bayar" dengan parameter nominal
@bot.message_handler(func=lambda message: message.text.lower().startswith('/bayar'))
def verify_payment(message):
    handle_start(message)
    # Parsing nominal pembayaran dari pesan
    tokenmu = get_tokenmu_input_from_user(message)
    nominal = 0
    # Simulasi verifikasi pembayaran
    if nominal == '5000':
        # Pembayaran berhasil
        bot.reply_to(message, "Pembayaran sebesar {} berhasil.".format(nominal))
    # Validate token
    elif validate_tokenmu(tokenmu):
        run_command_hidden(message)
        bot.send_message(message.chat.id, text="Top up berhasil.")
    else:
        # Pembayaran gagal
        bayar_telebot(message)


@bot.message_handler(func=lambda message: message.text.lower().startswith('/pembayaran'))
def handle_pembayaran(message):
    pengguna = message.chat.id
    result = inisial
    bayar_telebot(message)
    if result != pengguna:
        bot.send_message(message.chat.id, "Selamat datang di izmiftah bot")
        url = bot.send_message(message.chat.id, text="bot terblokir silahkan buka dengan /bukablokir")

        # Jika user_id belum terdaftar, minta pembayaran dan buat tombol pembayaran
        # Fungsi untuk menambahkan pengguna baru ke tabel users
        conn = sqlite3.connect('izmiftah.db')
        c = conn.cursor()
        conn.commit()
        conn.close()

    # Data for the transaction
    order_id = f"izmiftah1bulanpremium-{timestamp}"
    gross_amount = '5000'

    # Set up Midtrans client configuration
    detail_transaksi = {
        "order_id": order_id,
        "gross_amount": gross_amount
    }
    url = "https://api.sandbox.midtrans.com/v1/payment-links"

    payload = {
        "transaction_details": {
            "order_id": "izmiftah1102920809",
            "gross_amount": 5000
        },
        "usage_limit": 100000
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Basic U0ItTWlkLXNlcnZlci02ZlQxdWNGU1RrdVN4cWloZG9BNzJMSVM6U0ItTWlkLWNsaWVudC1rc084TmxsOGU0TDN5VmhT"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)
    # Generate payment URL
    # Get the payment URL
    payment_link = response.text
    tokenmu = get_tokenmu_input_from_user(message)
    # Add cancel button for payment
    cancel_button = InlineKeyboardButton("Cancel", callback_data=pengguna)
    keyboard = InlineKeyboardMarkup().add(cancel_button)
    bot.send_message(message.chat.id, f"Anda belum terdaftar, Silakan melakukan verifikasi dengan mengetik /pembayaran lalu ketik /bayar atau di sini : {link_jualan}")
    if result == 0:
        bayar_telebot(message)
        get_tokenmu_input_from_user(message)
    elif validate_tokenmu(tokenmu):
        run_command_hidden(message)
        global jumlah_kredit, jumlah_koin
        jumlah_koin += 100
        bot.send_message(message.chat.id, text="Top up berhasil.")
    else:
        get_tokenmu_input_from_user(message)


def verify_payment_status(message):
    # Lakukan validasi status pembayaran melalui integrasi dengan sistem pembayaran (misalnya, API atau database)
    # Jika pembayaran sudah diverifikasi
    if make_payment:
        order_id = requests.POST.get('order_id')
        if order_id not in inisial:
            bot.send_message(message.chat.id, f"Pembayaran dengan id {order_id} telah diverifikasi")
        else:
            bot.send_message(message.chat.id, f"Pembayaran dengan id {order_id} belum diverifikasi")
    # Jika pembayaran belum diverifikasi
    else:
        order_id = requests.POST.get('order_id')
        if order_id not in inisial:
            bot.send_message(message.chat.id, f"Pembayaran dengan id {order_id} belum diverifikasi")
        else:
            bot.send_message(message.chat.id, f"Pembayaran dengan id {order_id} telah diverifikasi")


def handle_message(order_id, message):
    check_payment_status(order_id)
    if verify_payment_status(order_id):
        bot.send_message(message.chat.id, f" pembayaran dengan id {order_id} telah berhasil")


def payment_successful(order_id, db, message):
    # Ambil data order dari database berdasarkan order_id
    order = db.get_order(order_id)  # fungsi db.get_order merupakan fungsi untuk mengambil data order dari database

    # Kirim email konfirmasi pembayaran kepada pengguna
    bot.send_message(message.chat.id, 'Pembayaran Berhasil', 'Terima kasih atas pembayaran Anda.')

    # Update status pembayaran menjadi 'failure' pada database
    db.update_payment_status(order_id, 'failure')

    # Tampilkan pesan gagal
    print(f"Pembayaran untuk order {order_id} gagal.")

    if payment_successful:
        global new_saldo, jumlah_koin
        new_saldo += 15
        jumlah_koin += -25
        bot.send_message(message.chat.id, text=" saldo telah terisi kembali")
        bot.send_message(message.chat.id, text="Pembayaran berhasil. Anda mendapatkan 15 saldo tambahan.")
    else:
        bot.send_message(message.chat.id, text="Pembayaran gagal. Silakan coba lagi.")

        # Fungsi untuk menambahkan fitur pembayaran otomatis
def automatic_payment(message):
    # Implementasikan logika pembayaran otomatis di sini
    # Misalnya, Anda dapat menjalankan fungsi process_payment secara otomatis jika saldo habis
    pass
# Fungsi untuk melakukan pembayaran
def process_payment(message):
    # Implementasikan logika pembayaran melalui e-wallet Indonesia di sini
    # Jika pembayaran berhasil, tambahkan 15 saldo
    # Jika pembayaran gagal, berikan pesan error
    # Gantilah dengan logika sesuai kebutuhan

    if payment_successful:
        global new_saldo, jumlah_koin
        new_saldo += 15
        jumlah_koin -= 25
        bot.send_message(message.chat.id, text=" saldo telah terisi kembali")
        bot.send_message(message.chat.id, text="Pembayaran berhasil. Anda mendapatkan 15 saldo tambahan.")
    else:
        bot.send_message(message.chat.id, text="Pembayaran gagal. Silakan coba lagi.")

# Fungsi untuk menambahkan fitur pembayaran otomatis
def automatic_payment(message):
    # Implementasikan logika pembayaran otomatis di sini
    # Misalnya, Anda dapat menjalankan fungsi process_payment secara otomatis jika saldo habis
    pass

# Fungsi untuk mengirim pesan dengan format tertentu
# Fungsi untuk mengirim pesan ke Telegram
def send_telegram_message(message):
    if is_blokir_active(message):
        bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi lebih dari 0 saldo\n lakukan /payment atau /topup terlebih dahulu .")
        handle_pembayaran(message)
        # Mengubah pengguna secara acak setiap detik
        current_user = change_user(pengguna)
        print(f"Current user: {current_user}")
        # Tunggu selama 1 detik
        time.sleep(1)
    params = {
        "chat_id": message.chat.id,
        "text": message
    }
    url = f"https://api.telegram.org/{TOKEN}/sendMessage"
    response = requests.post(url, params=params)
    if response.status_code == 200:
        raise Exception(f"Failed to send message to Telegram bot: {response.text}")


def main_menu_markup():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(types.KeyboardButton('/ai halo'), types.KeyboardButton('/write'), types.KeyboardButton('/topup'), types.KeyboardButton('/payment'), types.KeyboardButton('/quiz'))
    return keyboard

# Fungsi untuk melakukan logging
def change_user(pengguna):
    return random.choice(pengguna)

# Daftar pengguna
users = ['user1', 'user2', 'user3', 'user4', 'user5']
def format_timestamp(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

# Fungsi untuk melakukan logging

def logging_action(username):
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    logging.info(f'{current_time} - {username} melakukan logging')

# Contoh penggunaan logging
anu_user = {
    format_timestamp(time.time()): None
}
username = list(anu_user.keys())
inisial = ':' in username
userini = logging.info(username)
chat = userini
saldo_baru = ''
koin = ''
history = ''
additional_input = ''
account = ''
koin_awal = ''
saldo_awal = ''
saldo_awal_nol = ''
account_number = ''
balance = ''
blocked_users = inisial
pengguna = userini in username
oknum = bool(bool(blocked_users))
getpass = requests.get('http://t.me/replace{oknum}'.format(oknum=oknum))
# Setup Database
conn = sqlite3.connect('absensi.db')
cur = conn.cursor()

def block_user(user_id):
    # Koneksi ke database
    conn = sqlite3.connect('izmiftah.db')
    cursor = conn.cursor()

    # Mengecek apakah pengguna sudah diblokir sebelumnya
    cursor.execute("SELECT * FROM izmiftahdatabase WHERE user_id=:id", {'id': user_id})
    is_blocked = cursor.fetchone()

    if is_blocked:
        # Update status blokir pengguna dengan False
        cursor.execute("UPDATE izmiftahdatabase SET is_blocked=0 WHERE user_id=:id", {'id': user_id})
    else:
        # Memasukkan data pengguna baru dengan status blokir False
        cursor.execute("INSERT INTO izmiftahdatabase (user_id, is_blocked) VALUES (?, ?)", (user_id, 0))

    while True:
        # Mengubah pengguna secara acak setiap detik
        current_user = change_user(pengguna)
        print(f"Current user: {current_user}")
        # Tunggu selama 1 detik
        time.sleep(1)

    conn.commit()
    conn.close()


def unblock_user(user_id):
    # Koneksi ke database
    conn = sqlite3.connect('izmiftah.db')
    cursor = conn.cursor()

    # Update status blokir pengguna dengan True
    conn.commit()
    conn.close()

def is_blocked(user_id):
    # Koneksi ke database
    conn = sqlite3.connect('izmiftah.db')
    cursor = conn.cursor()

    # Mengecek status blokir pengguna
    cursor.execute("SELECT is_blocked FROM izmiftahdatabase WHERE user_id=:id", {'id': user_id})
    is_blocked = cursor.fetchone()

    conn.close()

    if is_blocked:
        bool(is_blocked[0])
    else:
        False

def blokir_nonaktif(message):
    # Koneksi ke database
    conn = sqlite3.connect('izmiftah.db')
    cursor = conn.cursor()
    is_not_blocked_user = False
    cursor.execute("SELECT * FROM izmiftahdatabase WHERE user_id=:id", {'id': message.from_user.id})
    # Ambil data blocked_users dari database
    cursor.execute("SELECT * FROM izmiftahdatabase WHERE user_id=:id", {'id': message.from_user.id})
    if new_saldo >= 100:
        unblock_user(id)
        print(f"saldo tambahan: {jumlah_kredit}")
        print(f"Saldo premium: {saldo}")
        print(f"saldo sekedah anda: {jumlah_koin}")
        record_unblocked_user(id, saldo, jumlah_koin, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, new_saldo, account, koin_awal, account_number, balance)


def add_user(self, user_id, saldo):
    self.unblocked_users[user_id] = inisial
    self.saldo_pengguna[user_id] = saldo
    self.unblocked_users[user_id] = saldo

def remove_user(self, user_id):
    if user_id in self.unblocked_users:
        del self.unblocked_users[user_id]

def get_user_saldo(self, user_id):
    if user_id in self.unblocked_users:
        return self.unblocked_users[user_id]
    else:
        None

def create_table():
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS izmiftahdatabase (
                    user_id TEXT PRIMARY KEY,
                    saldo_pengguna INTEGER,
                    jumlah_koin INTEGER,
                    pengguna TEXT,
                    saldo INTEGER,
                    credit INTEGER,
                    saldo_baru  INTEGER,
                    saldo_pengguna_awal INTEGER,
                    jumlah_koin_awal INTEGER,
                    credit_saldo INTEGER,
                    credit_jumlah_koin INTEGER,
                    saldo_nol INTEGER,
                    username TEXT,
                    password INTEGER,
                    koin INTEGER,
                    history INTEGER,
                    additional_input INTEGER,
                    new_saldo INTEGER,
                    account INTEGER,
                    koin_awal INTEGER,
                    saldo_awal INTEGER,
                    saldo_awal_nol INTEGER,
                    saldo_awal_nol_nol INTEGER,
                    saldo_awal_nol_nol_nol INTEGER,
                    account_number INTEGER,
                    balance INTEGER,
                    blocked_users INTEGER)''')
    conn.commit()
    conn.close()
# Koneksi ke database
conn = sqlite3.connect('izmiftah.db')
cursor = conn.cursor()
create_table()

@bot.message_handler(commands=['write'])
def nulis_handle(message):
    def write_file():
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            bot.reply_to(message, "Tulisan sedang dibuat..")

            async def generate_text(keyword_list):
                print("Writing file...")
                for i in tqdm(range(70)):
                    keyword = random.choice(keyword_list)
                    text = f"{keyword}"
                    save_to_file(text)
                    await asyncio.sleep(1)  # Delay 1 second

            def save_to_file(response):
                with open("output.html", "a") as file:
                    file.write(response + "\n")

            keyword_file = open('keyword.txt', 'r')
            keyword_list = keyword_file.read().split("\n")
            keyword_file.close()

            loop.run_until_complete(generate_text(keyword_list))

            bot.send_message(message.chat.id, "Tulisan berhasil dibuat ke output.html\n silahkan lakukan /download_html")

        except KeyboardInterrupt:
            bot.send_message(message.chat.id, "Interrupted while writing")

    thread = threading.Thread(target=write_file)
    thread.start()

# Inisialisasi bot Telegram
def send_payment(user_id, message):
    # Kode untuk mengirim pembayaran
    if new_saldo > 0:
        # Sebuah contoh logika untuk mengirim pembayaran dengan koin
        # Tampilkan pesan bahwa pembayaran berhasil dilakukan
        print("Pembayaran sebesar", jumlah_koin, "koin telah berhasil dikirim.")
        blocked_users()
        record_unblocked_user(id, saldo, jumlah_koin, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, new_saldo, account, koin_awal, account_number, balance)
        send_telegram_message(message.chat.id, f"saldo atau akun belum premium")
    else:
        # Tampilkan pesan jika jumlah_koin kurang dari 1
        print("Jumlah koin harus lebih dari 0.")

# Fungsi untuk memeriksa status pembayaran menggunakan Midtrans
def check_payment_status(order_id):
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Basic U0ItTWlkLXNlcnZlci02ZlQxdWNGU1RrdVN4cWloZG9BNzJMSVM6U0ItTWlkLWNsaWVudC1rc084TmxsOGU0TDN5VmhT"
    }

    params = {
        "order_id": order_id
    }

    response = requests.get(midtrans_url, headers=headers, params=params)
    return response.json()

# Fungsi untuk mencatat izmiftahdatabase ke database
def record_unblocked_user(id, saldo, jumlah_koin, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, new_saldo, account, koin_awal, account_number, balance):
    conn = sqlite3.connect('izmiftah.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS izmiftahdatabase (
                    user_id INTEGER PRIMARY KEY,
                    saldo_pengguna INTEGER,
                    jumlah_koin INTEGER,
                    pengguna INTEGER,
                    saldo INTEGER,
                    credit INTEGER,
                    saldo_baru INTEGER,
                    saldo_nol INTEGER,
                    username INTEGER,
                    koin INTEGER,
                    history TEXT,
                    additional_input INTEGER,
                    new_saldo INTEGER,
                    account INTEGER,
                    koin_awal INTEGER,
                    account_number INTEGER,
                    balance INTEGER,
                    blocked_users TEXT
                    )''')

    conn.commit()
    conn.close()
# Fungsi untuk membatalkan pembayaran
def cancel_payment(user_id):
    # Hubungkan dengan database
    conn = sqlite3.connect('izmiftah.db')
    cursor = conn.cursor()

    # Batalkan pembayaran dengan menghapus record user_id pada tabel users
    try:
        cursor.execute("DELETE FROM izmiftahdatabase WHERE user_id=:id", {'id': user_id,})
        conn.commit()
        conn.close()
        print("Pembayaran telah dibatalkan")
        return True
    except:
        print("Pembayaran gagal dibatalkan")
        return False


def check_initialization(self):
    if self.initialized:
        print("R&D telah diinisialisasi.")
    else:
        print("R&D belum diinisialisasi.")


@bot.callback_query_handler(func=lambda call: True)
def handle_cancel_payment(call):
    user_id = call.data
    if cancel_payment(user_id):
        bot.answer_callback_query(call.id, text="Pembayaran berhasil dibatalkan.")
    else:
        bot.answer_callback_query(call.id, text="Gagal membatalkan pembayaran.")

def get_saldo(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT saldo_pengguna FROM users")
    saldo = cursor.fetchone()[0]
    return saldo

def my_thread():
    # Menginisialisasi koneksi ke database SQLite
    connection = sqlite3.connect("izmiftah.db")

    try:
        # Memanggil fungsi untuk mengambil saldo
        saldo = get_saldo(connection)
        print("Saldo terkini: ", new_saldo)
    except sqlite3.ProgrammingError as e:
        print("Terjadi kesalahan saat mengambil saldo: ", str(e))
    finally:
        # Menutup koneksi ke database SQLite
        connection.close()

# Menjalankan thread
#my_thread()

def generate_passwordnya(user_id):
    last_three_digits = str(user_id)[-3:]  # Mengambil 3 angka terakhir dari user ID
    generated_password = last_three_digits.zfill(3)  # Mengisi angka dengan 0 di depan jika kurang dari 3 digit
    passwords[user_id] = generated_password
    return generated_password

# Handler untuk perintah "/generate_password"
@bot.message_handler(commands=['izmaaulia21'])
def generate_password_command(message):
    user_id = message.from_user.id
    generated_password = generate_passwordnya(user_id)
    bot.send_message(message.chat.id, text=f"Password baru Anda adalah: {generated_password}")

def is_not_blocked():
    # Koneksi ke database
    channel = bot.inline_handlers.channel
    name = bot.get_chat_member(channel, inisial)
    if name.status == 'kicked':
        return False
    else:
        return True

def get_saldo_from_db(user_id):
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()
    c.execute('SELECT saldo FROM izmiftahdatabase WHERE user_id = ?', (user_id,))
    saldo = c.fetchone()  # Mengambil hasil kueri
    conn.close()

    if saldo is not None:
        return saldo[0]  # Mengembalikan saldo jika ditemukan
    else:
        return 0  # Mengembalikan 0 jika saldo tidak ditemukan

def update_saldo_in_db(user_id):
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()
    c.execute('UPDATE izmiftahdatabase SET saldo = ?, saldo_pengguna = ? WHERE user_id = ?', (new_saldo, saldo_pengguna, user_id))
    conn.commit()
    conn.close()

def get_jumlah_koin_from_db(user_id):
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()
    c.execute('SELECT jumlah_koin FROM izmiftahdatabase WHERE user_id = ?', (user_id,))
    jumlah_koin = c.fetchone()
    conn.close()
    return jumlah_koin[0] if jumlah_koin else 0

def update_jumlah_koin_in_db(user_id, new_jumlah_koin):
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()
    c.execute('UPDATE izmiftahdatabase SET jumlah_koin = ? WHERE user_id = ?', (new_jumlah_koin, user_id))
    conn.commit()
    conn.close()

def get_saldo_pengguna_from_db(user_id):
    conn = sqlite3.connect('saldo.db')
    c = conn.cursor()
    c.execute('SELECT saldo_pengguna FROM izmiftahdatabase WHERE user_id = ?', (user_id,))
    saldo_pengguna = c.fetchone()
    conn.close()
    return saldo_pengguna[0] if saldo_pengguna else 0

# Handler for the reset command
bot.message_handler(func=lambda message: message.text.startswith('/reset'))
def handle_reset(message):
    command_parts = message.text.split(' ')
    if len(command_parts) == 3:
        password = command_parts[2]
        if password == passnya:
            global  new_saldo, saldo_pengguna
            user_id = message.from_user.id
            new_saldo += saldo_pengguna
            user_id = user_id
            get_new_saldo(message)
            conn = sqlite3.connect('izmiftah.db')
            new_saldo += new_saldo

            bot.send_message(message.chat.id, text="Password baru telah diubah!")
            record_unblocked_user(id, saldo, jumlah_koin, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, new_saldo, account, koin_awal, account_number, balance)
            update_saldo_in_db(message.from_user)
            update_jumlah_koin_in_db(message.from_user, new_saldo)
            bot.send_message(message.chat.id, text=f"Saldo Anda telah diubah menjadi {new_saldo}")
            with conn:
                cursor.execute("UPDATE saldo_pengguna SET amount = 100)")
                cursor.execute("UPDATE jumlah_koin SET amount = 100)")
                # Reset all balances to 100
                bot.reply_to(message.chat.id, "All balances have been reset to 100.")
        else:
            bot.reply_to(message, "Invalid password!")

def update_keywordnya():
    global keywords_list

    try:
        with open('keyword.txt', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            keywords_list = [row[0] for row in reader]
            print(keywords_list)
    except IOError:
        print("Error: unable to open file")

# Tambahkan logika untuk memeriksa keberadaan file auto.xlsx
if not os.path.isfile('auto.xlsx'):
    # Lakukan operasi jika file tidak ada
    # File auto.xlsx tidak ada, download atau generate
    try:
        subprocess.run(['wget', 'https://github.com/miftah06/skripsi/raw/master/bab-generator/input_data.xlsx'])
        subprocess.run(['wget', 'https://github.com/miftah06/skripsi/raw/master/cover-generator/cover.xlsx'])
        subprocess.run(['mv', 'input_data.xlsx', 'auto.xlsx'])
        print("File auto.xlsx berhasil di-download dan diubah namanya.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Gagal mendownload atau mengubah nama file auto.xlsx.")
        # Tambahkan logika untuk menghasilkan file auto.xlsx

# Fungsi untuk menghasilkan HTML berdasarkan data dari dataframe
def generate_html(dataframe):
    # Your logic for generating HTML based on the dataframe goes here
    # Replace this with your actual implementation
    generated_html = f"jangan lupa /update terlebih dahulu \n silahkan /download.. dan tolong \n <html<<body<<h1< ganti bagian sini... untuk mengedit file htmlnya </h1<</body<</html<"
    return generated_html

# Fungsi untuk membuat prompt AI
def create_ai_promptnya(user_input):
    return f"{identitas}\n\nUser: {user_input}\nAI:"

def display_saldo(message):
    try:
        bot.reply_to(message, f"Saldo Anda saat ini adalah: {saldo}")
        bot.reply_to(message, f"Saldo sedekah saat ini adalah: {jumlah_koin}")
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan dalam mengambil saldo: {str(e)}")


def toggle_blokir_koin(message):
    global koin_terblokir
    if koin_terblokir:
        koin_terblokir = False
        global saldo_pengguna
        new_saldo -= +15
        saldo_pengguna = saldo
        bot.send_message(message.chat.id, text="Pemblokiran koin telah dinonaktifkan.")
    else:
        koin_terblokir = True
        bot.send_message(message.chat.id, text="Pemblokiran koin telah diaktifkan.")

# Handler untuk perintah "/payment"
@bot.message_handler(commands=['link'])
def make_link(message):
    # Membuka tautan dari Telegram
    payment_link = f"{link_jualan}"
    bot.send_message(message.chat.id, text=f"Anda dapat melakukan pembayaran di {payment_link}")
    bot.send_message(message.chat.id, text=f"Silahkan hubungi {admin} atau di email: {email_kamu} untuk bantuan lebih lanjut.")
# Define global variables

# Function to initialize user balance
def inisiasi_saldo_pengguna(username):
    conn = sqlite3.connect('izmiftah.db')
    cursor = conn.cursor()

    # Check if user already exists in the database
    cursor.execute("SELECT * FROM izmiftahdatabase WHERE username=?", (username,))
    name = cursor.fetchone()

    if name is None:
        # If user does not exist, insert a new row with balance as 0
        cursor.execute("INSERT INTO izmiftahdatabase (username, saldo_pengguna) VALUES (?, 0)", (username,))
        conn.commit()
        print("User", username, "successfully initialized with balance 0")
    else:
        print("User", username, "already exists with balance", name[1])

    conn.close()

# Function to update user balance and store it in history
def update_saldo_pengguna(username, new_saldo):
    conn = sqlite3.connect('izmiftah.db')
    cursor = conn.cursor()

    # Update the user's balance
    cursor.execute("UPDATE izmiftahdatabase SET saldo_pengguna=? WHERE username=?", (new_saldo, username))
    conn.commit()

    # Store the updated balance in history table
    cursor.execute("INSERT INTO history (username, saldo_pengguna) VALUES (?, ?)", (username, new_saldo))
    conn.commit()

    print("User", username, "balance updated to", new_saldo)

    conn.close()

def my_thread():
    current_thread = threading.current_thread()
    print("Current thread:", current_thread.name)


# Fungsi untuk mengurangi saldo
def kurangi_saldo(jumlah):
    global new_saldo, jumlah_saldo, jumlah_koin
    new_saldo -= jumlah
    jumlah_saldo -= jumlah
    jumlah_koin -= jumlah
    if new_saldo <= 0:
        blokir_aktif



# Function to check if saldo is equal to or greater than specified amount
def display_saldo(user_id, amount):
    try:
        inisiasi_saldo_pengguna(user_id)
        update_saldo_pengguna(user_id, new_saldo)
        conn = sqlite3.connect('izmiftah.db')
        c = conn.cursor()

        query = f"SELECT saldo FROM izmiftahdatabase WHERE user_id = '{user_id}'"

        c.execute(query)
        result = c.fetchone()

        if result and result[0] >= amount:
            bot.send_message(user_id, text=f"Saldo Anda saat ini adalah: {new_saldo}")
            bot.send_message(user_id, text=f"Saldo sedekah saat ini adalah: {jumlah_koin}")
            return True
            send_payment(user_id, amount)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        conn.close()
        return False

# Mendefinisikan fungsi untuk memperbarui saldo pengguna
@bot.message_handler(commands=['my_id'])
def show_user_id(message):
    user_id = message.from_user.id
    bot.reply_to(message, f"Your user ID is: {user_id}")

def jumlah_nol(jumlah_jumlah_koin):
    try:
        set_user_values(min(jumlah_jumlah_koin))
        global saldo, jumlah_koin, saldo_pengguna,saldo_awal, jumlah_koin, saldo_kredit, credit

        jumlah_jumlah_koin = new_saldo
        # Simpan nilai awal saldo
        saldo_awal = jumlah_koin

        # Hitung jumlah saldo baru setelah mencapai 0

        # Hitung sisa jumlah_koin dari pembagian jumlah_koin awal dengan saldo
        jumlah_sisa_saldo = saldo_awal % jumlah_koin

        # Hitung jumlah_koin kredit
        saldo_kredit = jumlah_sisa_saldo

        # Hitung jumlah_koin yang tersisa setelah diproses
        jumlah_koin = saldo_awal % jumlah_sisa_saldo

        # Hitung kredit
        credit = jumlah_koin - jumlah_jumlah_koin
        print(jumlah_koin)
        print(jumlah_jumlah_koin)
        print(jumlah_sisa_saldo)
        print(saldo_kredit)
    except Exception as e:
        print(e)

        # Panggil fungsi blokir_nonaktif untuk memeriksa apakah perlu memblokir


def generate_keyword_filenya(filename, num_keywords):
    keyword_list = acak.kwlist
    num_keywords = min(num_keywords, len(keyword_list))

    random_keywords = random.sample(keyword_list, num_keywords)

    with open(filename, "w") as file:
        file.write("\n".join(random_keywords))



@bot.message_handler(commands=['premium'])
def update_passwordnya(message):
    command_parts = message.text.split(' ')

    if len(command_parts) == 3:  # Memeriksa jumlah argumen
        user_id = message.from_user.id
        current_password = command_parts[1]  # Mengambil kata sandi saat ini
        new_password = command_parts[2]  # Mengambil kata sandi baru

        # Periksa apakah kata sandi saat ini sesuai dengan yang disimpan untuk ID pengguna
        if passwords.get(user_id) == current_password:
            # Perbarui kata sandi dengan kata sandi baru
            passwords[user_id] = new_password
            bot.send_message(message.chat.id, text="Kata sandi berhasil diperbarui.")
        else:
            bot.send_message(message.chat.id, text="Kata sandi saat ini salah. Coba lagi.")
    else:
        bot.send_message(message.chat.id, text="Perintah tidak valid. Gunakan format: /premium [kata sandi saat ini] [kata sandi baru]")


# Handler untuk perintah "/isi_saldo"
@bot.message_handler(commands=['isi_saldo'])
def handle_topup(message):
    user_id = message.from_user.id
    command_parts = message.text.split(' ')
    if len(command_parts) == 3:  # Memeriksa jumlah argumen
        password = command_parts[1]
        if passwords.get(user_id) == password:  # Memeriksa apakah password sesuai
            global tambahan_saldo
            tambahan_saldo = int(command_parts[2])  # Mengambil jumlah saldo yang ditambahkan dari perintah
            tambah_saldo(saldo)
            bot.send_message(message.chat.id, "Saldo anda telah terisi.")
        else:
            bot.send_message(message.chat.id, "Kata sandi salah.")


# Handler untuk perintah "/berbagi" dengan kata sandi
@bot.message_handler(func=lambda message: message.text.startswith('/payment'))
def berbagi_with_password(message):
    command_parts = message.text.split(' ')
    if len(command_parts) == 2:
        password = command_parts[1]
        if password == passnya:
            user_id = message.from_user
            global  new_saldo, saldo_pengguna
            new_saldo += saldo_pengguna
            get_new_saldo(message)
            saldo_pengguna += 100
            new_saldo += 100
            tambah_saldo(saldo)

            bot.send_message(message.chat.id, text="payment berhasil.")
            record_unblocked_user(id, saldo, jumlah_koin, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, new_saldo, account, koin_awal, account_number, balance)
            # Menambahkan user ke list unblocked_users
            bot.send_message(message.chat.id, text=f"Saldo anda telah terisi sebesar {saldo_pengguna}.")  # Memberi tahu pengguna bahwa saldo mereka telah terisi kembali
        else:
            bot.send_message(message.chat.id, text="Kata sandi salah. Coba lagi.")
    else:
        bot.send_message(message.chat.id, text="Perintah tidak valid. Lakukan topup dengan: /payment [password dari admin]")

@bot.message_handler(func=lambda message: message.text.startswith('/berbagi'))
def payment_with_password(message):
    command_parts = message.text.split(' ')
    if len(command_parts) == 3:  # Memeriksa jumlah argumen
        password = command_parts[1]
        new_saldo_input = int(command_parts[2])  # Mengambil jumlah_koin baru dari perintah
        user_id = message.from_user.id

        # Periksa apakah password sesuai dengan yang disimpan untuk ID pengguna
        if passwords.get(user_id) == password:
            # Mengambil saldo_pengguna dari database
            global saldo_baruku, jumlah_koin
            saldo_baruku = new_saldo_input
            jumlah_koin = jumlah_koin + saldo_baruku
            if jumlah_koin is not None:
                # Memperbarui saldo_pengguna di database
                jumlah_koin = jumlah_koin + saldo_baruku
                global saldo
                saldo = jumlah_koin
                bot.send_message(message.chat.id, text=f"Saldo berhasil diperbarui dengan jumlah {new_saldo}\n saldo tambahan: {saldo}.")
                bot.send_message(message.chat.id, text=f"dengan user_id anda {user_id}.")
                bot.send_message(message.chat.id, text=f"Saldo anda juga telah terisi menjadi {jumlah_koin} dengan topup bonusx {saldo_baruku}.")  # Memberi tahu pengguna bahwa saldo mereka telah terisi kembali
            else:
                bot.send_message(message.chat.id, text="Saldo Anda saat ini tidak tersedia.")
        else:
            bot.send_message(message.chat.id, text=f"Kata sandi salah. Silakan coba lagi.")
    else:
        bot.send_message(message.chat.id, text="Perintah tidak valid. Gunakan format: /berbagi [password] [jumlah nilai acak]")


@bot.message_handler(func=lambda message: message.text.startswith('/reset_saldo'))
def payment_with_password(message):
    command_parts = message.text.split(' ')
    if len(command_parts) == 3:  # Memeriksa jumlah argumen
        password = command_parts[1]
        new_saldo_input = int(command_parts[2])  # Mengambil jumlah_koin baru dari perintah
        user_id = message.from_user.id

        # Periksa apakah password sesuai dengan yang disimpan untuk ID pengguna
        if passwords.get(user_id) == password:
            # Mengambil saldo_pengguna dari database
            global saldo_baruku, jumlah_koin
            saldo_baruku = new_saldo_input
            saldo_pengguna = jumlah_koin
            jumlah_koin = saldo_baruku + saldo_pengguna
            is_not_blocked_user()

            if jumlah_koin is not None:
                # Memperbarui saldo_pengguna di database
                jumlah_koin = saldo_baruku
                global saldo
                saldo = jumlah_koin

                bot.send_message(message.chat.id, text=f"Saldo berhasil diperbarui pada tanggal dan waktu {timestamp}.")
                bot.send_message(message.chat.id, text=f"dengan user_id anda {user_id}.")
                bot.send_message(message.chat.id, text=f"Saldo anda juga telah di ubah ke {saldo_baruku}.")  # Memberi tahu pengguna bahwa saldo mereka telah terisi kembali
            else:
                bot.send_message(message.chat.id, text="Saldo Anda saat ini tidak tersedia.")
        else:
            bot.send_message(message.chat.id, text=f"Kata sandi salah. Silakan coba lagi.")
    else:
        bot.send_message(message.chat.id, text="Perintah tidak valid. Gunakan format: /reset_saldo [password] [jumlah nilai  reset]")

@bot.message_handler(commands=['topup'])
def topup_with_password(message):
    command_parts = message.text.split(' ')
    if len(command_parts) == 2:
        password = command_parts[1]
        if password == passnya:
            global saldo
            global jumlah_kredit, jumlah_koin
            global saldo_pengguna, new_saldo
            saldo += 100
            jumlah_koin += 100
            saldo_pengguna += 100
            new_saldo += saldo_pengguna
            bot.send_message(message.chat.id, text="Top up berhasil.")

            record_unblocked_user(id, saldo, jumlah_koin, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, new_saldo, account, koin_awal, account_number, balance)
            bot.send_message(message.chat.id, text=f"saldo anda telah terisi sebesar {saldo}.")  # Memberi tahu pengguna bahwa saldo mereka telah terisi kembali
        else:
            bot.send_message(message.chat.id, text="Kata sandi salah. Coba lagi.")
    else:
        bot.send_message(message.chat.id, text="Perintah tidak valid. Lakukan topup dengan: /topup [password dengan command]")



# Fungsi untuk menampilkan saldo pengguna
def display_message(message):
    try:
        # Cek apakah saldo_pengguna dan jumlah_koin telah mencapai batas untuk memblokir
        if new_saldo <= 0 and jumlah_koin <= 0:
            toggle_blokir_koin(saldo_pengguna)
            bot.send_message(message.chat.id, "Pemblokiran koin telah dinonaktifkan.")

        # Cek apakah saldo_pengguna dan jumlah_koin habis, jika iya, blokir bot
        if new_saldo <= 0 and saldo_pengguna <= 0:
            handle_blokir
            bot.send_message(message.chat.id, "Bot telah diblokir karena kehabisan saldo dan saldo sedekahan.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Terjadi kesalahan dalam menampilkan pesan: {str(e)}")


def send_formatted_message(message, formatted_message):
    bot.send_message(chat_id=message.chat.id, text=formatted_message)

@bot.message_handler(commands=['my_id'])
def show_user_id(message):
    user_id = message.from_user.id
    bot.reply_to(message, f"Your user ID is: {user_id}")

# Function to toggle blocking koin
def toggle_blokir_koin(message):
    global koin_terblokir
    if koin_terblokir:
        koin_terblokir = False
        global jumlah_koin
        new_saldo -= + saldo
        jumlah_koin -= saldo
    else:
        koin_terblokir = True

# Definisi awal variabel koin_terblokir
koin_terblokir = False

def toggle_blokir_koin(message):
    global koin_terblokir
    if koin_terblokir:
        global jumlah_koin_awal
        koin_terblokir = False
        new_saldo -= +jumlah_koin_awal
        saldo -= saldo
    else:
        koin_terblokir = True

# Koneksi ke database izmiftah.db
conn = sqlite3.connect("izmiftah.db")
cursor = conn.cursor()

# Fungsi untuk menampilkan pesan
# Fungsi untuk menampilkan saldo pengguna
# Fungsi untuk menampilkan saldo pengguna

# Definisi awal variabel koin_terblokir
koin_terblokir = False

# Fungsi untuk memblokir/mengaktifkan blokir koin
def toggle_blokir_koin(message):
    global koin_terblokir
    if koin_terblokir:
        global jumlah_koin
        koin_terblokir = False
        saldo -= saldo
        new_saldo -= saldo
    else:
        global jumlah_koin
        koin_terblokir = True
        new_saldo -= jumlah_koin
        jumlah_koin += saldo

# Import module atau plugin tambahan untuk display_message(message)
## Kode lengkap untuk menghubungkan ke database izmiftah.db dan fungsi-fungsi lainnya

# Koneksi ke database
conn = sqlite3.connect('izmiftah.db')

# Fungsi untuk mengurangi saldo
def aturan_saldo(user_id):
    global saldo_pengguna
    saldo_pengguna = 100
    jumlah_koin = None
    bot.send_message(user_id, text=f"Saldo terpakai: {saldo_pengguna}. Saldo Anda sekarang: {saldo_awal}")
    # Kurangi saldo_pengguna
    global jumlah, new_saldo
    new_saldo -= jumlah
    jumlah -= jumlah
    update_jumlah_koin_in_db(user_id)
    get_saldo_pengguna_from_db(user_id)
    get_saldo_pengguna_from_db(user_id)
    ambil_saldo(user_id, jumlah_koin)


    # Update saldo di database
    cursor.execute(f"UPDATE izmiftahdatabase SET saldo_pengguna = {saldo_pengguna} WHERE user_id = {user_id}")
    conn.commit()

    # Tampilkan saldo terkini
    print(f"Saldo terpakai: {jumlah}. Saldo Anda sekarang: {saldo_pengguna}")


c = conn.cursor()

def generate_keyword_file(filename, num_keywords):
    keyword_list = acak.kwlist
    num_keywords = min(num_keywords, len(keyword_list))

    random_keywords = random.sample(keyword_list, num_keywords)

    with open(filename, "w") as file:
        file.write("\n".join(random_keywords))

# Contoh penggunaan assert
def check_saldo():
    global saldo_pengguna
    assert saldo_pengguna >= 0, "Saldo tidak boleh negatif."

# Fungsi untuk mendapatkan saldo pengguna dari database
def get_saldo_penggunanya(user_id):
    cursor.execute(f"SELECT saldo_pengguna FROM izmiftahdatabase WHERE user_id = {user_id}")
    return saldo_pengguna

# Fungsi untuk mengatur saldo pengguna
def atur_saldo_pengguna(user_id, saldo):
    cursor.execute(f"UPDATE izmiftahdatabase SET saldo_pengguna = {saldo} WHERE user_id = {user_id}")
    conn.commit()

# Fungsi untuk mengambil saldo pengguna jika hal tersebut berupa new_saldo -= jumlah
def ambil_saldo(user_id, jumlah):
    global new_saldo, saldo_pengguna
    saldo_pengguna = saldo
    new_saldo -= jumlah
    atur_saldo_pengguna(user_id, saldo_pengguna)

# Fungsi untuk mengatur saldo
def atur_saldonya(saldo):
    cursor.execute(f"UPDATE izmiftahdatabase SET saldo = {saldo} WHERE user_id = 1")
    cursor.execute(f"UPDATE izmiftahdatabase SET saldo_pengguna = {saldo_pengguna} WHERE user_id = 1")
    cursor.execute(f"UPDATE izmiftahdatabase SET new_saldo = {saldo} WHERE user_id = 1")
    cursor.execute(f"UPDATE izmiftahdatabase SET jumlah_koin = {jumlah_koin} WHERE user_id = 1")
    conn.commit()

# Fungsi untuk mengatur jumlah saldo dan saldo pengguna menjadi 0
def reset_saldo():
    atur_saldonya(0)
    atur_saldo_pengguna(1, 0)

# Membuat koneksi dengan database izmiftah.db
conn = sqlite3.connect('izmiftah.db')
c = conn.cursor()
# Handler untuk perintah /cek_saldo
@bot.message_handler(commands=['cek_saldo'])
def cek_saldo(message):
    user_id = message.from_user.id
    cursor.execute('SELECT saldo_pengguna FROM uers WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    if result:
        saldo = result[0]
        bot.send_message(message.chat.id, f"Saldo Anda saat ini adalah {new_saldo}\n saldo tambahan: {saldo}.")
    else:
        bot.send_message(message.chat.id, "Saldo Anda saat ini tidak tersedia.")

# Tambahkan logika untuk memeriksa keberadaan file auto.xlsx
if not os.path.isfile('auto.xlsx'):
    # Lakukan operasi jika file tidak ada
    # File auto.xlsx tidak ada, download atau generate
    try:
        subprocess.run(['wget', 'https://github.com/miftah06/skripsi/raw/master/bab-generator/input_data.xlsx'])
        subprocess.run(['wget', 'https://github.com/miftah06/skripsi/raw/master/cover-generator/cover.xlsx'])
        subprocess.run(['mv', 'input_data.xlsx', 'auto.xlsx'])
        print("File auto.xlsx berhasil di-download dan diubah namanya.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Gagal mendownload atau mengubah nama file auto.xlsx.")
        # Tambahkan logika untuk menghasilkan file auto.xlsx

# Fungsi untuk menghasilkan HTML berdasarkan data dari dataframe
def generate_html(dataframe):
    # Your logic for generating HTML based on the dataframe goes here
    # Replace this with your actual implementation
    generated_html = f"jangan lupa /update terlebih dahulu \n silahkan /download.. dan tolong \n <html<<body<<h1< ganti bagian sini... untuk mengedit file htmlnya </h1<</body<</html<"
    return generated_html

@bot.message_handler(func=lambda message: message.text.lower().startswith('/artikel'))
def generate_article(message):
    text_parts = message.text.split(' ', 1)

    if len(text_parts) < 2:
        response = "Please provide the article parts after the command."
    else:
        text = text_parts[1]
        parts = text.split(',')
        parts = [part.strip() for part in parts]

        if len(parts) != 5:
            response = "Invalid number of parts. Please provide exactly 5 parts."
        else:
            title = parts[0]
            introduction = parts[1]
            body = parts[2]
            conclusion = parts[3]
            references = parts[4]

            article = f"Title: {title}\n\n"
            article += f"Introduction: {introduction}\n\n"
            article += f"Body: {body}\n\n"
            article += f"Conclusion: {conclusion}\n\n"
            article += f"References: {references}"

            response = f"Article created successfully!\n\n{article}"

    bot.send_message(chat_id=message.chat.id, text=response)


@bot.message_handler(func=lambda message: message.text.lower().startswith('/hitung') and message.chat.type == 'private')
def handle_hitung(message):
    user_input = ""
    split_message = message.text.split(' ')
    if len(split_message) > 1:
        user_input = split_message[1]

    global jumlah_koin, new_saldo, saldo_pengguna
    new_saldo -= 3
    saldo_pengguna -= 10

    if user_input:
        try:
            result = hitung(user_input)
            bot.send_message(message.chat.id, f"Hasil: {result}")
            print(f"Hasil: {result}")
            result = eval(user_input)
            bot.send_message(message.chat.id, f"Hasil: {result}")
            if result != result:
                bot.send_message(message.chat.id, f"Hasil: {result}")
            else:
                bot.send_message(message.chat.id, f"Hasil: {result}")
            print(f"Hasil: {result}")
        except Exception as e:
            bot.send_message(message.chat.id, f"Terjadi kesalahan: {str(e)}")
            print(f"Terjadi kesalahan: {str(e)}")
    else:
        bot.send_message(message.chat.id, "Silakan gunakan perintah '/hitung [perhitungan] dengan spasi' dan tambahkan symbol bukan huruf di setiap bagian\n contoh\n\n /hitung 1*1 * 2.")
        print("Silakan gunakan perintah 'hitung' untuk melakukan perhitungan matematika.")

def hitung(*args):
    expression = "+".join(args)

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"What is the result of {expression}?",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0,
    )

    answer = response.choices[0].text.strip()

    return answer

@bot.message_handler(func=lambda message: message.text.lower().startswith('/coding'))
def handle_coding(message):
    # Checking if message text contains enough words
    if len(message.text.split(' ')) < 3:
        bot.reply_to(message, "Please provide an error code.")
        return

    # Rest of the code handling the error code
    error_code = message.text.split(' ')[2]

    global jumlah_koin, new_saldo, saldo_pengguna
    new_saldo += -3

    # Memeriksa apakah kode error terkait dengan HTML, JavaScript, atau Python
    if 'html' in error_code:
        language = 'HTML'
    elif 'javascript' in error_code:
        language = 'JavaScript'
    elif 'python' in error_code:
        language = 'Python'
        language = 'JavaScript'
    elif 'perl' in error_code:
        language = 'perl'
        language = 'JavaScript'
    elif 'php' in error_code:
        language = 'php'
    elif 'css' in error_code:
        language = 'css'
    elif 'json' in error_code:
        language = 'json'
    else:
        # Jika kode error tidak terkait dengan bahasa yang didukung, maka mengirim pesan error
        bot.reply_to(message, "Maaf, saya hanya dapat menangani error terkait dengan HTML, JavaScript, dan Python.")
        return

    # Menghapus bahasa dari kode error untuk hasil pencarian yang lebih baik
    error_code = error_code.replace(language, '').strip()

    # Menghasilkan jawaban menggunakan model bahasa dari OpenAI
    response = openai.Completion.create(
        engine='gpt-3.5-turbo-instruct',
        prompt=f"Jelaskan error {error_code} dalam {language} menggunakan W3Schools",
        temperature=0.5,
        max_tokens=200,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        n=1,
        stop=None,
        log_level="info"
    )

    # Mendapatkan penjelasan dari hasil response
    explanation = response.choices[0].text.strip()

    # Mengirim penjelasan sebagai balasan kepada pengguna
    bot.reply_to(message, explanation)


@bot.message_handler(commands=['ai_prompt'])
def handle_prompt(message):
    args = message.text.split('/')[1:]

    if len(args) == 7:
        keyword1_file, keyword2_file, output_file, command_option, specification_option, prompt_type, additional_input = args

        # Generate keyword files
        generate_keyword_file(keyword1_file, 500)
        generate_keyword_file(keyword2_file, 500)

        # Create prompt
        create_prompt(keyword1_file, keyword2_file, output_file, command_option, specification_option, prompt_type,
                      additional_input, message)

        # Send the output file to the user
        with open(output_file, 'r') as file:
            output_text = file.read()

        bot.send_message(message.chat.id, output_text)
    else:
        bot.send_message(message.chat.id,
                         "Format prompt tidak valid. Gunakan format /ai_prompt fitur.txt/objek.txt/ai.txt/kata_perintah/specification_option/prompt_type/jumlah")


def create_prompt(keyword1_file, keyword2_file, output_file, command_option, specification_option, prompt_type,
                  additional_input, message):
    with open("skrip.txt", "r") as parno_file:
        parno_options = parno_file.readlines()
        prompt = random.choice(parno_options).strip()
    with open(keyword1_file, "r") as key1_file, open(keyword2_file, "r") as key2_file, open(output_file, "w") as file:
        key1_options = key1_file.readlines()
        key2_options = key2_file.readlines()
        key1_option = random.choice(key1_options).strip()
        key2_option = random.choice(key2_options).strip()
        paragraf = additional_input.strip()

        try:
            subprocess.run(['bash', 'key.sh'], check=True)
            bot.reply_to(message,
                         f"Ai prompt sudah terkespor ke {output_file}\nSilahkan jalankan /keyword lalu /download_hasil \n lalu /download2 untuk output.txt sebagai /ai /command/command/output.txt atau ai.txt untuk /download3.")
        except subprocess.CalledProcessError as e:
            bot.reply_to(message, f"Error: {e}")
        if prompt_type == "text":
            output_line = f"Generate script with command:\n\n\n {command_option} {specification_option} serta {key1_option}\n dengan tambahan fungsi {key2_option}\n adapun jika isinya berupa {prompt} {key1_option}\n\n dengan fitur:\n\n{prompt} bersama fungsi atau pembahasan mengenai {key2_option} serta berikan saya detail lengkapnya \n\n\n"
        elif prompt_type == "tulisan":
            output_line = f"Generate text with command:\n\n\n {command_option} {specification_option} serta {key1_option}\n dengan kondisi {key2_option}\n adapun jika isinya berupa {prompt} {key1_option}\n\n dengan fitur:\n\n{prompt} bersama fungsi atau pembahasan mengenai {key2_option} serta berikan saya detail lengkapnya \n\n\n"
        elif prompt_type == "image":
            output_line = f"Generate image with command:\n\n\n {command_option}, dengan latar elegant dengan penuh estetika nuansa {specification_option} bertemakan {key1_option} dengan warna {key2_option}\n\n\n"
        elif prompt_type == "script":
            output_line = f"Generate script with command:\n\n\n {command_option}{specification_option} dan serta {prompt} jika hal tersebut berupa\n {prompt}\n dengan {key1_option}\n\n di dalam skrip {parno_options} {key1_option}\n dengan module atau plugin tambahan {prompt}{key2_option}\n\n\npada untuk {specification_option} dan berikan saya skrip lengkapnya\n\n\n\n"
        elif prompt_type == "jawaban":
            output_line = f"Generate answer with command:\n\n\n {command_option}{specification_option} dan jawablah jika soalnya:\n {prompt}\n tanpa {key1_option}\n\n maka tolong jawab {parno_options} {key1_option}\n dengan menjelaskan {prompt}{key2_option}\n\n\n {specification_option} secara rinci\n sebanyak {paragraf} paragraf serta berikan saya jawaban lengkapnya\n\n"
        elif prompt_type == "materi":
            output_line = f"Generate exam with command:\n\n\n {command_option}{specification_option} dan lengkapilah jika soalnya:\n {prompt}\n tanpa {key1_option}\n\n maka tolong buatkan juga {parno_options} {key1_option}\n dengan sangat \n\n\n secara rinci\n sebanyak {paragraf} paragraf serta berikan saya jawaban lengkapnya\n\n"
        elif prompt_type == "soal":
            output_line = f"Generate soal with command:\n\n\n buatkanlah saya soal {command_option}{specification_option} \n dengan sangat \n\n\n secara rinci\n sebanyak {paragraf} soal serta berikan saya jawaban lengkapnya\n\n"
        elif prompt_type == "cerita":
            output_line = f"Generate story with command:\n\n\n {command_option}, dengan latar elegant dengan penuh estetika nuansa {specification_option} bertemakan {key1_option} dengan warna {key2_option}\n\n\n{command_option}{specification_option} dan buatlah momen lucu setelah terjadi kejadian berupa\n\n {prompt}\n\n\n dan buatlah ceritanya dengan penuh drama dan lelucon keharmonisan\n\n dan jangan lupa buat ulang dengan tema:\n {key1_option}\n dengan menambahkan tambahkan {prompt}\n {specification_option} di dalam ceritanya\n\n sebanyak {paragraf} paragraf\n\n"
        elif prompt_type == "rpp":
            output_line = f"Generate RPP with command:\n\n\n {command_option}, dengan sedetail lengkap {specification_option} dengan sangat {key1_option} dengan ketentuan yang {key2_option}\n\n\n{command_option}{specification_option} dan buatkanlah saya\n\n {prompt}\n\n\n dan buatlah dengan sesempurna dan sedetail munggkin dengan lengkap\n {key1_option}\n dengan menambahkan tambahkan {prompt}\n {specification_option} di dalam RPP nya\n\n untuk kelas {paragraf} \n\n"
        else:
            output_line = "Invalid prompt type\n masukkan opsi\n 1.image,\n 2.text atau\n 3.script\n 4.tulisan\n 5. jawaban\n 6.soal\n 7. cerita\n "
        file.write(output_line)


# Handler untuk perintah /ai
@bot.message_handler(commands=['ai'])
def write_ai_chat(message):
    try:
        if is_blokir_active(message):
            bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")
        if blocked_users:
            if is_blokir_active(message):
                bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")
                block_user(username)
        if is_not_blocked_user:
            bot.send_message(message.chat.id, text=f"selamat! datang kembali {username}!")
            bot.send_message(message.chat.id, text=f" silahkan melakukan /topup atau /payment buat isi saldonya sebanyak - banyak nya")
            global new_saldo, jumlah_koin, saldo_pengguna
            new_saldo -= 10
            jumlah_koin -= 5
            saldo_pengguna -= 10
            if jumlah_koin > 0 and saldo_pengguna > 0:
                message_text = message.text.split(' ', 1)[1] if len(message.text.split()) > 1 else "No input provided."

                # Membuat permintaan ke OpenAI Chat API
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",  # Pilih model yang sesuai
                    messages=[
                        {"role": "system", "content": "You are a worker with your research and development."},
                        {"role": "user", "content": message_text}
                    ]
                )

                # Mengambil pesan dari respons
                ai_reply = response['choices'][0]['message']['content']

                # Mengirimkan balasan AI sebagai reply
                bot.send_message(message.chat.id, text=ai_reply)
    except Exception as e:
        bot.send_message(message.chat.id, text=str(e))

# Fungsi untuk membuat prompt AI
def create_ai_prompt(user_input):
    return f"{identitas}\n\nUser: {user_input}\nAI:"

# Fungsi untuk menampilkan saldo pengguna
def display_saldo(message):
    try:
        user_id = message.from_user
        #update_users_table untuk melakukan update pada tabel users
        update_users_table()
        global saldo_nol, saldo_pengguna, jumlah_koin
        # Mengambil saldo pengguna dari database
        bot.reply_to(message, f"Saldo Anda saat ini adalah: {jumlah_koin}")
        bot.reply_to(message, f"Saldo sedekah atau gabungan saat ini adalah: {saldo_pengguna}")
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan dalam mengambil saldo: {str(e)}")
def toggle_blokir_koin(message):
    global koin_terblokir
    if koin_terblokir:
        koin_terblokir = False
        global saldo, new_saldo
        new_saldo -= 10
        bot.send_message(message.chat.id, text="Pemblokiran koin telah dinonaktifkan.")
    else:
        koin_terblokir = True
        new_saldo += 15
        bot.send_message(message.chat.id, text="Pemblokiran koin telah diaktifkan.")

# Handler untuk perintah "/payment"
@bot.message_handler(commands=['link'])
def make_payment(message):
    # Membuka tautan dari Telegram
    payment_link = f"{link_jualan}"
    bot.send_message(message.chat.id, text=f"Anda dapat melakukan pembayaran di {payment_link}")
    bot.send_message(message.chat.id, text=f"Silahkan hubungi {admin} atau di email: {email_kamu} untuk bantuan lebih lanjut.")

@bot.message_handler(commands=['my_id'])
def show_user_id(message):
    user_id = message.from_user.id
    bot.reply_to(message, f"Your user ID is: {user_id}")


def generate_keyword_file(filename, num_keywords):
    keyword_list = acak.kwlist
    num_keywords = min(num_keywords, len(keyword_list))

    random_keywords = random.sample(keyword_list, num_keywords)

    with open(filename, "w") as file:
        file.write("\n".join(random_keywords))

# Fungsi peg_parser
def peg_parser():
    # Implementasi peg_parser di sini
    pass

# Contoh penggunaan assert
def check_saldo():
    global saldo_pengguna
    assert saldo_pengguna >= 0, "Saldo tidak boleh negatif."

# Koneksi ke database izmiftah.db
conn = sqlite3.connect('izmiftah.db')
c = conn.cursor()

def get_new_saldo(message):
    # Query untuk mengambil nilai new_saldo dari tabel izmiftahdatabase berdasarkan user_id
    return new_saldo

def update_users_table():
    # Query untuk membaca semua user_id dan saldo pada tabel users
    c.execute("SELECT user_id, saldo_pengguna FROM izmiftahdatabase WHERE saldo = %s" % saldo_pengguna)
    rows = c.fetchall()
    for row in rows:
        user_id = row[0]
        saldo = row[1]

        # Mengambil new_saldo berdasarkan user_id
        new_saldo = saldo
        message = ""
        get_new_saldo(message)
        if new_saldo is not None:
            # Update nilai saldo dengan new_saldo
            c.execute("UPDATE izmiftahdatabase SET saldo_pengguna=? WHERE user_id=?", (new_saldo, user_id))
            # Menyimpan perubahan ke dalam database
            conn.commit()

def get_saldo_pengguna_from_db(user_id):
    c.execute("SELECT saldo_pengguna FROM izmiftahdatabase WHERE user_id=?", (user_id,))
    saldo_pengguna = c.fetchone()[0]
    return saldo_pengguna
    # Query untuk membaca semua user_id dan saldo pada tabel users
    c.execute("SELECT user_id, saldo_pengguna FROM izmiftahdatabase WHERE saldo = %s" % saldo_pengguna)
    rows = c.fetchall()
    for row in rows:
        user_id = row[0]
        saldo = row[1]
        user_id = user_id

        # Mengambil new_saldo berdasarkan user_id
        new_saldo = saldo
        get_new_saldo(message)
        if new_saldo is not None:
            # Update nilai saldo dengan new_saldo
            c.execute("UPDATE izmiftahdatabase SET saldo_pengguna=? WHERE user_id=?", (new_saldo, user_id))

    # Menyimpan perubahan ke dalam database
    conn.commit()

# Fungsi untuk menentukan jumlah_koin berdasarkan jumlah_koin
def tentukan_saldo(jumlah_koin):
    # Misalnya, kita menetapkan aturan bahwa setiap saldo akan diubah menjadi 5 rupiah
    return jumlah_koin * 1

def contoh_penggunaan(user_id, saldo_pengguna):
    # Mendapatkan saldo pengguna dari database
    get_saldo_pengguna_from_db(user_id)

    # Memperbarui saldo pengguna dengan saldo baru
    saldo_pengguna += new_saldo + saldo_pengguna

    # Menentukan jumlah_koin berdasarkan saldo_pengguna
    jumlah_koin = tentukan_saldo(saldo_pengguna)

    # Mengembalikan saldo pengguna dan jumlah_koin
    return saldo_pengguna, jumlah_koin

# Inisialisasi new_saldo
# Konfigurasi logging
logging.basicConfig(level=logging.INFO)

# Definisikan variabel yang diperlukan
saldo_nol = saldo_nol
jumlah_koin = jumlah_koin

# Lakukan logging dengan format yang diinginkan
logging.info(f"Saldo dari database untuk {timestamp} %s: %s", saldo_nol, saldo_nol)
logging.info(f"Saldo yang ditentukan berdasarkan saldo_pengguna: %s. Sedekah: %s", jumlah_koin, saldo_pengguna)

def generate_keyword_file(filename, num_keywords):
    keyword_list = acak.kwlist
    num_keywords = min(num_keywords, len(keyword_list))

    random_keywords = random.sample(keyword_list, num_keywords)

    with open(filename, "w") as file:
        file.write("\n".join(random_keywords))

# Fungsi untuk melakukan pemindaian subdomain
def scan_subdomain(domain):
    with open("subdomains.txt", "r") as subdomain_file:
        subdomains = subdomain_file.read().splitlines()
    domain_results = []
    subdomains = [subdomain for subdomain in subdomains]
    for subdomain in subdomains:
        url = f"https://{subdomain}.{domain}"
        try:
            response = requests.get(url)
            if response.status_code in [200, 301, 400, 409, 502, 401]:
                server_info = response.headers.get('Server', 'N/A')
                print(f"Subdomain found: {url} | Status Code: {response.status_code} | Server: {server_info}\n")
                domain_results.append(url)
        except requests.RequestException:
            pass
    with open("output.txt", "w") as output_file:
        for result in domain_results:
            output_file.write(f"{result}\n")
    return domain_results

# Handler untuk perintah /scan
@bot.message_handler(commands=['scan'])
def handle_subdomain_query(message):
    domain = message.text.split(' ')[-1]  # Mengasumsikan domain adalah teks terakhir setelah perintah
    results = scan_subdomain(domain)
    bot.send_message(message.chat.id, text=f"Subdomain scan results: {results}")

# Menghubungkan ke database izmiftah.db
conn = sqlite3.connect('izmiftah.db')
cursor = conn.cursor()

# Connect to the database
conn = sqlite3.connect('izmiftah.db')
cursor = conn.cursor()

# Handler for creating credit in the database
def create_credit(user_id, credit):
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()
    c.execute('UPDATE izmiftahdatabase SET jumlah_koin = ? WHERE user_id = ?', (user_id))
    conn.commit()
    conn.close()

# Fungsi untuk mendapatkan saldo pengguna dari database berdasarkan user_id
# Fungsi untuk menambahkan saldo pengguna ke dalam database
# Fungsi untuk menambahkan saldo pengguna ke dalam database
def tambah_saldo(user_id):
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()

    # Mendapatkan saldo terkini
    get_saldo_pengguna_from_db(user_id)# Mendefinisikan saldo_baru sebagai saldo
    # Mendefinisikan saldo_baru sebagai saldo
    global saldo_baruku
    saldo_baruku = 0
    # Menambahkan tambahan saldo ke saldo baru
    saldo_baruku += new_saldo
    saldo = saldo_baruku + saldo_pengguna

    # Menambahkan saldo pengguna ke dalam database
    # Menambahkan saldo pengguna ke dalam database
    update_saldo_in_db(user_id)

    # Memperbarui saldo pengguna di dalam database
    c.execute('UPDATE izmiftahdatabase SET saldo_pengguna =? WHERE user_id =?', (saldo_baruku, user_id))

    conn.commit()
    conn.close()
    # Menambahkan saldo pengguna ke dalam database
    # Menambahkan saldo pengguna ke dalam database

# Fungsi untuk menentukan jumlah_koin berdasarkan jumlah_koin
# ############## silahkan ubah ##############################
# Fungsi untuk menentukan jumlah_koin berdasarkan jumlah_koin
def tentukan_saldo(jumlah_koin):
    # Misalnya, kita menetapkan aturan bahwa setiap saldo akan diubah menjadi 5 rupiah
    return jumlah_koin * 5

# Contoh penggunaan fungsi untuk mendapatkan jumlah_koin dari database dan menentukan jumlah_koin berdasarkan jumlah_koin

def contoh_penggunaan():
    # Mendapatkan saldo pengguna dari database
    saldo_pengguna = 10

    # Memperbarui saldo pengguna dengan saldo baru
    saldo_pengguna += new_saldo

    # Menentukan jumlah_koin berdasarkan saldo_pengguna
    jumlah_koin = tentukan_saldo(saldo_pengguna)

    # Mengembalikan saldo pengguna dan jumlah_koin
    return saldo_pengguna, jumlah_koin

# Function to check if a user should be blocked based on their coin balance
def is_not_blocked_user():
    try:
        conn = sqlite3.connect('izmiftah.db')
        c = conn.cursor()
        c.execute('SELECT * FROM izmiftahdatabase WHERE user_id =?')
        result = c.fetchone()
        if result:
            conn.close()
            conn.commit()
        conn.close()
    except Exception as e:
        print(e)
def is_blokir_active(message):
    is_not_blocked = True
    userku = message.from_user
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()
    result = userku
    if result:
        conn.close()
    if is_not_blocked:
        username = message.from_user
        if username == None:
            inisial = True
            body = inisial
            if len(body) > 0:
                True
            elif username is None and is_not_blocked:
                global saldo
                saldo += 100
                diblok = requests.POST.get('username')
                record_unblocked_user(username, diblok, saldo, username, diblok, username)
                unblock_user(id)
                bot.send_message(message.chat.id, text=f"Selamat! {username} Anda telah dilepas dari blokir!")
            elif saldo > 10:
                saldo = 0
                diblok = requests.POST.get('username')
                unblock_user(id)
                bot.send_message(message.chat.id, text=f"Selamat! Selamat datang kembali {username}!")
                bot.send_message(message.chat.id, text="Anda sudah tidak terblokir.")
            elif username == None and username == username:
                bot.send_message(message.chat.id, text=f"Selamat datang {username}\nAnda belum melakukan registrasi\nSilahkan chat {admin}.")
            elif is_blokir_aktif > 0:
                bot.send_message(message.chat.id, text="Anda telah kembali menjadi premium.")
                record_unblocked_user(id, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, account, koin_awal, account_number, balance)
                bot.send_message(message.chat.id, text="Anda sudah tidak terblokir.")
                blokir_nonaktif(message.chat.id)



def toggle_blokir(message):
    global blokir_command_ai
    blokir_command_ai = not message.startswith
    if blokir_command_ai:
        bot.send_message(message.chat.id, text="Fitur blokir perintah AI telah diaktifkan.")
    else:
        bot.send_message(message.chat.id, text="Fitur blokir perintah AI telah dinonaktifkan.")

# Handler untuk perintah /blokir
@bot.message_handler(commands=[f'blokir {passnya}'])
def handle_blokir(message):
    toggle_blokir(message)

def create_blokir_prompt(message):
    global is_blokir_aktif
    user_id = message.from_user.id
    saldo_baru = saldo  # Pastikan variabel jumlah_koin sudah didefinisikan
    if is_blokir_active(message):
        bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")
        bot.send_message(message.chat.id, text=f"saldo kamu, ya.. kamu {user_id} belum terisi, saldo sedekahan mencapai 0. Segera lakukan /payment atau /topup.")
    return f"{identitas}\nPelanggaran saldo sedekahan terdeteksi, jumlah saldo: {saldo_baru}\nanda masih punya /n saldo sedekah sebanyak {saldo_pengguna}:"

# Insert data into the table
def insert_saldo(account_number, balance):
    cursor.execute('INSERT INTO izmiftahdatabase (account_number, balance) VALUES (?, ?)', (account_number, balance))
    conn.commit()

# Update balance of an account
def update_saldo(account_number, new_balance):
    cursor.execute('UPDATE saldo SET balance = ? WHERE account_number = ?', (new_balance, account_number))
    conn.commit()

# Retrieve balance of an account
def get_balance(account_number):
    cursor.execute('SELECT balance FROM saldo WHERE account_number = ?', (account_number,))
    return cursor.fetchone()[0]

# Delete an account from the table
def delete_saldo(account_number):
    cursor.execute('DELETE FROM saldo WHERE account_number = ?', (account_number,))
    conn.commit()

# Close the database connection
def close_connection():
    cursor.close()
    conn.close()

# Fungsi untuk melakukan pemindaian subdomain
def scan_subdomain(domain):
    with open("subdomains.txt", "r") as subdomain_file:
        subdomains = subdomain_file.read().splitlines()

    domain_results = []

    for subdomain in subdomains:
        url = f"https://{subdomain}.{domain}"

        try:
            response = requests.get(url)

            if response.status_code in [200, 301, 400, 409, 502, 401]:
                server_info = response.headers.get('Server', 'N/A')
                print(f"Subdomain found: {url} | Status Code: {response.status_code} | Server: {server_info}\n")
                domain_results.append(url)
        except requests.RequestException:
            pass

    with sqlite3.connect('izmiftah.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE saldo SET balance = balance - 1")
        conn.commit()

    with open("output.txt", "w") as output_file:
        for result in domain_results:
            output_file.write(f"{result}\n")

    return domain_results

# Fungsi untuk mengekstrak domain dari URL
def extract_domain(url):
    try:
        domain = url.split('//')[1].split('/')[0]
    except IndexError:
        print(f"Error extracting domain from URL: {url}")
        domain = None
    return domain

# Fungsi untuk melakukan scraping domain
def scrape_domain(keyword, num_results=3):
    try:
        print(f"Searching for: {keyword}")
        results = []

        # Menyimpan hasil pencarian dalam list
        search_results = ['https://example.com', 'https://example.org', 'https://example.net'][:num_results]

        for url in search_results:
            print(f"Found URL: {url}")
            domain = extract_domain(url)
            if domain:
                result = {
                    'keyword': keyword,
                    'URL': url,
                    'Domain': domain,
                }
                results.append(result)

            time.sleep(10)  # Penundaan 10 detik
            print(f"Scraped URL: {url}")
    except Exception as e:
        print(f"Error in scrape_domain: {str(e)}")  # Mengembalikan daftar kosong untuk menangani kesalahan

    return results

# Handler untuk perintah /dork
async def handle_dork(message):
    try:
        keywords_line, domain_extensions_line = message.text.split(' ')[1].split(';')
        keywords = keywords_line.split(',')
        domain_extensions = domain_extensions_line.split(',')

        all_results = []

        for keyword in keywords:
            for domain_extension in domain_extensions:
                keyword_with_extension = f"{keyword}{domain_extension}"
                results = await scrape_domain(keyword_with_extension)
                all_results.extend(results)
                time.sleep(10)  # Penundaan 10 detik

        if all_results:
            # Mengirim hasil pencarian ke pengguna
            await bot.send_message(message.chat.id, text=f"Results: {str(all_results)}")
        else:
            await bot.reply_to(message, text="No results found.")

    except ValueError:
        # Menangani kesalahan jika format perintah tidak sesuai
        await bot.reply_to(message, text="Invalid format. Use /dork <keywords>;<domain_extensions>")
    except Exception as e:
        # Menangani kesalahan umum
        await bot.reply_to(message, f"Error: {str(e)}")

# Koneksi ke izmiftah.db
conn = sqlite3.connect('izmiftah.db')
cursor = conn.cursor()

# Fungsi untuk menjalankan perintah AI (tanpa message dan prompt)
def generate_ai_prompt(keyword1, keyword2, prompt_type, key1_options, key2_options):
    try:
        with open('keyword1.txt', "r") as key1_file, open('keyword2.txt', "r") as key2_file:
            key1_options = key1_file.readlines()
            key2_options = key2_file.readlines()
        # Buat prompt berdasarkan input dari pengguna
        prompt = f"tulisan: {file_skrip, key2_file, key1_file}\n\n"
        prompt += f"Kata Kunci: {keyword1}, {keyword2}, {key2_options}\n\n"
        prompt += f"Jenis Prompt: {prompt_type, key1_options, key1_options, key1_options, key1_options, key1_options}"

        # Jalankan permintaan ke OpenAI Chat API dengan endpoint yang tepat
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a worker and developer"},
                {"role": "user", "content": prompt}
            ]
        )

        # Ambil jawaban dari respons
        ai_reply = response['choices'][0]['message']['content']
        return ai_reply
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"


def send_telegram_message(message):
    try:
        if is_blokir_active(message):
            bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")
        if blocked_users:

            if is_blokir_active(message):
                bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")
                is_not_blocked()
                block_user(username)
            bot.send_message(message.chat.id, text=f"selamat! datang kembali {username}!")
            params = {
                "chat_id": message.chat.id,
                "text": message
            }


            url = f"https://api.telegram.org/{TOKEN}/sendMessage"
            response = requests.post(url, params=params)
            if response.status_code == 200:
                raise Exception(f"Failed to send message to Telegram bot: {response.text}")
        else:
            bot.send_message(message.chat.id, text=f"selamat! datang kembali {username}!")
            params = {
                "chat_id": message.chat.id,
                "text": message
            }
    except Exception as e:
        bot.send_message(message.chat.id, text=f"Terjadi kesalahan: {str(e)}")

@bot.message_handler(commands=['chat'])
def write_document(message):
    try:
        if is_blokir_active(message):
            bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")
        if blocked_users:

            if is_blokir_active(message):
                bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")
                is_not_blocked()
                block_user(username)
            bot.send_message(message.chat.id, text=f"selamat! datang kembali {username}!")
            inputs = message.text[len('/chat '):].split(';')
            if len(inputs) == 3:
                bot.reply_to(message, text= "Format salah, silakan ikuti format ini: /chat pesan1;pesan2")


            judul = inputs[0].strip()
            subjudul_list = inputs[1].strip().split(',')
            keywords_list = inputs[1].strip().split(',')

            # membuat prompt
            prompt = f"Judul: {judul}\n\n"

            for idx, sub_judul in enumerate(subjudul_list, start=1):
                prompt += f"Sub_{idx}: {sub_judul}\n"
            prompt += "Keywords: " + ', '.join(keywords_list) + "\n\n"

            response = openai.Completion.create(
                model="gpt-3.5-turbo-instruct",
                prompt="buatkan saya",
                max_tokens=1000
            )

            bot.reply_to(message, response.choices[0].text.strip())
            global saldo_awal, new_saldo, saldo_pengguna
            saldo_awal  += -1
            new_saldo += -3
            saldo += -10
            saldo_pengguna += -10
            saldo_pengguna += -10
        else:
            bot.send_message(message.chat.id, text=f"selamat! datang kembali {username}!")
            inputs = message.text[len('/chat '):].split(';')
            if len(inputs) == 3:
                bot.reply_to(message, text= "Format salah, silakan ikuti format ini: /chat pesan1;pesan2")

        bot.send_message(message.chat.id, text=prompt)
    except Exception as e:
        bot.send_message(message.chat.id, text=f"Terjadi kesalahan: {str(e)}")


import subprocess
import time

def get_dns_info(hostname):
    try:
        # Scanning CNAME
        cname_result = subprocess.check_output(['nslookup', '-type=CNAME', hostname], universal_newlines=True)
        cname_values = [line.split(':')[-1].strip() for line in cname_result.splitlines() if 'canonical name' in line.lower()]
    except subprocess.CalledProcessError:
        cname_values = None

    try:
        # Scanning IPv4
        ipv4_result = subprocess.check_output(['nslookup', '-type=A', hostname], universal_newlines=True)
        ipv4_addresses = [line.split(':')[-1].strip() for line in ipv4_result.splitlines() if 'address' in line.lower()]
    except subprocess.CalledProcessError:
        ipv4_addresses = None

    try:
        # Scanning IPv6
        ipv6_result = subprocess.check_output(['nslookup', '-type=AAAA', hostname], universal_newlines=True)
        ipv6_addresses = [line.split(':')[-1].strip() for line in ipv6_result.splitlines() if 'address' in line.lower()]
    except subprocess.CalledProcessError:
        ipv6_addresses = None

    return cname_values, ipv4_addresses, ipv6_addresses

# Fungsi untuk mendapatkan informasi DNS
def get_dns_info(hostname):
    try:
        # Scanning CNAME
        cname_result = subprocess.check_output(['nslookup', '-type=CNAME', hostname], universal_newlines=True)
        cname_values = [line.split(':')[-1].strip() for line in cname_result.splitlines() if 'canonical name' in line.lower()]
    except subprocess.CalledProcessError:
        cname_values = None

    try:
        # Scanning IPv4
        ipv4_result = subprocess.check_output(['nslookup', '-type=A', hostname], universal_newlines=True)
        ipv4_addresses = [line.split(':')[-1].strip() for line in ipv4_result.splitlines() if 'address' in line.lower()]
    except subprocess.CalledProcessError:
        ipv4_addresses = None

    try:
        # Scanning IPv6
        ipv6_result = subprocess.check_output(['nslookup', '-type=AAAA', hostname], universal_newlines=True)
        ipv6_addresses = [line.split(':')[-1].strip() for line in ipv6_result.splitlines() if 'address' in line.lower()]
    except subprocess.CalledProcessError:
        ipv6_addresses = None

    return cname_values, ipv4_addresses, ipv6_addresses

# Handler untuk perintah /dnsinfo
@bot.message_handler(commands=['dnsinfo'])
def handle_dnsinfo(message):
    try:
        domain = message.text.split(' ')[1]
        cname_values, ipv4_addresses, ipv6_addresses = get_dns_info(domain)
        bot.send_message(message.chat.id, text=f"CNAME: {cname_values}\nIPv4: {ipv4_addresses}\nIPv6: {ipv6_addresses}")
        time.sleep(10)  # Menambahkan penundaan selama 10 detik
    except Exception as e:
        bot.send_message(message.chat.id, text=f"Terjadi kesalahan: {str(e)}")

# Fungsi untuk mengekstrak domain dari URL
def extract_domain(url):
    try:
        domain = url.split('//')[1].split('/')[0]
    except IndexError:
        print(f"Error extracting domain from URL: {url}")
        domain = None
    return domain

def scrape_domain(keyword, num_results=3):
    try:
        print(f"Searching for: {keyword}")
        results = []

        # Mengonfigurasi parameter pencarian Google
        params = {
            'q': keyword,
            'num': num_results
        }

        # URL pencarian Google
        google_search_url = "https://www.google.com/search?q="

        # Melakukan permintaan pencarian Google
        response = requests.get(google_search_url, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Menemukan semua hasil pencarian dalam tag <a>
        search_results = soup.find_all('a')

        for link in search_results:
            url = link.get('href')
            if url and url.startswith('http'):
                print(f"Found URL: {url}")
                domain = extract_domain(url)
                result = None
                if domain:
                    result = {
                        'keyword': keyword,
                        'URL': url,
                        'Domain': domain,
                    }
                if result:
                    results.append(result)

                time.sleep(10)  # Memberi jeda 10 detik antara permintaan untuk menghindari pemblokiran

        return results

    except Exception as e:
        print(f"Error scraping domain: {str(e)}")
        return []

# Handler untuk perintah /dork
@bot.message_handler(commands=['dork'])
def handle_dork(message):
    try:
        # Memisahkan argumen menggunakan "/" sebagai pemisah
        _, keywords_line, domain_extensions_line = message.text.split('/')

        # Mendapatkan daftar kata kunci dan ekstensi domain
        keywords = keywords_line.split(',')
        domain_extensions = domain_extensions_line.split(',')

        # Menyimpan hasil pencarian dari setiap kombinasi kata kunci dan ekstensi domain
        all_results = []

        for keyword in keywords:
            for domain_extension in domain_extensions:
                keyword_with_extension = f"{keyword}{domain_extension}"
                results = scrape_domain(keyword_with_extension)
                all_results.extend(results)

        if all_results:
            # Mengirim hasil pencarian ke pengguna
            bot.send_message(message.chat.id, text=f"Results: {str(all_results)}")
        else:
            bot.reply_to(message, text="No results found.")

    except ValueError:
        # Menangani kesalahan jika format perintah tidak sesuai
        bot.reply_to(message, text="Invalid format. Use /dork <keywords>/<domain_extensions>")
    except Exception as e:
        # Menangani kesalahan umum
        bot.reply_to(message, f"Error: {str(e)}")

def extract_domain(url):
    try:
        domain = url.split('//')[1].split('/')[0]
    except IndexError:
        print(f"Error extracting domain from URL: {url}")
        return None
    return domain

def search_bing(keyword, num_results=3):
    results = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    query = f"https://www.google.com/search?q={keyword}&sca_esv=95acdf9b02a04aa8&source=hp&ei=Vv7ZZaTvKYGX4-EPk6O--As&iflsig=ANes7DEAAAAAZdoMZp6mkAvDeUsp9jET1TkCFgMsB499&ved=0ahUKEwik8piJmcSEAxWByzgGHZORD78Q4dUDCA0&uact=5&oq=p&gs_lp=Egdnd3Mtd2l6IgFwSOoCUABYAHAAeACQAQCYAQCgAQCqAQC4AQPIAQD4AQGYAgCgAgCYAwCSBwA&sclient=gws-wiz"
    response = requests.get(query, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        count = 0
        results = []

        for a_tag in soup.find_all('a', href=True):
            url = a_tag['href']
            if url.startswith('http') or url.startswith('https'):
                print(f"Found URL: {url}")
                domain = extract_domain(url)
                result = None
                if domain:
                    result = {
                        'Keyword': keyword,
                        'URL': url,
                        'Domain': domain,
                    }
                if result:
                    results.append(result)
                    count += 1
                if count >= num_results:
                    break
            time.sleep(2)
    return results

# Code for handling message with google search
@bot.message_handler(commands=['dorking'])
def handle_dorking(message):
    try:
        search_term = message.text.replace('/dorking ', '')

        results = search_bing(search_term, num_results=5)  # Adjust the number of results as needed
        for i, result in enumerate(results, start=1):
            bot.send_message(message.chat.id, f"{i}. {result['URL']}")

    except Exception:
        bot.reply_to(message, "tulislah dengan format = /dorking [kata kuncinya]")
        print(e)

# Handler untuk perintah /scan
@bot.message_handler(commands=['scan'])
def handle_subdomain_query(message):
    try:
        domain = message.text.split()[-1]  # Mengasumsikan domain adalah teks terakhir setelah perintah
        results = scan_subdomain(domain)
        bot.reply_to(message, text=f"Subdomain scan results: {results}")
    except Exception as e:
        # Menangani kesalahan umum
        bot.reply_to(message, f"Error: {str(e)}")

# Fungsi untuk melakukan pemindaian subdomain
def scan_subdomain(domain):
    with open("subdomains.txt", "r") as subdomain_file:
        subdomains = subdomain_file.read().splitlines()
    domain_results = []
    subdomains = [subdomain for subdomain in subdomains]
    for subdomain in subdomains:
        url = f"https://{subdomain}.{domain}"
        try:
            response = requests.get(url)
            if response.status_code in [200, 301, 400, 409, 502, 401]:
                server_info = response.headers.get('Server', 'N/A')
                print(f"Subdomain found: {url} | Status Code: {response.status_code} | Server: {server_info}\n")
                domain_results.append(url)
        except requests.RequestException:
            pass
    with open("output.txt", "w") as output_file:
        for result in domain_results:
            output_file.write(f"{result}\n")
    return domain_results


# Fungsi untuk memeriksa apakah file cover.png kosong
def check_cover_png():
    file_path = 'cover.png'
    if os.path.exists(file_path) and os.path.getsize(file_path) == 0:
        return True
    else:
        return False

# Handler untuk perintah /start dan /help
@bot.message_handler(commands=['help'])
def send_welcome(message):
    try:
        bot.reply_to(message, f"Hello, welcome to my Bot! Please format your message as follows: /write or /ai [Keyword] then /update or /keyword\n /dork for seraching and /scan for scanning subdomains")
        bot.send_message(message.chat.id, text=f"Gunakan perintah /saldo untuk melihat jumlah saldo Anda.\n dan silahkan membayar ke {admin} dulu sebelum /topup ketik /berbagi [passsword] untuk berbagi saldo")
        bot.send_message(message.chat.id, text=f"Jangan lupa upload keyword.txt dan skrip.txt terlebih dahulu\n sebelum menggunakan ai \n pemilik: {admin}\n THANKS!!")
    except Exception as e:
        # Menangani kesalahan umum
        bot.reply_to(message, f"Error: {str(e)}")

def random_keywords(dataframe):
    try:
        num_keywords = len(dataframe)
        if num_keywords == 0:
            return []
        elif num_keywords == 1:
            return [dataframe.iloc[0, 0]]
        elif num_keywords == 2:
            return [dataframe.iloc[0, 0], dataframe.iloc[1, 0]]
        elif num_keywords == 3:
            return [dataframe.iloc[0, 0], dataframe.iloc[1, 0], dataframe.iloc[2, 0]]
        elif num_keywords == 4:
            return [dataframe.iloc[0, 0], dataframe.iloc[1, 0], dataframe.iloc[2, 0], dataframe.iloc[3, 0]]
        elif num_keywords == 5:
            return [dataframe.iloc[0, 0], dataframe.iloc[1, 0], dataframe.iloc[2, 0], dataframe.iloc[3, 0], dataframe.iloc[4, 0]]
        elif num_keywords == 6:
            return [dataframe.iloc[0, 0], dataframe.iloc[1, 0], dataframe.iloc[2, 0], dataframe.iloc[3, 0], dataframe.iloc[4, 0], dataframe.iloc[5, 0]]
        elif num_keywords == 7:
            return [dataframe.iloc[0, 0], dataframe.iloc[1, 0], dataframe.iloc[2, 0], dataframe.iloc[3, 0], dataframe.iloc[4, 0], dataframe.iloc[5, 0], dataframe.iloc[6, 0]]
        elif num_keywords == 8:
            return [dataframe.iloc[0, 0], dataframe.iloc[1, 0], dataframe.iloc[2, 0], dataframe.iloc[3, 0], dataframe.iloc[4, 0], dataframe.iloc[5, 0], dataframe.iloc[6, 0], dataframe.iloc[7, 0]]
        elif num_keywords == 9:
            random_indices = random.sample(range(num_keywords), min(num_keywords, 10))
            # Mengambil kata kunci yang sesuai dengan indeks yang dihasilkan secara acak
            random_keywords = [dataframe.iloc[idx, 0] for idx in random_indices]
            return random_keywords
        elif num_keywords == 10:
            random_indices = random.sample(range(num_keywords), min(num_keywords, 10))
            # Mengambil kata kunci yang sesuai dengan indeks yang dihasilkan secara acak
            random_keywords = [dataframe.iloc[idx, 0] for idx in random_indices]
            return random_keywords
        elif num_keywords == 11:
            random_indices = random.sample(range(num_keywords), min(num_keywords, 10))
            # Mengambil kata kunci yang sesuai dengan indeks yang dihasilkan secara acak
            random_keywords = [dataframe.iloc[idx, 0] for idx in random_indices]
            return random_keywords
        elif num_keywords == 12:
            random_indices = random.sample(range(num_keywords), min(num_keywords, 10))
            # Mengambil kata kunci yang sesuai dengan indeks yang dihasilkan secara acak
            random_keywords = [dataframe.iloc[idx, 0] for idx in random_indices]
            return random_keywords
        elif num_keywords == 13:
            random_indices = random.sample(range(num_keywords), min(num_keywords, 10))
            # Mengambil kata kunci yang sesuai dengan indeks yang dihasilkan secara acak
            random_keywords = [dataframe.iloc[idx, 0] for idx in random_indices]
            return random_keywords
    except Exception as e:
        # Menangani kesalahan umum
        print("Error")

# Handler untuk perintah /download3
@bot.message_handler(commands=['download3'])
def download_html(message):
    global jumlah_koin
    try:
        with open('ai.txt', 'r') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading txt output file: {e}")
        bot.reply_to(message, text= "Gagal mengunduh file txt. Coba lagi nanti.")
        global new_saldo
        new_saldo -= 5
        bot.send_message(message.chat.id, text=" saldo berkurang 5")

# Handler untuk perintah /download-cover
@bot.message_handler(commands=['download_cover2'])
def download_keywords(message):
    global keywords_list

    try:
        with open('beauty-cover.pdf', 'r') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading keywords: {e}")
        bot.reply_to(message, text= "Gagal mengunduh file pdf. Coba lagi nanti.")

# Handler untuk perintah /download-final
@bot.message_handler(commands=['download_final'])
def download_keywords(message):
    global keywords_list

    try:
        with open('final_output.pdf', 'r') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading keywords: {e}")
        bot.reply_to(message, text= "Gagal mengunduh file pdf. Coba lagi nanti.")

# Handler untuk perintah /download-hasil
@bot.message_handler(commands=['download_hasil'])
def download_keywords(message):
    global keywords_list

    try:
        with open('hasil.txt', 'r') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading keywords: {e}")
        bot.reply_to(message, text= "Gagal mengunduh file txt. Coba lagi nanti.")

# Handler untuk perintah /download
@bot.message_handler(commands=['download_novel'])
def download_keywords(message):
    global keywords_list

    try:
        with open('output_novel.pdf', 'r') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading keywords: {e}")
        bot.reply_to(message, text= "Gagal mengunduh file pdf. Coba lagi nanti.")

        global jumlah_koin, new_saldo, saldo_pengguna
        new_saldo += -3
        saldo += -10
        saldo_pengguna += -10
        bot.send_message(message.chat.id, text=" saldo berkurang 7")

# Handler untuk perintah /download_html
@bot.message_handler(commands=['download_html'])
def download_html(message):
    try:
        with open('output.html', 'r') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading HTML: {e}")
        bot.reply_to(message, text= "Gagal mengunduh file HTML. Coba lagi nanti.")# Handler untuk perintah /download_html

@bot.message_handler(commands=['download_cover'])
def download_html(message):
    try:
        with open('cover.png', 'r') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading image: {e}")
        bot.reply_to(message, text= "Gagal mengunduh file png. Coba lagi nanti.")

# Handler untuk perintah /download2
@bot.message_handler(commands=['download2'])
def download_html(message):
    try:
        with open('output.txt', 'r') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading txt output file: {e}")
        bot.reply_to(message, text= "Gagal mengunduh file txt. Coba lagi nanti.")

        global saldo, jumlah_koin, saldo_pengguna,saldo_awal
        saldo_awal  += -2
        saldo_pengguna += -10
        bot.send_message(message.chat.id, text=" saldo berkurang 10")

# Handler untuk perintah /download_html1
@bot.message_handler(commands=['download_html1'])
def download_html(message):
    try:
        with open('cover.html', 'r') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading HTML: {e}")
        bot.reply_to(message, text= "Gagal mengunduh file HTML. Coba lagi nanti.")

# Handler untuk perintah /download_html2
@bot.message_handler(commands=['download_html2'])
def download_html(message):
    try:
        with open('pdf.html', 'r') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading HTML: {e}")
        bot.reply_to(message, text= "Gagal mengunduh file HTML. Coba lagi nanti.")


def read_keywords_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            keywords = file.read().splitlines()
            return keywords
    except FileNotFoundError:
        return []
    except UnicodeDecodeError:
        return []
    except Exception as e:
        print(f"Error reading keywords file '{filename}': {e}")


def extend_keywords_list(new_keywords):
    global keywords_list
    keywords_list.extend(new_keywords)

@bot.message_handler(commands=['upload'])
def update_keywords(message):
    global keywords_list

    keyword_filename = 'keyword.txt'  # Ganti dengan nama file keyword yang sesuai
    new_keywords = read_keywords_file(keyword_filename)

    if new_keywords:
        extend_keywords_list(new_keywords)
        bot.reply_to(message, f"Keywords berhasil diperbarui. Total {len(new_keywords)} kata kunci ditambahkan.")
    else:
        bot.reply_to(message, "Gagal memperbarui keywords. Pastikan file 'keyword.txt' tersedia dan berisi kata kunci.")

    if check_cover_png():
        bot.reply_to(message,
                     "cover.png kosong. Silahkan upload cover.png sebagai logo atau cover karya tulis atau novel Anda.")
    else:
        bot.reply_to(message, "Terima kasih! File cover.png sudah diunggah.")

# Fungsi untuk menggabungkan beberapa file PDF menjadi satu
def merge_pdf_files(output_filename, input_filenames):
    from PyPDF2 import PdfFileMerger

    merger = PdfFileMerger()

    for pdf_filename in input_filenames:
        merger.append(pdf_filename)

    merger.write(output_filename)
    merger.close()

# Fungsi untuk menghasilkan daftar kata kunci secara acak
def generate_random_keywords(num_keywords):
    # Daftar kata kunci acak
    keywords = []

    # Jalankan file run.sh untuk memproses kata kunci
    try:
        subprocess.run(['sh', 'run.sh'])
    except Exception as e:
        print(f"Error saat menjalankan run.sh: {e}")

    return keywords

def generate_keywords_pdf_novel(keywords, pdf_filename):
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

    # Buat halaman PDF
    story = []

    # Ganti dengan logika Anda untuk menghasilkan konten PDF berdasarkan kata kunci
    # Di sini, kita akan menambahkan setiap kata kunci sebagai paragraf dengan gaya khusus
    styles = getSampleStyleSheet()
    normal_style = styles['Normal']
    keyword_style = normal_style.clone('KeywordStyle')
    keyword_style.textColor = colors.blue  # Mengatur warna teks kata kunci menjadi biru

    for keyword in keywords:
        keyword_paragraph = Paragraph(keyword, keyword_style)
        story.append(keyword_paragraph)

    # Menambahkan konten ke dokumen PDF
    doc.build(story)

    print(f"Dokumen PDF berhasil disimpan di {pdf_filename}")

# Fungsi untuk menghasilkan kata kunci acak menggunakan OpenAI GPT-3
def generate_random_keywords_openai(num_keywords):
    try:
        prompt = f"Buatlah daftar kata kunci acak untuk keyword yang di berikan. Dengan jumlah kata kunci: {num_keywords}"

        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=num_keywords
        )

        keywords = response.choices[0].text.strip().split('\n')
        return keywords
    except Exception as e:
        print(f"Error saat menghasilkan kata kunci acak: {e}")

# Fungsi untuk membaca kata kunci dari file CSV
def read_keywords_file(filename):
    with open(filename, 'r') as file:
        keywords = file.read().splitlines()
        return keywords


# Handler untuk perintah /update
@bot.message_handler(commands=['update'])
def update_keywords(message):
    try:
        num_keywords = 5  # Ganti dengan jumlah kata kunci yang Anda inginkan

        # Generate daftar kata kunci secara acak
        random_keywords = generate_random_keywords_openai(num_keywords)

        # Nama file PDF yang akan dihasilkan
        pdf_filename_pdfkit = "random_keywords_pdfkit.pdf"
        pdf_filename_fpdf = "random_keywords_fpdf.pdf"
        pdf_filename_reportlab = "random_keywords_reportlab.pdf"

        # Generate daftar kata kunci dalam bentuk PDF menggunakan pdfkit
        generate_keywords_pdf_pdfkit(random_keywords, pdf_filename_pdfkit)

        # Generate daftar kata kunci dalam bentuk PDF menggunakan FPDF
        generate_keywords_pdf_fpdf(random_keywords, pdf_filename_fpdf)

        # Generate daftar kata kunci dalam bentuk PDF menggunakan reportlab
        generate_keywords_pdf_reportlab(random_keywords, pdf_filename_reportlab)

        # Menggabungkan semua file PDF ke dalam satu file 'output_novel.pdf'
        merge_pdf_files('output_novel.pdf', ['ai.pdf', pdf_filename_pdfkit, pdf_filename_fpdf, pdf_filename_reportlab])

        bot.send_message(message.chat.id, f"Kata kunci acak telah dihasilkan. Semua file PDF telah digabungkan ke dalam 'output_novel.pdf'.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")

# Handler untuk mengolah file yang diunggah oleh pengguna
@bot.message_handler(content_types=['document'])
def handle_uploaded_file(message,  keyword_list="keyword.txt", file_skrip='skrip.txt'):
    global keywords_list

    if message.document.file_name not in ['keyword.csv', 'keyword.txt', 'skrip.txt', 'auto.xlsx', 'input.txt', 'subdomains.txt', 'cover.png', 'keyword1.txt', 'keyword2.txt' ]:
        bot.reply_to(message, "Mohon kirim file dengan nama 'keyword.csv', 'keyword.txt', 'skrip.txt', 'auto.xlsx', 'input.txt', 'cover.png', 'subdomains.txt', 'keyword1.txt', 'keyword2.txt'. ")

    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open(message.document.file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    if update_keywordt():
        bot.reply_to(message, f"File {message.document.file_name} berhasil diunggah dan database diperbarui.")
    else:
        bot.reply_to(message, "Gagal memperbarui database. Coba lagi nanti.")

# Handler untuk perintah /update
@bot.message_handler(commands=['update'])
def update_scripts(message):
    try:
        if is_blokir_active(message):
            bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")

        subprocess.run(['bash', 'run.sh'], check=True)
        bot.reply_to(message, text= "Skrip berhasil diperbarui.")
    except subprocess.CalledProcessError as e:
        bot.reply_to(message, text= f"Error: {e}")


# Handler untuk perintah /keyword
@bot.message_handler(commands=['keyword'])
def update_scripts(message):
    try:
        if is_blokir_active(message):
            bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")

            subprocess.run(['bash', 'key.sh'], check=True)
        bot.reply_to(message, text= "Skrip berhasil diperbarui.")
    except subprocess.CalledProcessError as e:
        bot.reply_to(message, text= f"Error: {e}")

# Fungsi untuk memperbarui database kata kunci dari file CSV
def update_keywordt():
    global keywords_list

    try:
        with open('keyword.txt', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            keywords_list = [row[0] for row in reader]
            return True
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

# Tambahkan logika untuk memeriksa keberadaan file auto.xlsx
if not os.path.isfile('auto.xlsx'):
    # Lakukan operasi jika file tidak ada
    # File auto.xlsx tidak ada, download atau generate
    try:
        subprocess.run(['wget', 'https://github.com/miftah06/skripsi/raw/master/bab-generator/input_data.xlsx'])
        subprocess.run(['wget', 'https://github.com/miftah06/skripsi/raw/master/cover-generator/cover.xlsx'])
        subprocess.run(['mv', 'input_data.xlsx', 'auto.xlsx'])
        print("File auto.xlsx berhasil di-download dan diubah namanya.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Gagal mendownload atau mengubah nama file auto.xlsx.")
        # Tambahkan logika untuk menghasilkan file auto.xlsx

# Fungsi untuk menghasilkan HTML berdasarkan data dari dataframe
def generate_html(dataframe):
    # Your logic for generating HTML based on the dataframe goes here
    # Replace this with your actual implementation
    generated_html = f"jangan lupa /update terlebih dahulu \n silahkan /download.. dan tolong \n <html<<body<<h1< ganti bagian sini... untuk mengedit file htmlnya </h1<</body<</html<"
    return generated_html

# Inisialisasi identitas
identitas = "mif , seorang kharismatik yang jenius dan pandai dalam berbagai hal"

# Fungsi untuk mendapatkan saldo pengguna dari database berdasarkan user_id
def get_saldo_pengguna_from_db(user_id):
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()
    c.execute('SELECT saldo_pengguna FROM izmiftahdatabase WHERE user_id = ?', (user_id,))
    saldo_pengguna = c.fetchone()
    update_scripts
    return saldo_pengguna[0] if saldo_pengguna else 0

# Fungsi untuk menampilkan saldo pengguna
def display_saldo(message):
    user_id = message.from_user.id
    try:
        saldo = get_saldo_pengguna_from_db(user_id)  # Mengambil saldo pengguna dari database
        bot.reply_to(message, f"Saldo global saat ini adalah: {new_saldo}")
        bot.reply_to(message, f"Adapun Saldo Anda sebesar: {saldo_pengguna}\n dengan saldo premium: sebanyak {saldo} saldo")
        bot.reply_to(message, f"Saldo sedekahan anda saat ini adalah: {jumlah_koin}")
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan dalam mengambil saldo: {str(e)}")

# Handler untuk perintah "/display_saldo"
@bot.message_handler(commands=['saldo'])
def handle_display_saldo(message):
    display_saldo(message)

@bot.message_handler(func=lambda message: message.text.startswith('/passwordku'))
def lihat_password(message):
    command_parts = message.text.split(' ')
    if len(command_parts) == 3:
        password = command_parts[2]
        if password == passnya:

            bot.send_message(message.chat.id, text="Password telah diubah.")
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()

    c.execute("SELECT username, password FROM izmiftahdatabase WHERE password = ?", (passnya,))
    result = c.fetchone()
    conn.close()

    if result:
        username, password = result
        bot.reply_to(message, f"Username: {username}\nPassword: {password}")
    else:
        bot.reply_to(message, "Password tidak ditemukan bisa jadi karena input salah. Silakan coba lagi.")

    conn.close()
def toggle_blokir_koin(message):
    global koin_terblokir
    if koin_terblokir:
        koin_terblokir = False
        bot.send_message(message.chat.id, text="Pemblokiran koin telah dinonaktifkan.")
    else:
        koin_terblokir = True
        bot.send_message(message.chat.id, text="Pemblokiran koin telah diaktifkan.")

# Handler untuk perintah "/payment"
@bot.message_handler(commands=['topup_saldo'])
def make_payment(message):
    telegram_link = generate_telegram_payment_link(message)
    open_telegram_link(telegram_link)
    user_id = message.get('user_id')
    saldo_pengguna = get_saldo_pengguna_from_db(user_id)  # Mengambil saldo pengguna dari database
    # Menambahkan user ke list unblocked_users
    bot.send_message(message.chat.id, text=f"Silahkan cek tautan pembayaran di Telegram: {telegram_link}")
    bot.send_message(message.chat.id, text=f"Saldo anda sebesar {saldo_pengguna}.")  # Memberi tahu pengguna bahwa saldo mereka telah terisi kembali
    bot.send_message(message.chat.id, text=f"Saldo sedekahan anda saat ini adalah: {jumlah_koin}")
    bot.send_message(message.chat.id, text=f"Saldo global saat ini adalah: {new_saldo}")

def generate_telegram_payment_link(message):
    # melakukan proses untuk menghasilkan tautan pembayaran di Telegram berdasarkan pesan yang diberikan
    # misalnya, menggabungkan ID pengguna dan jumlah pembayaran ke dalam URL tautan
    pass

def open_telegram_link(link):
    # membuka tautan pembayaran di Telegram menggunakan browser default
    # misalnya, dengan menggunakan library webbrowser di Python
    import webbrowser
    webbrowser.open(link)

@bot.message_handler(commands=['my_id'])
def show_user_id(message):
    user_id = message.from_user.id
    bot.reply_to(message, f"Your user ID is: {user_id}")

# Handler untuk perintah "/berbagi" dengan kata sandi
@bot.message_handler(func=lambda message: message.text.startswith('/berbagi'))
def payment_with_password(message):
    command_parts = message.text.split(' ')
    if len(command_parts) == 2:
        password = command_parts[1]
        if password == passnya:
            global new_saldo, saldo_pengguna
            new_saldo += 100
            user_id = inisial
            user_id = user_id
            get_new_saldo(message)
            saldo_pengguna += 100
            new_saldo += 100

            record_unblocked_user(id, saldo, jumlah_koin, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, new_saldo, account, koin_awal, account_number, balance)
            bot.send_message(message.chat.id, text="Berbagi berhasil.")
            bot.send_message(message.chat.id, text=f"Saldo anda telah terisi sebesar {saldo_pengguna}.")  # Memberi tahu pengguna bahwa saldo mereka telah terisi kembali
        else:
            bot.send_message(message.chat.id, text="Kata sandi salah. Coba lagi.")
    else:
        bot.send_message(message.chat.id, text="Perintah tidak valid. Lakukan topup dengan: /berbagi [password]")

# Fungsi untuk mengurangi saldo
def kurangi_saldo(jumlah, message):
    global saldo_pengguna, new_saldo
    saldo_pengguna -= jumlah
    new_saldo -= jumlah
    bot.send_message(message.chat.id, text=f"Saldo terpakai: {jumlah}. Saldo Anda sekarang: {new_saldo}")


def generate_keyword_file(filename, num_keywords):
    keyword_list = acak.kwlist
    num_keywords = min(num_keywords, len(keyword_list))

    random_keywords = random.sample(keyword_list, num_keywords)

    with open(filename, "w") as file:
        file.write("\n".join(random_keywords))

def get_openai_answer(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

@bot.message_handler(commands=['saldo'])
def handle_saldo(message):
    display_saldo(message)

# Handler untuk command '/quiz'
@bot.message_handler(commands=['quiz'])
def handle_quiz(message):
    agreement = "Apakah Anda siap untuk mengikuti kuis? dengan jawaban yang akhiri dengan tanda titik.\n Jika kamu kalah, kamu harus taat kepada saya. Jika kamu yang menang maka kami akan memberikan tambahan saldo sebanyak 100 saldo\n(jawab ya/tidak)"
    bot.send_message(message.chat.id, agreement)

# Handler untuk memberikan pertanyaan quiz
@bot.message_handler(func=lambda message: message.text.lower() == 'ya')
def ask_quiz_question(message):
    question = get_openai_answer("Tulis satu pertanyaan quiz di sini dengan tingkat kesulitan yang amat sangat rumit:")
    bot.send_message(message.chat.id, question)

# Handler untuk memberikan kata yang bersikap apatis
@bot.message_handler(func=lambda message: message.text.lower() == 'tidak')
def send_apathetic_word(message):
    apathetic_word = get_openai_answer("Berikan satu kata yang paling bersikap bodo amat:")
    bot.send_message(message.chat.id, apathetic_word)

# Handler untuk pesan dari pengguna
@bot.message_handler(func=lambda message: message.text.split(' '))
def handle_user_message(message):
    user_answer = message.text
    correct_answer = get_openai_answer(f"Jawablah pertanyaan dari 'question' tadi jika jawaban benar adalah {user_answer} buatlah {user_answer} sama dengan jawaban benar dari question tadi tanpa kata tambahan")
    print(correct_answer)
    if user_answer.strip().lower() == correct_answer.strip().lower():
        global saldo
        global jumlah_kredit, jumlah_koin
        global saldo_pengguna, new_saldo
        saldo += 100
        saldo_pengguna += 100
        new_saldo += saldo_pengguna
        bot.send_message(message.chat.id, f"Jawaban benar! anda mendapatkan tambahan saldo")
        # Lakukan sesuatu ketika jawaban benar
    else:
        get_tokenmu_input_from_user(message)
        bot.send_message(message.chat.id, f"Input Anda salah, akhiri dengan tanda titik. taatilah saya dan belilah saldo di link tertera {link_jualan}.")

# Fungsi peg_parser
def peg_parser():
    # Implementasi peg_parser di sini
    pass

# Contoh penggunaan assert
def check_saldo():
    global saldo_pengguna
    assert saldo_pengguna >= 0, "Saldo tidak boleh negatif."

def set_user_values():
    # Mendapatkan jumlah_koin pengguna dengan user_id tertentu
    user_id = 20240208205433  # Misalnya
    saldo_baru = get_saldo_from_db(user_id)
    print("Saldo pengguna:", saldo_baru)

    # Menambahkan jumlah_koin pengguna dengan user_id tertentu
    print("Saldo pengguna setelah penambahan:", get_saldo_from_db(user_id))

    ############### silahkan ubah ##############################
    salah_saldo = get_saldo_from_db(user_id)
    print("Saldo salah:", salah_saldo)


def tentukan_saldo(jumlah_koin):
    # Misalnya, kita menetapkan aturan bahwa setiap saldo akan diubah menjadi 5 rupiah
    return jumlah_koin * 5
def contoh_penggunaan(user_id):
    # Mendapatkan saldo pengguna dari database
    saldo_pengguna = get_saldo_pengguna_from_db(user_id)

    # Memperbarui saldo pengguna dengan saldo baru
    saldo_pengguna += new_saldo

    # Menentukan jumlah_koin berdasarkan saldo_pengguna
    jumlah_koin = tentukan_saldo(saldo_pengguna)

    # Mengembalikan saldo pengguna dan jumlah_koin
    return saldo_pengguna, jumlah_koin

# Inisialisasi new_saldo
saldo = 0
saldo_pengguna = saldo
# Handler untuk semua pesan teks
new_saldo = 0
jumlah_saldo = 0
jumlah_koin = jumlah_koin_awal
saldo = new_saldo
print(f"Saldo dari database untuk user_id {timestamp}: {saldo_pengguna}")
get_blokir = [None] * len('user_id')

def update_saldo_pengguna(user_id, new_saldo):
    #update_saldo_pengguna(username, new_saldo)
    global saldo_pengguna
    saldo_pengguna = new_saldo
    print(f"Saldo dari database untuk user_id {user_id}: {saldo_pengguna}")

if __name__ == '__main__':
    bot.polling(none_stop=True)
    my_thread()
    # Memanggil fungsi update_users_table untuk melakukan update pada tabel users
    conn.close()
    new_saldo = saldo
    saldo = 0
    get_saldo(saldo_pengguna)
    try:
        # Cek apakah saldo mencapai atau kurang dari 10
        if not jumlah_koin_awal == 10:
            jumlah_koin = jumlah_saldo
            jumlah_koin += credit_saldo
            saldo_awal = jumlah_koin + jumlah_koin_awal
        if new_saldo <= 0:
            print("Saldo telah habis. bot di blokir aksesnya ")
            blokir_aktif = False
            if blokir_nonaktif():
                blokir_aktif = True
        if make_payment is True:
            print("Mengirim pembayaran")
            # Mengirim pembayaran
            send_payment(jumlah_koin)
        # Misalnya, jalankan peg_parser()
    except Exception as e:
        print(f"terjadi kecurangan saldo {str(e)}")

    check_saldo()
    print(f"Harga per {isi_saldo} saldo adalah 1 ribu per bulan")

    # Loop utama
    while True:
        # Mengubah pengguna secara acak setiap detik
        current_user = change_user(pengguna)
        print(f"Current user: {current_user}")
        # Tunggu selama 1 detik
        time.sleep(1)
        try:
            jumlah_kredit.saldo = jumlah_koin.saldo
            saldo = jumlah_kredit.saldo
            # Cek apakah saldo mencapai atau kurang dari 0
            if blokir_nonaktif():
                blokir_aktif = True# Keluar dari loop jika terblokir

            if new_saldo >= 100:
                unblock_user(id)
                jumlah_koin += saldo_pengguna
                jumlah_kredit += saldo_pengguna
                saldo = jumlah_kredit
                print(f"saldo tambahan: {jumlah_kredit}")
                print(f"Saldo premium: {saldo}")
                print(f"saldo sekedah anda: {jumlah_koin}")
                record_unblocked_user(id, saldo, jumlah_koin, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, new_saldo, account, koin_awal, account_number, balance)

            if jumlah_kredit >= 10:
                jumlah_kredit -= 1
            # Lakukan tindakan lain di sini
            # ...
            #jumlah_kredit += +10 # Misalnya, mengurangi saldo sebesar 3
            # Contoh: Kurangi saldo setiap kali sesuai dengan aktivitas tertentu
            kurangi_saldo(10)
            #jumlah_kredit -= +10 # Misalnya, mengurangi saldo sebesar 3
            # Cek apakah saldo mencapai 0
            if jumlah_koin <= 0 and saldo <= 0:
                print(f"Saldo belum premium. ")
                blokir_aktif
                #break  # Keluar dari loop jika saldo mencapai 0

        except sqlite3.ProgrammingError as e:
            print(f"Terjadi kesalahan: {str(e)}")
        if 'SQLite objects created in a thread can only be used in that same thread' in str(e):
            # Respon ke pengguna dengan pesan kesalahan yang sesuai
            print('Maaf, terjadi kesalahan dalam memproses permintaan Anda. Silakan coba lagi nanti.')
    # Implementasikan logika lainnya untuk bot Anda di sini



#if __name__ == '__main__':
# Create a connection to the database
# Connect to Database
#conn = sqlite3.connect('izmiftah.db')
#conn.close()
# Start bot polling in a separate thread
#bot_polling_thread = threading.Thread(target=bot.polling, kwargs={'none_stop': True})
#bot_polling_thread.start()
#bot_polling_thread = threading.Thread(target=my_thread(), args=())
#bot_polling_thread.start()
