import gui

print("Hello".format())
import re
import requests
from bs4 import BeautifulSoup
import sys
import subprocess
#movie = input('Enter movie name\n')
f=open("details.txt", "r")
movie=f.read()
f.close()
url = "https://thepiratebay.party/search/"+movie+"/1/99/0"
reqs= requests.get(url)
soup = BeautifulSoup(reqs.content, 'html.parser')
content = soup.find_all('a')
content = str(content)
#print(content[100])
re_links = r'\bmagnet(.*?)announce"'

link_list = re.findall(re_links,content)
movie= "magnet" + link_list[0]
movie = f'"{movie}"'
# print(movie)

# cmd = []
# cmd.append('webtorrent')
# cmd.append(movie)

# cmd.append('--vlc')
if sys.platform.startswith('linux'):
    #cmd = []
    #cmd.append('webtorrent')
    #cmd.append(movie)
    #cmd.append('--vlc')
    cmd = f'webtorrent {movie} --vlc'
    subprocess.call(cmd, shell=True)
    print(cmd)
if sys.platform.startswith('win32'):
    cmd = f'webtorrent {movie} --vlc'
    subprocess.call(cmd, shell=True)
