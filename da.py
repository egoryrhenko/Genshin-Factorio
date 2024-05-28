import os
import requests
import pystray
from pystray import MenuItem as item
from PIL import Image
import threading
from pypresence import Presence

def download_icon(url, save_path):
    response = requests.get(url)
    response.raise_for_status()  # Проверяем, что запрос был успешным
    with open(save_path, 'wb') as file:
        file.write(response.content)

def background_task():
    RPC = Presence("1244978322862247937")
    RPC.connect()
    RPC.update(
        start="123",
        large_image="da"
    )

def on_quit(icon, item):
    icon.stop()

# Ссылка на иконку
icon_url = "https://cdn.discordapp.com/attachments/1119653686411526214/1245038223231815804/da.ico?ex=66574bb4&is=6655fa34&hm=dc3ac3fd9295bd79d903a9bd30a4f7b1ce6dc92efc4af58b91784d0f82c04009&"
# Путь для сохранения иконки
icon_path = os.path.join(os.path.dirname(__file__), "da.ico")

# Загружаем иконку по ссылке
download_icon(icon_url, icon_path)

# Загружаем иконку из файла
icon_image = Image.open(icon_path)

# Создаем иконку и меню
menu = (item('Вийти', on_quit),)
icon = pystray.Icon("test_icon", icon_image, "Геншин факторио", menu)

# Запускаем фоновую задачу в отдельном потоке
thread = threading.Thread(target=background_task)
thread.daemon = True
thread.start()

# Запускаем иконку в системном трее
icon.run()