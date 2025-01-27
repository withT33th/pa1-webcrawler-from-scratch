from bs4 import BeautifulSoup
import argparse
import requests


parser = argparse.ArgumentParser(description = 'Program scrapes the KSU website')
parser.add_argument('siteURL', type = str, help = 'Enter target URL: ')
parser.add_argument('--num-pages', type = int, help = 'Number of pages to scrape before terminating')
parser.add_argument('--restrict-domain', action = 'store_false' , help = 'Restricts the scraper to the specified domain')
args = parser.parse_args()

siteText = requests.get(args.siteURL).text
soup = BeautifulSoup(siteText, 'lxml')
pageLinks = []

for link in soup.find_all('a'):
    print(link.get('href'))