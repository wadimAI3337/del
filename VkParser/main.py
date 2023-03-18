import re
from time import time
from parse_posts import collect_postData, get_wall_posts, divide_groups
from auth_data import symbol_assignments
from decode_sequence import encode_decode_sequence
from groups import groups

man_shoes = ["angryman_sadovod", "isroill1994", "simmodda", "178010144", "sadovod_store1"]
API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '6242446471:AAHAESMZObnxdDcbmnVl8Ti-dXfTvEtuAow'

gpath = "C:/Users/wadim.DESKTOP-ONBR3LG/PycharmProjects/VkParser/Groups/"
dpath = "C:/Users/wadim.DESKTOP-ONBR3LG/PycharmProjects/VkParser/Data/"
groups = ['216316323', 'smotrinashmotki']

chat_id: str = "@publi7773"

# get_wall_posts(groups_name=man_shoes)
# collect_postData(gpath, dpath=dpath, review=False)

# print(encode_decode_sequence("https://vk.com/wall" + "!#**@@%#=+?^^$$", symbol_assignments, encode=False))

text2 = """
⚜ ⚜❤🌺𝙉𝙀𝙒 𝘾𝙊𝙇𝙇𝙀𝘾𝙏𝙄𝙊𝙉🌺❤⚜ ⚜

~~~~~~ 2А-75 Корпус А ~~~~~~
▫Кроп-Топ Майки Лето Классические
_________________________________
▫Длина Изделия: 55см
▫ Производство: Сделано в РОССИИ
_________________________________
▫Ткань: 75%Хлопок 25%Эластин
_________________________________
▫Размеры: 42-50 Единый
_________________________________
▫Цена: 350₽ ‼‼‼
_________________________________
▫Товар Для Маркетплейса ‼‼‼
_________________________________
📞 Номер для заказа и получения информации: +7 (926 818 70 47)
https://vk.com/kolyaxas"""

text = """
Нет некрасивых женщин — есть только женщины, не знающие, что они красивы. (Вивьен Ли)
Повседневный костюм Adida$
Размеры: 42, 44, 46, 48, 50, 52
Длина кофты: 60см
Длина штанов: 100см
Цена: 1399₽
Материал: Турецкая Двухнитка ( Lux )
"""

text3 = """
✔Хайповые весенние куртка CALVIN KLEIN
✔Качество LUX LUX LUX 💪
✔Материал Плащовка ВЕСНА
✅Производства Фабричный Китай 🇨🇳
✅Размеры 46 48 50 52 54 🤗
✅Цена 1шт 2399 оптом дешевле
✅8 977 720 54 97 Хусейн ✍✍
✔Наши места САДОВОД 10.Линия 113.павильон
"""

# sizes = re.search(r'(?<=Размеры: ).+', text3, re.IGNORECASE)
# price = re.search(r'(?<=Цена: ).*', text3, re.IGNORECASE)

material = re.search(r'(?<=Материал: ).*', text3, re.IGNORECASE)
if material:
    print("Материал: ", material.group())
elif re.search(r"(?<=Ткань: ).*", text3, re.IGNORECASE):
    material = re.search(r"(?<=Ткань: ).*", text3, re.IGNORECASE)
    print("Материал: ", material.group())
# print("Размеры: ", sizes.group())
# print("Цена: ", price.group())
# print("Материал: ", material)

pattern_material = r'Материал(.+)'
pattern_tkan = r'Ткань(.+)'
match_mat = re.search(pattern_material, text2, re.IGNORECASE)
match_tk = re.search(pattern_tkan, text2, re.IGNORECASE)
if match_mat:
    print("Материал:", match_mat.group(1).strip(":").strip())
elif match_tk:
    print("Материал:", match_tk.group(1).strip(":").strip())