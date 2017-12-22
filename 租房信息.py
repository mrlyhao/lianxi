from bs4 import BeautifulSoup
import requests
url = 'http://xa.xiaozhu.com/fangzi/8407647264.html'
web_date = requests.get(url)
soup = BeautifulSoup(web_date.text,'lxml')


title = soup.select('div.pho_info > h4')[0].text
dizhi = soup.select('.pr5')[0].text
fangzu =soup.select('div.day_l > span')[0].text
img = soup.select('#curBigImage')[0].get('src')
names = soup.select('div.w_240 > h6 > a')[0].text
xingbie = soup.select('div.member_pic > div')[0].get('class')[0]
print(title)
print(dizhi)
print(fangzu)
print(img)
print(names)
print(xingbie)

def xingbies(xingbie):
    if xingbie == 'member_ico1':
        return '女'
    if xingbie =="member_ico":
        return '男'
data = {
    "title":title,
    "dizhi":dizhi,
    'fangzu':fangzu,
    "immg":img,
    'name':names,
    'xingbie':xingbies(xingbie),
}
print(data)

page_link = [] # <- 每个详情页的链接都存在这里，解析详情的时候就遍历这个列表然后访问就好啦~

def get_page_link(page_number):
    for each_number in range(1,page_number): # 每页24个链接,这里输入的是页码
        full_url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(each_number)
        wb_data = requests.get(full_url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        for link in soup.select('a.resule_img_a'): # 找到这个 class 样为resule_img_a 的 a 标签即可
            page_link.append(link)

# ---------------------