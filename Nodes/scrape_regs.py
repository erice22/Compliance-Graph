from bs4 import BeautifulSoup as soup
import numpy as np
import shutil
import os
import requests
from markdownify import markdownify
from urllib.request import Request, urlopen

def scrape(tag_name, class_name, base_url, url_addin = ""):
    url = base_url
    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    print(url)
    page_soup = soup(webpage, "html.parser")
    tags = page_soup.find_all(tag_name , class_ = class_name)
    cwd = os.getcwd()
    for i in range(len(tags)):
        realname = "SFD" + str(i)
        file = open(cwd + "/{}.md".format(realname), 'w')
        md = markdownify(str(tags[i]), heading_style = "ATX")
        n = file.write("[[BSIMM]] #intelligence #feature_design")
        n = file.write(md)
        file.close()



def main():
    #scrape("div","component-text", "https://www.bsimm.com/framework/intelligence/security-design.html")
    
main()
