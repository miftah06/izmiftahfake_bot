import os
import subprocess
import threading
import requests
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from dotenv import load_dotenv

class IzmiftahBot(toga.App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        load_dotenv('.env')
        self.api_token = os.getenv('token')
        self.openai_api_key = os.getenv('openai')
        self.sales_link = os.getenv('link')
        self.bot_password = os.getenv('password')

    def execute_command(self, widget):
        command = self.command_input.value.strip()
        if not command:
            self.result_label.text = 'Please enter a command.'
            return

        def run_command():
            try:
                output = subprocess.check_output(command, shell=True, text=True)
                self.result_label.text = output
            except subprocess.CalledProcessError as e:
                self.result_label.text = f"Error executing command: {e}"

        threading.Thread(target=run_command).start()

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=20))

        login_input_box = toga.Box(style=Pack(direction=ROW, padding=10))
        self.login_input = toga.TextInput(placeholder='message.from.user.id:')
        login_input_box.add(toga.Label('Chat ID Telegram Target:'))
        login_input_box.add(self.login_input)

        chat_input_box = toga.Box(style=Pack(direction=ROW, padding=10))
        self.chat_input = toga.TextInput(placeholder='Tulis pesan bot anda di sini')
        chat_input_box.add(toga.Label('Pesan:'))
        chat_input_box.add(self.chat_input)

        send_button = toga.Button('Kirim Pesan sebagai bot', on_press=self.send_message)

        command_box = toga.Box(style=Pack(direction=ROW, padding=10))
        self.command_input = toga.TextInput(placeholder='python3 izmiftah.py')
        command_box.add(toga.Label('Command pesan perintah ex: /sudo python3 izmiftah.py:'))
        command_box.add(self.command_input)

        execute_button = toga.Button('jalankan', on_press=self.execute_command)
        self.result_label = toga.Label('')

        main_box.add(login_input_box)
        main_box.add(chat_input_box)
        main_box.add(send_button)
        main_box.add(command_box)
        main_box.add(execute_button)
        main_box.add(self.result_label)

        self.main_window = toga.MainWindow(title='IzmiftahBot', size=(400, 400))
        self.main_window.content = main_box
        self.main_window.show()

    def send_message(self, widget):
        phone_number = self.login_input.value.strip()
        message = self.chat_input.value.strip()
        if not phone_number:
            self.result_label.text = 'Nomor telepon tidak boleh kosong.'
            return
        if len(phone_number) < 5:
            self.result_label.text = 'Target telegram harus memiliki setidaknya 5 digit pada ID nya.'
            return
        if not message:
            self.result_label.text = 'Pesan tidak boleh kosong.'
            return

        url = f'https://api.telegram.org/bot{self.api_token}/sendMessage'
        data = {
            'chat_id': phone_number,
            'text': message
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            self.result_label.text = 'Pesan Anda telah berhasil dikirim.'
        else:
            self.result_label.text = f'Terjadi kesalahan saat mengirim pesan: {response.text}'

def main():
    app = IzmiftahBot('Izmiftah Bot', 'myai.miftah.izmiftahbot')
    app.main_loop()

if __name__ == '__main__':
    main()
