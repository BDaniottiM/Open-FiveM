import importlib
import sys
import psutil
import subprocess
import webbrowser
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon
import os

def install_pip():
    try:
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--default-pip"])
        print("pip instalado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar pip: {e}")

def install_package(package_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"{package_name} instalado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar {package_name}: {e}")

if not importlib.util.find_spec("pip"):
    install_pip()

packages = ['psutil', 'PyQt5']
for package in packages:
    if not importlib.util.find_spec(package):
        install_package(package)


app = QApplication(sys.argv)
discord_url = "discord://https://discord.com/channels/865690041966919689/1018324428381229076"

fivem_url = "fivem://connect/kamikazegtarp.com.br?pure_1"

def check_process():
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if "FiveM.exe" in proc.info['name']:
            return True
    return False

def show_message_box(title, text, informative_text):
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(text)
    msg_box.setInformativeText(informative_text)
    msg_box.setWindowIcon(QIcon())
    msg_box.resize(800, 400)
    msg_box.setStyleSheet("QLabel{ font-size: 24px; }")
    msg_box.setWindowFlags(msg_box.windowFlags() | Qt.WindowStaysOnTopHint)
    subprocess.Popen(['start', discord_url], shell=True)
    
    msg_box.exec_()

def show_open_ponto_message():
    show_message_box("Abre o ponto", "Não esquece de abrir o ponto!", "Já abriu o ponto?")
    webbrowser.open(fivem_url)

def show_fechar_ponto_message():
    show_message_box("Fecha seu ponto", "Cê fechou o fivem, agora fecha o ponto!", "Obrigado, agora não vai tomar ADV")

show_open_ponto_message()

if check_process():
    procs = psutil.process_iter(attrs=['pid', 'name'])
    fivem_procs = [p for p in procs if "FiveM.exe" in p.info['name']]
    psutil.wait_procs(fivem_procs)
    show_fechar_ponto_message()

sys.exit(app.exec_())