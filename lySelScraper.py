from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from pyvirtualdisplay import Display
import time 
import random 

def ready(browser, d): 
	page_source = (browser.page_source).encode('utf-8')
	yes = "class=\"available selected\""
	no = "class=\"not_available\"" 
	check1 = yes in page_source
	check2 = no in page_source
	while(check1 == False and check2 == False):
		time.sleep(1)
		page_source = (browser.page_source).encode('utf-8')
		check1 = yes in page_source
		check2 = no in page_source
		print "%s yes: check1 = %s no: check2 = %s"(d, check1, check2)
	availability = True if check1 else False 
	return page_source, availability

def domain_names(): 
	LENGTH = 20 

	d_list = []
	with open('domain.txt', 'r') as df:
		for d in df: 
			d_list.append((d[0:2]).lower())

	d_exclude_list = []

	d_list = ['ly']

	wf = open('words.txt', 'r')
	w_list = wf.read().split()
	wf.close()

	domain_out = []
	with open('domain_out.txt', 'w') as outf:
		for d in d_list:
			if d not in d_exclude_list:
				pass 
				for w in w_list: 
					if w[-2] == d and len(w) >= 5 and len(w) <= LENGTH:
						w_short = w[:-2]
						if w_short in w_list:
							d_str = w[:-2]+'.'+d
							outf.write(d_str + '\n')
							domain_out.append(d_str)
if __name__ == '__main__'
	domain = domain_names()

	print domain 

	available_domain = []

	display = Display(visible=0, size=(1024, 768))
	display.start()
	browser = webdriver.Firefox()

	for d in domain:
		print "getting browser"
		browser.get('http://www.101domain.com/')
		time.sleep(random.randint(1,5))
		elem = None 
		while(not elm):
			time.sleep(1)
			try: 
				elem = browser.find_element_by_name('root')
			except: 
				print "No such element: root"
		elem.send_keys(d + Keys.RETURN)
		page_source, available = ready(browser, d)
		if available: 
			available_domain.append(d)
		print "%s : %s" %(d, available)

	browser.close()

	with open('available_domain.txt', 'w') as f:
		for d in available_domain:
			f.write(d+'\n')
























