import pprint
import pyperclip

message = str(pyperclip.paste())
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print('Your clipboard has the following data:\n')
pprint.pprint(count)
