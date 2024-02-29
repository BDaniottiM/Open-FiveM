import sys
import psutil
import subprocess
import webbrowser
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon
import os

app = QApplication(sys.argv)
discord_url = "discord://https://discord.com/channels/865690041966919689/1018324428381229076"

# URL para abrir no navegador
fivem_url = "fivem://connect/kamikazegtarp.com.br?pure_1"

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
    msg_box.setWindowIcon(QIcon())  # Usa o ícone padrão do PyQt5

    # Define o tamanho da janela
    msg_box.resize(800, 400)

    # Define o tamanho do texto usando folhas de estilo
    msg_box.setStyleSheet("QLabel{ font-size: 24px; }")

    msg_box.setWindowFlags(msg_box.windowFlags() | Qt.WindowStaysOnTopHint)
    subprocess.Popen(['start', discord_url], shell=True)
    
    msg_box.exec_()

def show_open_ponto_message():
    show_message_box("Abre o ponto", "Não esquece de abrir o ponto!", "Não esquece de abrir a porra do ponto nesse caralho.")
    webbrowser.open(fivem_url)  # Abre a URL em uma nova aba do navegador

# Função para exibir a mensagem de fechamento
def show_fechar_ponto_message():
    show_message_box("Fecha seu ponto", "Cê fechou o fivem, agora fecha o ponto!", "Puta burra")

# Exibir a mensagem pedindo para abrir o ponto quando o FiveM for aberto
show_open_ponto_message()

# Verificar o status do aplicativo e esperar até que o FiveM seja fechado
if check_process():
    procs = psutil.process_iter(attrs=['pid', 'name'])
    fivem_procs = [p for p in procs if "FiveM.exe" in p.info['name']]
    psutil.wait_procs(fivem_procs)
    show_fechar_ponto_message()

sys.exit(app.exec_())
