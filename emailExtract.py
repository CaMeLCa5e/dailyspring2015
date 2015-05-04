import re

with open('scrape_email_output.txt', 'a') as f:
		# while count > 10:
		# start = 1
	for n in range(100):
			# for n in range(start):
		email_addresses = re.findall('\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}', page)

				# import pdb; pdb.set_trace()
		email_addresses = set(email_addresses)  # take out duplicate addresses
		
		', '.join(email_addresses)
			
		for email_address in email_addresses:
			f.write(email_address + ', ')

				# time.sleep(randrange(2, 7))

	        	# driver.find_element_by_link_text("next").click()
	        	# try: 
	   	        	# driver.find_element_by_link_text("repeat the search with the omitted results included").click()
	   	    	# else:
	   	        	# driver.find_element_by_xpath("//table[@id='nav']/tbody/tr/td[7]/a/span").click()
 				# count = 0
	      		# count += 1

			# driver.close()
if __name__ == '__main__':
	main()
