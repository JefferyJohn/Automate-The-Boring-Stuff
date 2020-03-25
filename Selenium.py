# Simple assignment
from selenium.webdriver import Firefox
browser = Firefox()
'''
# Or use the context manager
from selenium.webdriver import Firefox

with Firefox() as driver:
# your code inside this indent
'''

browser.get('https://automatetheboringstuff.com')
elem = browser.find_element_by_css_selector('.main > ul:nth-child(16) > li:nth-child(1) > a:nth-child(1)')
elem.click()
elems = browser.find_elements_by_css_selector('p')
print(str(len(elems)))

browser.quit()