import webbrowser, sys, pyperclip


# Check if command line arguments were passed
sys.argv

if len(sys.argv) > 1:
    # ['WebBrowser.py', 'University of Georgia'] --> 'University of Georgia Athens Georgia 30602
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)