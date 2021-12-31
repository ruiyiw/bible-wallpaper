import sys
import requests

API_KEY = '372a5eb0c7b7884ccd148b4d65b98ca1fcc71939'
API_URL = 'https://api.esv.org/v3/passage/text/'

def get_esv_text(passage)->str:
    params = {
        'q': passage,
        'include-headings': True,
        'include-footnotes': False,
        'include-verse-numbers': True,
        'include-short-copyright': False,
        'include-passage-references': False
    }
    
    headers = {
        'Authorization': 'Token %s' % API_KEY, 
    }

    response = requests.get(API_URL, params=params, headers=headers)

    j = response.json()
    passages = response.json()['passages']

    return passages[0].strip() if passages else 'Error: Passage not found'


def get_verse(volume, chapter, number)->str:
    command = str(volume)+' '+str(chapter)+':'+str(number)
    # raw = get_esv_text(command).split(" ")
    raw = get_esv_text(command).split(" ")

    for i in range(len(raw)):
        if len(raw[i]) > 0 and list(raw[i])[0] == "[":
            index = i
            break
    

    verse = raw[index+1:len(raw)]
    return " ".join(verse)
