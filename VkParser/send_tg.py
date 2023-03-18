import os
import re
import json
import time

import requests
from auth_data import headers

API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '6242446471:AAHAESMZObnxdDcbmnVl8Ti-dXfTvEtuAow'
SECS = 30
offset: int = -2
counter: int = 0
chat_id: str = "@publi7773"

def test_request(url, retry, data, link):
    try:
        response = requests.post(url, data=data, headers=headers)
        print(f"\n[+] {link} {response.status_code}")
    except Exception as ex:
        time.sleep(SECS)
        if retry:
            print(f"[INFO] retry={retry} => {link}")
            return test_request(url=url, retry=(retry-1), data=data, link=link)
    return response

def send_message(text, photos, link, retry):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMediaGroup'
    media = []
    media.append({'type': 'photo', 'media': photos[0], 'caption': text})
    for photo in photos[1:]:
        media.append({'type': 'photo', 'media': photo})
    data = {
        'chat_id': chat_id,
        'media': json.dumps(media)
    }
    response = test_request(url, retry, data, link)
    return response.json()


def send_post(text_file, keywords):
    if not any(keyword.lower() in text_file.lower() for keyword in keywords):
        try:
            intro = "💌" + "Hey, ОБЗОР 😍\n\n"
            name = "✔" + "Наименование: " + text_file.split('\n')[0] + '\n'

            match_p = re.search(r'\d+р', text_file)
            if match_p:
                match_p = match_p.group().strip()
                match_p = match_p.split('р')[0]
            else:
                match_p = re.search(r'\n\d+', text_file).group().strip()
            price = "🏷" + "Цена: " + str(
                int(int(match_p) * 1.3)) + "₽\n"
            rating = "⭐" + "Рейтинг: " + re.search(r'\d+/\d\b', text_file).group() + '\n'
            link = "🔍" + "Ссылка: " + re.search(r"https?://\S+", text_file).group() + '\n'
            match = re.search(r'https://\S+', text_file)
            if match:
                text = "\n".join(
                    [line for line in text_file[match.end():].split("\n") if line.strip()])
                description = "✏" + "Описание: " + text
            else:
                print("Описание не подтягивается. Проверь регулярное выражение")
            full_text = intro + name + price + rating + link + description
            return full_text
        except:
            pass
