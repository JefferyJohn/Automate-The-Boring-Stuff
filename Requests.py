import requests

res = requests.get('https://drive.google.com/file/d/1b80hbutCORUKasisX-zCqVRSLpBj4Sdh/view?usp=sharing')
res.raise_for_status()
playFile = open('CurrentResume.txt', 'wb')
for chunk in res.iter_content(10000000):
    playFile.write(chunk)
playFile.close()