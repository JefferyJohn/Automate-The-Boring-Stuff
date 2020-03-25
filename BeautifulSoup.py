import bs4, requests

# Finds most recent discount code for the Automate the Boring Stuff  Udemy Course
res = requests.get('https://automatetheboringstuff.com/')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = soup.select('body > div.main > p:nth-child(12) > a:nth-child(2)')
discount = elems[0].text.strip()

print(discount)


