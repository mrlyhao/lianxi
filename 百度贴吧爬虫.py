import re
import requests
from bs4 import BeautifulSoup
import time

def getHTMLtext(URL):
    try:
        r = requests.get(URL,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def getTitle(HTML):
    try:
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*)</h3>')
        title = re.search(pattern,HTML)
        return title.group(1).strip()
    except:
        return ''

def getPageNum(HTML):
    try:
        pattern = re.compile('<span class="red">(.*?)</span>')
        result = re.search(pattern,HTML)
        return result.group(1).strip()
    except:
        return ''

def getContent(HtML,Pagelist,Page):
    try:
        pattern = re.compile('<div id="post_content.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,HtML)
        floor = 1
        for item in items:
            removeImg = re.compile('<img.*?>| {7}|')#去除img标签,7位长空格
            removeAddr = re.compile('<a.*?>|</a>')    #删除超链接标签
            replaceLine = re.compile('<tr>|<div>|</div>|</p>')    #把换行的标签换为\n
            replaceTD= re.compile('<td>')    #将表格制表<td>替换为\t
            replacePara = re.compile('<p.*?>')    #把段落开头换为\n加空两格
            replaceBR = re.compile('<br><br>|<br>')    #将换行符或双换行符替换为\n
            removeExtraTag = re.compile('<.*?>')    #将其余标签剔除
            item = re.sub(removeImg,"",item)
            item = re.sub(removeAddr,"",item)
            item = re.sub(replaceLine,"\n",item)
            item = re.sub(replaceTD,"\t",item)
            item = re.sub(replacePara,"\n    ",item)
            item = re.sub(replaceBR,"\n",item)
            item = re.sub(removeExtraTag,"",item)
            Pagelist.append(item)
            Pagelist.extend(['\n',str(Page),'页',str(floor),u'楼-----------------------------------------------------------------------------------------------','\n'])
#            print(Page,'页',floor,u'楼-----------------------------------------------------------------------------------------------','\n')
            floor = floor+1
        return Pagelist
    except:
        return ''

def Printlist(Pagelist,Title):
    try:
        f = open(Title+'.txt','a')
        f.writelines(Pagelist)
        f.close()
    except:
        print('cuowu')
        return ''
def main():
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    url = 'http://tieba.baidu.com/p/3138733512'
    startpage = getHTMLtext(url)
    a= getPageNum(startpage)
    pagelist = []
    Page = 1
    title = getTitle(startpage)
    print(title)
    for i in range(1,int(a)+1):
        url = url +'?pn='+str(i)
        html = getHTMLtext(url)
        getContent(html,pagelist,Page)
        Page = Page + 1
    Printlist(pagelist,title)
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

main()
