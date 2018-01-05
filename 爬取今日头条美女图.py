import requests,json,urllib.parse,os,time
def get_url(keyword):
    url_keyword = urllib.parse.quote(keyword)
    url = 'http://www.toutiao.com/search_content/?offset={page}&format=json&keyword={word}&autoload=true&count=20&cur_tab=1'
    urls = (url.format(word=url_keyword, page=i) for i in range(0,101,20))
    return urls
def get_link(i):
    html = requests.get(i)
    web_data = html.text
    data = json.loads(web_data)
    for i in data['data']:
        a = i['image_detail']
        for b in a:
            print(b['url'])
            time.sleep(0.5)

if __name__ == '__main__':
    a = '美女'
    links = get_url(a)
    for i in links:
        get_link(i)

