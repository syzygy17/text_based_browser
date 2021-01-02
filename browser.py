import os
import sys
import requests


dir_name = sys.argv[1]
os.makedirs(dir_name, exist_ok=True)
tabs_list = []
stack_back = []

EXIT = 'exit'
TB_TABS = 'tb_tabs/'
BACK = 'back'
HTTPS = 'https://'

while True:
    url = input()
    if url == EXIT:
        break
    elif '.' not in url:
        print('Error: Incorrect URL')
    else:
        r = requests.get(HTTPS + url)
        if url in tabs_list:
            print(r.text)
        elif url == BACK and len(stack_back) > 0:
            stack_back.pop()
            print(stack_back[-1])
        elif url not in tabs_list:
            print(r.text)
            f = open(TB_TABS + url, 'w', encoding='UTF-8')
            f.write(r.text)
            f.close()
            tabs_list.append(url)
            stack_back.append(r.text)


