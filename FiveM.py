import sys
import psutil
import subprocess
import webbrowser
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import urllib.request
import os

app = QApplication(sys.argv)

# Diretório onde a imagem está localizada
icon_dir = "assets/xtv77fi.png"
icon_path = os.path.join(icon_dir, 'icon.png')

# Função para verificar o status do aplicativo
def check_process():
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if "FiveM.exe" in proc.info['name']:
            return True
    return False

# Função para exibir a caixa de diálogo
def show_message_box(title, text, informative_text):
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(text)
    msg_box.setInformativeText(informative_text)
    msg_box.setWindowIcon(QIcon(icon_path))
    msg_box.resize(800, 400)
    msg_box.setStyleSheet("QLabel{ font-size: 24px; }")
    msg_box.setWindowFlags(msg_box.windowFlags() | Qt.WindowStaysOnTopHint)
    msg_box.exec_()

# URL para abrir no navegador
fivem_url = "fivem://connect/kamikazegtarp.com.br?pure_1"

def show_open_ponto_message():
    show_message_box("Abre o ponto", "O puta tonta!", "Não esquece de abrir a porra do ponto nesse caralho.")
    webbrowser.open(fivem_url)  # Abre a URL em uma nova aba do navegador

def show_fechar_ponto_message():
    show_message_box("Fecha seu ponto", "Cê fechou o fivem, agora fecha o ponto!", "Fecha o prompt também puta burra")

# Exibir a mensagem pedindo para abrir o ponto quando o FiveM for aberto
show_open_ponto_message()

sys.exit(app.exec_())
