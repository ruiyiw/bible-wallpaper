from PIL import Image, ImageDraw, ImageFont
import sqlite3
import config
import esv
import argparse


class BibleCn():
    def __init__(self):
        con = sqlite3.connect(config.bible_cn)
        self.cur = con.cursor()

    def run(self, name)->list:
        return self.find_verse(name)

    def find_verse(self, name)->list:
        """
        Find all verses in a volume from the database
        """
        sn = self.cur.execute("select SN from BibleID where FullName = '%s'" % name)
        sn = int(list(sn)[0][0])
        verse = self.cur.execute("select ChapterSN, VerseSN, Lection from Bible where VolumeSN = '%s'" % sn)
        return list(verse)

    def get_verse_by_index(self, verse, chapter, number)->str:
        for line in verse:
            c, n, _ = line
            if c == chapter and n == number:
                return line
        

class BibleASV():
    def __init__(self):
        con = sqlite3.connect(config.bible_en)
        self.cur = con.cursor()
    
    def run(self, name)->list:
        return self.find_verse(name)

    def find_verse(self, name)->list:
        verse = self.cur.execute("select Chapter, Versecount, verse from bible where Book = '%d'" % name)
        return list(verse)


class BibleESV():
    def __init__(self):
        self.volume = config.volume_en

    def find_verse(self, chapter, number)->str:
        verse = esv.get_verse(self.volume, chapter, number)
        return verse


class DrawCard():
    def __init__(self, x, y, pic, font_en, font_cn, max_width, color, color_head, interval):
        self.img = Image.open(pic)
        self.draw = ImageDraw.Draw(self.img)
        self.x = x
        self.y = y
        self.font_en = font_en
        self.font_cn = font_cn
        self.max_width = max_width
        self.color = color
        self.color_head = color_head
        self.interval = interval

    def text_wrap(self, text, font, lang)->list:
        lines = []
        
        # If the text width is smaller than the image width, then no need to split
        # just add it to the line list and return
        if font.getsize(text)[0]  <= self.max_width:
            lines.append(text)
        else:
            #split the line by spaces to get words
            if lang == 'en':
                words = text.split(' ')
            if lang == 'cn':
                words = list(text)
            i = 0
            # append every word to a line while its width is shorter than the image width
            while i < len(words):
                line = ''
                while i < len(words) and font.getsize(line + words[i])[0] <= self.max_width:
                    if lang == 'en':
                        line = line + words[i]+ " "
                    if lang == 'cn':
                        line = line + words[i]
                    i += 1
                if not line:
                    line = words[i]
                    i += 1
                lines.append(line)
        return lines

    def draw_meta(self, chapter, number, font, lang):
        if lang == 'en':
            line_meta = "["+config.volume_en+" "+str(chapter)+":"+str(number)+"]"
            line_height = font.getsize('hg')[1] + 50
        if lang == 'cn':
            line_meta = "["+config.volume_cn+" "+str(chapter)+":"+str(number)+"]"
            line_height = font.getsize('国')[1] + 50

        self.draw.text((self.x,self.y), line_meta, fill=self.color_head, font=font)
        self.y = self.y + line_height

    def draw_text(self, text, font, lang):
        if lang == 'en':
            # line_height = self.font_en.getsize('hg')[1] + 50
            line_height = self.font_en.getsize('hg')[1] + 30
        if lang == 'cn':
            line_height = self.font_cn.getsize('国')[1]
        
        # If the text width is smaller than the image width, then no need to split
        # just add it to the line list and return
        if font.getsize(text)[0]  <= self.max_width:
            if lang == 'en':
                self.draw.text((self.x,self.y), text, fill=self.color, font=self.font_en)
                self.y = self.y + line_height

            if lang == 'cn':
                self.draw.text((self.x,self.y), text, fill=self.color, font=self.font_cn)
                self.y = self.y + line_height
            print(text)
        else:
            #split the line by spaces to get words
            if lang == 'en':
                words = text.split(' ')
            if lang == 'cn':
                words = list(text)
            i = 0
            # append every word to a line while its width is shorter than the image width

            while i < len(words):
                line = ''
                splitlines = False
                while i < len(words) and font.getsize(line + words[i])[0] <= self.max_width and not splitlines:
                    if lang == 'en':
                        line = line + words[i]+ " "
                        if '\n' in words[i]:
                            splitlines = True

                    if lang == 'cn':
                        line = line + words[i]
                    i += 1

                if not line:
                    line = words[i]
                    i += 1
                if lang == 'en':
                    self.draw.text((self.x,self.y), line, fill=self.color, font=self.font_en)

                if lang == 'cn':
                    self.draw.text((self.x,self.y), line, fill=self.color, font=self.font_cn)
                
                self.y = self.y + line_height
                print(line)


    def add_text(self, verse_cn)->None:
        chapter, number, text_cn = verse_cn
        bible_en = BibleESV()
        text_en = bible_en.find_verse(chapter, number)

        # lines = []
        # line_height_cn = self.font_cn.getsize('国')[1] + 50
        # #Draw meta
        # line_meta = "["+config.volume_cn+" "+str(chapter)+":"+str(number)+"]"
        # self.draw.text((self.x,self.y), line_meta, fill='rgb(192,192,192)', font=self.font_cn)
        # self.y = self.y + line_height_cn
        # #Draw content
        # lines.append(self.text_wrap(text_cn, self.font_cn,'cn'))
        # for line in lines[0]:
        #     print(line)
        #     self.draw.text((self.x,self.y), line, fill=self.color, font=self.font_cn)
        #     self.y = self.y + line_height_cn
        #     # self.img.save(f"sample/sample_{idx}.png")

        # lines = []
        # line_height_en = self.font_cn.getsize('hg')[1]
        # #Draw meta
        # self.y = self.y + line_height_cn*2
        # line_meta = "["+config.volume_en+" "+str(chapter)+":"+str(number)+"]"
        # self.draw.text((self.x,self.y), line_meta, fill='rgb(192,192,192)', font=self.font_en)
        # self.y = self.y + line_height_en
        # #Draw content
        # lines.append(self.text_wrap(text_en, self.font_en,'en'))
        # for line in lines[0]:
        #     print(line)
        #     self.draw.text((self.x,self.y), line, fill=self.color, font=self.font_en)
        #     self.y = self.y + line_height_en
        
        self.draw_meta(chapter, number, self.font_cn, 'cn')
        self.draw_text(text_cn, self.font_cn, 'cn')
        self.y = self.y + self.interval
        self.draw_meta(chapter, number, self.font_en, 'en')
        self.draw_text(text_en, self.font_en, 'en')
        
        self.img.save(f"sample/{config.volume_en}{chapter}:{number}.png")





bible_cn = BibleCn()
verse_cn = bible_cn.run(config.volume_cn)

draw_card = DrawCard(x=config.x, y=config.y, pic=config.pic, font_en=config.font_en, font_cn=config.font_cn, max_width=config.max_width, color=config.color, color_head=config.color_head, interval=config.interval)
# Generate full list
# for i in range(len(verse_cn)):
#     draw_card.add_text(verse_cn[i])

# Generate single verse
draw_card.add_text(bible_cn.get_verse_by_index(verse_cn, config.chapter, config.number))

# # Generate verses in a range
# for i in range(config.range1, config.range2+1, 1):
#     draw_card = DrawCard(x=config.x, y=config.y, pic=config.pic, font_en=config.font_en, font_cn=config.font_cn, max_width=config.max_width, color=config.color, color_head=config.color_head, interval=config.interval)
#     draw_card.add_text(bible_cn.get_verse_by_index(verse_cn, config.chapter, i))
