from bs4 import BeautifulSoup



def scrap_vulns(url):
	soup = BeautifulSoup(open(url), "html.parser")
	all_details = soup.findAll('div',attrs={'name':'allcats'})
	report_list = []
	for detail in all_details:
		vulnerability = []
		vulnerability_name =  detail.find('div',attrs={'class':'vulnblock'})['name']
		vulnerability.append(vulnerability_name)
		print vulnerability_name
		vulnerability_location = detail.find('div',attrs={'class':'codebox'})
		vulnerability_location = vulnerability_location.find('table')
		vulnerability_location = vulnerability_location.find('tbody')
		vulnerability_location = vulnerability_location.find('tr')
		vulnerability_location = vulnerability_location.findAll('td')[1]
		vulnerability_location = vulnerability_location.find('div',attrs={'class':'code'})['id']
		print vulnerability_location
		vulnerability.append(vulnerability_location)
		report_list.append(vulnerability)
		#print vulnerability
	return report_list


scrap_vulns("RIPS_dvwa.html")
