import gui 
print("Hello".format())
import re
import requests
from bs4 import BeautifulSoup
import sys
import subprocess
#movie = input('Enter movie name\n')
f=open("assets/details.txt", "r")
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
cmd = []
cmd.append('webtorrent')
cmd.append(movie)
cmd.append('--vlc')
subprocess.call(cmd)
