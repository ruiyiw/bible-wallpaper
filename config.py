from PIL import ImageFont
import os
import argparse

parser = argparse.ArgumentParser(description="Generate CN/EN wallpapers given the chapter and verse number of the Bible.")
parser.add_argument("--volume_cn", type=str, default="罗马书", help="Volume name in Chinese")
parser.add_argument("--volume_en", type=str, default="Romans", help="Volume name in English")
parser.add_argument("-c", "--chapter", type=int, default=1, help="Chapter number")
parser.add_argument("-v", "--verse", type=int, default=7, help="Verse number")
parser.add_argument("--range1", type=int, default=1, help="Range of verse numbers: [range1, range2]")
parser.add_argument("--range2", type=int, default=7, help="Range of verse numbers: [range1, range2]")

arg = parser.parse_args()
bible_cn = "data/bible_chinese.db"
bible_en = "data/bible_esv.db"
# pic = "data/bkgd_low.jpeg"
pic = "data/bkgd_new.jpeg"
# volume_cn = "罗马书"
# volume_en = "Romans"
volume_cn = arg.volume_cn
volume_en = arg.volume_en
chapter = arg.chapter
number = arg.verse
range1 = arg.range1
range2 = arg.range2
# x = 750
# y = 1500
x = 350
y = 600
# font_en = ImageFont.truetype(os.path.join(os.getcwd(), "data/Georgia.ttf"), 140)
# font_cn = ImageFont.truetype(os.path.join(os.getcwd(), "data/NotoSerifSC-Regular.otf"), 140)
font_en = ImageFont.truetype(os.path.join(os.getcwd(), "data/Georgia.ttf"), 70)
font_cn = ImageFont.truetype(os.path.join(os.getcwd(), "data/NotoSerifSC-Regular.otf"), 70)
# max_width = 2000
max_width = 1000

color = 'rgb(0,0,0)'
color_head = 'rgb(64,64,64)'

# interval = 300
interval = 150
