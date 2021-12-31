from PIL import ImageFont
import os
import argparse

parser = argparse.ArgumentParser(description="Generate CN/EN wallpapers given the chapter and verse number of the Bible.")
parser.add_argument("--volume_cn", type=str, default="罗马书", help="Volume name in Chinese")
parser.add_argument("--volume_en", type=str, default="Romans", help="Volume name in English")
parser.add_argument("-c", "--chapter", type=int, default=1, help="Chapter number")
parser.add_argument("-v", "--verse", type=int, default=7, help="Verse number")

arg = parser.parse_args()
bible_cn = "data/bible_chinese.db"
bible_en = "data/bible_esv.db"
pic = "data/bkgd_low.jpeg"
# volume_cn = "罗马书"
# volume_en = "Romans"
volume_cn = arg.volume_cn
volume_en = arg.volume_en
chapter = arg.chapter
number = arg.verse
x = 750
y = 1500
font_en = ImageFont.truetype(os.path.join(os.getcwd(), "data/Georgia.ttf"), 140)
font_cn = ImageFont.truetype(os.path.join(os.getcwd(), "data/NotoSerifSC-Regular.otf"), 140)
max_width = 2000

color = 'rgb(255,255,255)'
