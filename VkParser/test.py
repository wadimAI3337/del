import re

texts = [
    '''Two NK UNISEX
    Material : Three-piece without fleece | Turkish
    Sizes: 48-54 OverSize
    Price : 1600
    Wholesale: 5pcs-1500₽
    The best for you!''',

    '''⚜  ⚜ ❤ 🌺 𝙉𝙀𝙒 𝘾𝙊𝙇𝙇𝙀𝘾𝙏𝙄𝙊𝙉 🌺 ❤ ⚜  ⚜

    ~~~~~~ 2A-75 Housing A ~~~~~~
    ▫ Jackets Classic Spring-Summer
    __________________________________
    ▫ Product Length: 72cm
    ▫ Production: FACTORY CHINA
    __________________________________
    ▫ Fabric: 75%Cotton 25%Spandex
    __________________________________
    ▫ Sizes: 42-48 Single
    __________________________________
    ▫ Price: 450₽ ‼ ‼ ‼
    __________________________________
    ▫ Product For The Marketplace ‼ ‼ ‼
    __________________________________
    📞 Number for ordering and receiving information: +7 (926 818 70 47)
    https://vk.com/kolyaxas'''
]

# remove lines containing "Wholesale", links, and phone numbers starting with +7 or 8
for i, text in enumerate(texts):
    texts[i] = re.sub(r".*Wholesale.*\n", "", text)
    texts[i] = re.sub(r"http\S+", "", texts[i])
    texts[i] = re.sub(r"\+?[78]\s?\(?\d{3}\)?\s?\d{3}\s?\-?\d{2}\s?\-?\d{2}", "", texts[i])

    # multiply price by 1.3
    price_match = re.search(r"Price : (\d+)", texts[i])
    if price_match:
        price = int(price_match.group(1))
        new_price = price * 1.3
        texts[i] = re.sub(r"Price : \d+", f"Price : {new_price:.2f}", texts[i])

print(texts[1])