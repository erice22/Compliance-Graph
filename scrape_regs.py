from bs4 import BeautifulSoup as soup
import numpy as np
import shutil
import os
import requests
from markdownify import markdownify
from urllib.request import Request, urlopen

def scrape(num, tag_name, class_name, base_url, url_addin = ""):
    /*
    
    */
    url = base_url + str(num) + url_addin
    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    print(url)
    page_soup = soup(webpage, "html.parser")
    tags = page_soup.find_all(tag_name , class_ = class_name)
    cwd = os.getcwd()
    realname = "Art. " + str(num) + " GDPR"
    file = open(cwd + "/{}.md".format(realname), 'w')
    md = markdownify(str(tags[0]), heading_style = "ATX")
    n = file.write(md)
    file.close()



def main():
    for i in range(6,65):
        scrape(i, "div","entry-content", "https://gdpr-info.eu/art-", "-gdpr/")

main()
