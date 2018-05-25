import requests
import pandas as pd
import numpy as np
import matplotlib
import bs4
from bs4 import BeautifulSoup
import csv
import re


url = "./1 APR to 15 APR.html" 

def html_tables_to_csv(input_url):
    soup = BeautifulSoup(open(url).read(), 'html.parser')
    tables = soup.find_all('table')
    table = table[3]
    headers = [(header.text).decode() for header in table.find_all('th')]
    rows = []
    for row in table_.find_all('tr'):
        rows.append([val.text for val in row.find_all('td')])

    rows = [[(x.replace('"', '')).replace('=','').replace(',','').replace(' ','') for x in i] for i in rows]


    with open('output_file8.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(row for row in rows if row)


def main(url, output_file):
    html_tables_to_csv(url, output_file)

if __name__ == "__main__":
	main(sys.argv[1])