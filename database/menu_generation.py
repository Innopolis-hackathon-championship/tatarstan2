from math import ceil, sqrt
from PIL import Image, ImageDraw, ImageFont
# from interaction_with_db import get_menu_for_photo
import asyncio


def re_size(photo_link, baze):
    photo = Image.open(photo_link)
    x, y = photo.size
    image_new = photo.crop((0, 0, min(x, y), min(x, y)))
    return image_new.resize((baze, baze))


def text_to_photo(id, name, price):
    font = ImageFont.truetype("ljk_Adventure-Subtitles.ttf", size=80)
    name_st = name
    price_st = 'Цена: ' + str(price)
    id_st = 'Номер: ' + str(id)
    text = name_st + '\n' + id_st + '\n' + price_st
    text_image = Image.new("RGB", (1000, 1000), '#FFFFFF')
    imgDrawer = ImageDraw.Draw(text_image)
    left, top, right, bottom = imgDrawer.multiline_textbbox((0, 0), text, font=font, align="center")
    right = ceil(right)
    bottom = ceil(bottom)
    text_image2 = Image.new("RGB", (right, bottom), '#FFFFFF')
    imgDrawer = ImageDraw.Draw(text_image2)
    imgDrawer.multiline_text((0, 0), text, fill=(0, 0, 0), align="center", font=font)
    return [(right - left + 1), text_image2]


def create_menu(menu_table):
    # число продуктов достается из таблицы
    number_prod = len(menu_table)
    # дальше известные переменные (до цикла)
    inline_n = ceil(sqrt(number_prod))
    column_n = ceil(number_prod / inline_n)
    baze = 1000
    add_text = 300
    dif = 50
    x = inline_n * (baze + dif) + dif
    final_photo = Image.new("RGB", (inline_n * (baze + dif) + dif, column_n * (baze + add_text + dif) + dif),
                            ('#FFFFFF'))
    line = 1
    column = 1
    line_n_add = number_prod % inline_n
    # цикл перебирает таблицу
    for i in range(number_prod):
        # продукт и линка достаются из таблицы
        product = menu_table[i]
        link = f'photos/{product[3]}'
        # дальше только известные переменные
        prod_im = re_size(link, baze)
        if line_n_add != 0 and number_prod - (column - 1) * inline_n < inline_n:
            dif2 = (x - line_n_add * baze) // (line_n_add + 1)
            final_photo.paste(prod_im,
                              (dif2 * line + baze * (line - 1), dif * column + (baze + add_text) * (column - 1)))
            text_len, text = text_to_photo(product[0], product[1], product[2])
            delta = (text_len - baze) // 2
            final_photo.paste(text,
                              (dif2 * line + baze * (line - 1) - ceil(delta),
                               dif * column + (baze + add_text) * (column - 1) + baze))
            final_photo.save("res_menu.jpg")
        else:
            # final_photo =
            final_photo.paste(prod_im,
                              (dif * line + baze * (line - 1), dif * column + (baze + add_text) * (column - 1)))
            text_len, text = text_to_photo(product[0], product[1], product[2])
            delta = (text_len - baze) // 2
            final_photo.paste(text,
                              (dif * line + baze * (line - 1) - ceil(delta),
                               dif * column + (baze + add_text) * (column - 1) + baze))
            final_photo.save("res_menu.jpg")
        if line == inline_n:
            line = 0
            column += 1
        line += 1


# async def main():
#     result = await get_menu_for_photo()
#     create_menu(result)
#
#
# asyncio.run(main())
