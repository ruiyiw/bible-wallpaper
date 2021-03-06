# bible-wallpaper
_Generate wallpapers given chapter and verse number of the Bible_


## Preparation
1. Clone this repository
```bash
git clone https://github.com/ruiyiw/bible-wallpaper.git
```

2. Create python virtual environment and activate the environment
```bash
python3 -m venv env
source env/bin/activate
```

3. Install relevant packages via pip
```bash
pip install -r requirements.txt
```

## Usage
```bash
usage: cards.py [-h] [--volume_cn VOLUME_CN] [--volume_en VOLUME_EN] [-c CHAPTER]
                [-v VERSE] [--range1 RANGE1] [--range2 RANGE2]

Generate CN/EN wallpapers given the chapter and verse number of the Bible.

optional arguments:
  -h, --help            show this help message and exit
  --volume_cn VOLUME_CN
                        Volume name in Chinese
  --volume_en VOLUME_EN
                        Volume name in English
  -c CHAPTER, --chapter CHAPTER
                        Chapter number
  -v VERSE, --verse VERSE
                        Verse number
  --range1 RANGE1       Range of verse numbers: [range1, range2]
  --range2 RANGE2       Range of verse numbers: [range1, range2]
```
**Example**
```bash
# generate verse no.7 of chapter 1 in Romans both in Chinese and English
python3 cards.py --volume_cn 罗马书 --volume_en Romans -c 1 -v 7
# generate verses through no.1 to no. 5 of chapter 2 in Hebrews both in Chinese and English
python3 cards.py --volume_cn 希伯来书 --volume_en Hebrews -c 2 --range1 1 --range2 5 
```

**Note**
You need to make sure that both the Chinese and English volume names are correct and the chapters/verse numbers are not out of range.

## Sample
![111531640988411_ pic_hd](https://user-images.githubusercontent.com/76935534/147840597-143608ce-e4e3-4080-9208-59472a182ff6.jpg)
