import lxml.html as lh
from selenium import webdriver

browser = webdriver.PhantomJS()
browser.set_window_size(1024, 768)
browser.get('http://commons.wikimedia.org/wiki/File%3aBrad_Pitt_Cannes_2011.jpg')
content = browser.page_source
browser.quit()

doc = lh.fromstring(content)
for etl in doc.xpath('//span[a[contains(@title, "Use this file")]]/text()'):
	print etl 



