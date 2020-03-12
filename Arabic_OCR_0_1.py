import pandas as pd
from glob import glob


def text_to_imapge(text):
    import arabic_reshaper
    from bidi.algorithm import get_display
    from PIL import Image, ImageDraw, ImageFont
    input_text = text['text']
    reshaped_text = arabic_reshaper.reshape(input_text)
    bidi_text = get_display(reshaped_text)
    font = ImageFont.truetype('Arial', 20)
    image = Image.new('RGBA', (2000, 600), (255, 255, 255))
    image_draw = ImageDraw.Draw(image)
    image_draw.text((10, 10), bidi_text, fill=(0, 0, 0), font=font)
    img_name = str(text['Book_Number'] + "_" + text['Paragraph_No']) + '.PNG'
    image.save(img_name)

filename = r'Al_maktaba.csv'
chunksize = 10 ** 6
for chunk in pd.read_csv(filename, chunksize=chunksize, encoding='utf-8'):
    for input_row in chunk:
        text_to_imapge(input_row)





