


import sys
from bs4 import BeautifulSoup
import csv


def scrap_vulns(url):
	soup = BeautifulSoup(open(url), "html.parser")
	all_files = soup.findAll('div',attrs={'class':'filebox'})
	report_list = []
	report_list.append(["File","line","Vulnerability"])
	for file in all_files:
		filename = str( file.find('span',attrs={'class':'filename'}).text)
		filename = filename.strip("File: ")
		#print filename
		all_details = file.findAll('div',attrs={'name':'allcats'})
		for detail in all_details:
			vulnerability = []
			vulnerability.append(filename)
			vulnerability_name =  detail.find('div',attrs={'class':'vulnblock'})['name']
			vulnerability_location = detail.find('div',attrs={'class':'codebox'})
			vulnerability_location = vulnerability_location.find('table')
			vulnerability_location = vulnerability_location.find('tbody')
			vulnerability_location = vulnerability_location.find('tr')
			vulnerability_location = vulnerability_location.findAll('td')[1]
			vulnerability_location = vulnerability_location.find('div',attrs={'class':'code'})['id']
			vulnerability_line = vulnerability_location.strip(filename)
			vulnerability.append(vulnerability_line)
			vulnerability.append(vulnerability_name)
			report_list.append(vulnerability)
			#print vulnerability
	return report_list


def write_csv(report_list,report_file):
	myFile = open(report_file, 'w')  
	with myFile:  
		writer = csv.writer(myFile)
		writer.writerows(report_list)


if __name__ == '__main__':
	input_html_file = sys.argv[1]
	output_csv_file = sys.argv[2]
	vulns =scrap_vulns(input_html_file)
	write_csv(vulns,output_csv_file)
