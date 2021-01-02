import os
import sys

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

dir_name = sys.argv[1]
os.makedirs(dir_name, exist_ok=True)
tabs_list = []
stack_back = []

BLOOMBERG = 'bloomberg'
NYTIMES = 'nytimes'
BLOOMBERG_SITE = 'bloomberg.com'
NYTIMES_SITE = 'nytimes.com'
EXIT = 'exit'
TB_TABS = 'tb_tabs/'
BACK = 'back'

while True:
    url = input()
    if url != BLOOMBERG_SITE and url != NYTIMES_SITE:
        if url == EXIT:
            break
        if url in tabs_list:
            if url == BLOOMBERG:
                print(bloomberg_com)
            elif url == NYTIMES:
                print(nytimes_com)
        else:
            if url == BACK and len(stack_back) > 0:
                stack_back.pop()
                if stack_back[-1] == BLOOMBERG:
                    print(bloomberg_com)
                elif stack_back[-1] == NYTIMES:
                    print(nytimes_com)
            else:
                print('Error: Incorrect URL')
    else:
        if url == BLOOMBERG_SITE and url not in tabs_list:
            print(bloomberg_com)
            f = open(TB_TABS + BLOOMBERG, 'w')
            f.write(bloomberg_com)
            f.close()
            tabs_list.append(BLOOMBERG)
            stack_back.append(BLOOMBERG)
        elif url == NYTIMES_SITE and url not in tabs_list:
            print(nytimes_com)
            f = open(TB_TABS + NYTIMES, 'w')
            f.write(nytimes_com)
            f.close()
            tabs_list.append(NYTIMES)
            stack_back.append(NYTIMES)

