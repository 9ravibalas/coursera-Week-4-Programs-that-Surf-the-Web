import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=input("Enter URL:")
Count= (int)(input("enter  count:  "))
position=(int)(input("enter  position:  "))
for i in range(Count):
	l=[]
	u=[]
	with urllib.request.urlopen(url) as response:
		html = response.read()
		soup = BeautifulSoup(html, "html.parser")
		tags = soup('a')
		for tag in tags:
			u.append(tag.get('href', None))
			l.append(tag.contents[0])
		print(u[position-1])
		print(l[position-1])
		url=u[position-1]	


	
		


			
		