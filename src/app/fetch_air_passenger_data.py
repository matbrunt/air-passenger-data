import requests
import json
import re
import os
from bs4 import BeautifulSoup
from time import sleep
from zipfile import ZipFile
from urllib.parse import urljoin, quote

# caa_domain = 'http://www.caa.co.uk'
# search_page_path = '/Data-and-analysis/UK-aviation-market/Airports/Datasets/UK-Airport-data/Airport-data-1990-onwards/'
# search_page_url = urljoin(caa_domain, search_page_path)

# search_req = requests.get(search_page_url)

# if search_req.status_code == 200:
#     soup = BeautifulSoup(search_req.text, 'html5lib')
#     for link in soup.select('ul.documentsList > li > a'):
#         try:
#             file_link = urljoin(caa_domain, quote(link.get('href')))
#             filename = link.get('href').rsplit('/', 1)[1]

#             print('Fetching ', file_link)
#             r_link = requests.get(file_link, stream=True)
#             with open(os.path.join('.', 'air-passenger-data', 'archive', filename), 'wb') as fd:
#                 for chunk in r_link.iter_content(chunk_size=128):
#                     fd.write(chunk)

#             sleep(2)
#         except:
#             print('Problem fetching data from', link)

for dirpath, dirnames, filenames in os.walk(os.path.join('.', 'air-passenger-data', 'archive')):
    for zip_file in [x for x in filenames if x.endswith('.zip')]:
        with ZipFile(os.path.join(dirpath, zip_file), 'r') as zip_ref:
            extract_dirname = zip_file.lower().replace(' ', '-').rstrip('.zip')
            zip_ref.extractall(os.path.join('.', 'air-passenger-data', 'extracted', extract_dirname))