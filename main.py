import requests
from bs4 import BeautifulSoup
from os.path  import basename
import random
import string

count = int(input("Please input how many screenshots you want\n"))
print("Searching...\nPlease wait. To STOP the process press Ctrl C")

headers = {
	"User-Agent": 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36 OPR/66.0.3515.27'
}

index = 0

while (index < count):
	number = random.randrange(5,7,1)
	url = ''.join(random.choices(string.ascii_lowercase + string.digits, k=number))
	page = requests.get("https://prnt.sc/"+url, headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	img = soup.find(id="screenshot-image")
	if (img):
		src = img['src'].split("//")[1]
		if (src.split("/")[0] == 'i.imgur.com'):
			print(src)
			print("prnt.sc/"+url)
			with open(basename(src), 'wb') as f:
				f.write(requests.get('http://'+src).content)
			index += 1
	