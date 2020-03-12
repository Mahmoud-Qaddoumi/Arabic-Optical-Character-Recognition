import pandas as pd
from glob import glob
#todo: change the dimention of picture
#todo: change type and size



filename = r'Al_maktaba.csv'
chunksize = 10 ** 6
for chunk in pd.read_csv(filename, chunksize=chunksize, encoding='utf-8'):
    for index, input_row in chunk.iterrows():
        import arabic_reshaper
        from bidi.algorithm import get_display
        from PIL import Image, ImageDraw, ImageFont
        input_text = input_row['text']
        reshaped_text = arabic_reshaper.reshape(input_text)
        bidi_text = get_display(reshaped_text)
        font = ImageFont.truetype('Arial', 20)
        image = Image.new('RGBA', (2000, 600), (255, 255, 255))
        image_draw = ImageDraw.Draw(image)
        image_draw.text((10, 10), bidi_text, fill=(0, 0, 0), font=font)
        img_name = str(input_row['Book_Number'] + "_" + input_row['Paragraph_No']) + '.PNG'
        image.save(img_name)
        print(index)








