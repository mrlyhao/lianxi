import re
from bs4 import BeautifulSoup
import requests

def getHTMLtext(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return'cuowu'

def duanziyemian(ilt,html):
    try:
        soup = BeautifulSoup(html,'html.parser')
        names = soup.select('div[class="author clearfix"] h2')
        neirongs = soup.select('div[class="content"] span')
        for i in range(len(names)):
            ilt.append([names[i].get_text().strip(),neirongs[i].get_text().strip()])
        return ilt
    except:
        return'cuowu'

def main():
    infoList = []
    for i in range(1,11):
        try:
            start_url = 'http://www.qiushibaike.com/hot/page/'+str(i)
            html = getHTMLtext(start_url)
            duanziyemian(infoList,html)
        except:
            return'cuowu'
    print(infoList)
main()