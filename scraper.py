start = 1
		
		for n in range(start):
			
			driver.get(url)
			driver.implicitly_wait(15) 

			page = driver.page_source.encode('utf-8')

			tree = html.fromstring(page)

			# email_addresses = re.findall('email', page)
			# email_addresses = re.findall('^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$', page)
			
			email_addresses = re.findall('\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}', page)
