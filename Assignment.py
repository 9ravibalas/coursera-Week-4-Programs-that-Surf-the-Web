# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

sum=0
with urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_276067.html") as response:
	html = response.read()
	soup = BeautifulSoup(html, "html.parser")
	tags = soup('span')
	for tag in tags:
		print(int(tag.contents[0]))
		sum=sum+int(tag.contents[0])
	print("sum: ",sum)