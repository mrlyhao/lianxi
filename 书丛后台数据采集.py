import pandas as pd
import numpy as np
import time
import requests
import re
def geturllist(page):
    try:
        headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'Cookie':'UM_distinctid=15d81a78e390-005eb4bcd-3b664008-1fa400-15d81a78e3a38f; UNION_SESSION=eyJpdiI6Inc2XC9HcGQ4S3duZjNHVUlhdjlRbGx3PT0iLCJ2YWx1ZSI6Ik9JMXVJNXRSWTlVNUN5RnVGS3Nlbm5CZEZcL2VYaGxlTm9mdlNIZXQzdU1ZZjRGNU5OeFh1Ull4XC9HekcxREEwa3NJY1RTdU96SWhkQ2wzSVNZRlYwVHc9PSIsIm1hYyI6ImFhZmM2YjMzNDZhOGMxMDc5OTFkMGIyYzQyZTU1NWMyZGVhMWIyYTQ4ZTI0YmE5NTI0NGJiNTVmOGRmOTkzNmIifQ%3D%3D; Hm_lvt_91d1a3c1a6ce73e789f1b3a0dcf37b38=1510037338,1510377451,1510535773; CNZZDATA1262221695=1403518706-1501719651-%7C1510620922; jieqiUserInfo=jieqiUserId%3D28152134%2CjieqiUserUname%3D%E4%B9%A6%E4%B8%9B%E5%B0%8F%E8%AF%B4%E8%81%94%E7%9B%9F%2CjieqiUserName%3D%E4%B9%A6%E4%B8%9B%E5%B0%8F%E8%AF%B4%E8%81%94%E7%9B%9F%2CjieqiUserGroup%3D3%2CjieqiUserGroupName%3D%E6%99%AE%E9%80%9A%E4%BC%9A%E5%91%98%2CjieqiUserVip%3D0%2CjieqiUserHonorId%3D%2CjieqiUserHonor%3D%C1%D0%B1%F8%2CjieqiUserPassword%3D124ab1c62e27b5e139c7be17cf00bca3%2CjieqiUserUname_un%3D%26%23x4E66%3B%26%23x4E1B%3B%26%23x5C0F%3B%26%23x8BF4%3B%26%23x8054%3B%26%23x76DF%3B%2CjieqiUserName_un%3D%26%23x4E66%3B%26%23x4E1B%3B%26%23x5C0F%3B%26%23x8BF4%3B%26%23x8054%3B%26%23x76DF%3B%2CjieqiUserHonor_un%3D%26%23x5217%3B%26%23x5175%3B%2CjieqiUserGroupName_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserLogin%3D1510640991; jieqiVisitInfo=jieqiUserLogin%3D1510640991%2CjieqiUserId%3D28152134; SESSION=eyJpdiI6IkJtVzNHUWlTdnVhcU5XTEV3T0ZMc2c9PSIsInZhbHVlIjoicitYZDBwZkJYaGNSNjRjdlVTZ3cwV0UyNnNzcjJTVHgrWFFnYW9kd0hRaEV5UzRKRFwvaXFRaFVOVks5SU9cLzlLT3FPVVU0eUV0Q3Q4VnlDdVBCbkphQT09IiwibWFjIjoiMDk1ZTA3NzcxNWZlOTUxOTc4Yzk4ZjU3OWFmOTJlMTA4YTNkNjJjOWIyYjk3OTVkMmIzOTRkZjkxZDM1ZDU2MiJ9; aliyungf_tc=AQAAALVHHBNMSQUAJfm+cwDvdtT/LD7k; acw_tc=AQAAALT1/E4bGwYAJfm+c7JOb4/Jj1pa; XSRF-TOKEN=eyJpdiI6IlwvM01OK1ZxVVhJTHlJM2c4XC9Yb1ZKQT09IiwidmFsdWUiOiJZaHZndHF2UThDTndDK1VhaHFoNmwzbmk4eFpLb2xOcldNaWxiaWUzRjVFZlRUenVGcFdPXC81dTlBd0Z0Wko2MkpsNFY1ZFBwZnZnR1BwVGljTTMzMHc9PSIsIm1hYyI6Ijg0NmZjNDM0Yjg5YjQwMDA4Y2ZjNjc0NDc0NzMzNDViZjdjNzM1YzhhNWIwNjhmZmJlZDMyODFjODljMDVjNTcifQ%3D%3D; ADU_SESSION=eyJpdiI6InZzamVndWpkSXhxZnU2Q1JuZ1BvQWc9PSIsInZhbHVlIjoiMmR4a2I2ZG0wUUdFcWF1VWUzZHZPS25TVmZIaVhwc1hOMVBBanFFN2lnS21aS1hkUXU3XC9OS3JlVHpXUlBlMXRDMThJY2ZteU92U29cLzZvdHFhM0pvUT09IiwibWFjIjoiN2I3ZDA4ZDMwMjIwNTczNThmYTBjYTY3ODg5OWYxZTBmZGY4NjBhMDk5ZGU0NDNmOWE4NGUwZGY1MTYxMTMxMyJ9; 8f861f4af92520e2813f021078b04215425b6814=eyJpdiI6IlFcL1Y3YzByUXp3UmgyTFJNb2xSYkVBPT0iLCJ2YWx1ZSI6ImhFRCt3QXU5U09HQmV5UllLREhEUXJVS0JaSXR3WjJIVDEzc1JVTm1PWm1LRVBSdDJUQVU4T3VEUE5ndzBsVWJCQ2dPYkc4cjVldVNLR2VvMzdxZlJ5NkRqbVZnVUZJNkhXZUkzVFE2V1Z6ZVZUSTBUWVwvWCs3c2pLU2xkMzIxSDRwMkZlUWgxZ2FJTVRcLzg3U21mSGtHU1FjQ29yXC9OdEhIVE5CelVkdlhDSEpBRE4rdzVvMDRzaFZzQm9XMEEyVmVuVWI4eVVWdDhZMTNTZ2txUzhqR1wvMmJnNGowK3ZWb0JDWmJsQmc3aTBwWG5XRnhjOWpnY0pya1FCXC9XME1FQWdqUHpTMDA3Ym9cL2VncEhkR2swbTNEZEtBdXFDbzhRN2c0b0J2Vk4rV0JZOCtzNkhZSTFOek1pOUdjZXVpZ2tndFlqaldjekh6Mkhsak1LTHBWU3ZacXFqUWR3R0JldW5iVVlOS3h0eXZQYnF0bVN1XC8yYnRYWlI4RkZlMmFKWUNPYTkrbWlWXC9YWUl5Zm94a0kwdWpjbkRBRzUyK1Fld0paMjczU3lpdTlpemV5SGpHdkNlcWt5ckx4dURBS2tSaDJncVpFUzIrc1UrQVNRMVVaeEg3Tlg4QWJSVTFqOHpSeWplWk5vb2UzVGdNWldWMmZTWFJ1MGhCMHdQeEUxeVhEa1Y0VXZ3R1wvSlpnRnpcL1dRaUd6bUd0STZpekVxelhnNU9HVGZcL2dpOEM1MUFcL2RabXZielJhTXE3aVBBN1prQm1oeG91NlEwV3FZRmw3dDJ1elRvYVNvZG00bnV5XC9QWm1xaFJGOFdlN0pRcnRHeExxb1VvZ2pIWWplZk8xczFwSmxMb1hMbWpVMGx2Yk0rc3FCdFFBdz09IiwibWFjIjoiMWMyNDRmNjkwYTI3ZTYyMTIwMWI3ZDIxYTI5NjEwNzYyZGMwZjIxOWNkMzJlYWZjNDNiOTFiNzk5OTg4ZDdmNyJ9'
        }
        web_data = requests.get(page,headers=headers)
        return web_data.text
    except:
        return ''
def Page(Html,a0,a1,a2,a3,a4,a5,a6,a7,a8,a9):
    try:
        pattern = re.compile('<tr>.*?<td.*?>(.*?)</td>.*?'
                             '<td.*?>(.*?)</td>.*?'
                             '<td.*?>(.*?)</td>.*?'
                             '<td.*?>(.*?)</td>.*?'
                             '<td.*?>(.*?)</td>.*?'
                             '<td.*?>(.*?)</td>.*?'
                             '<td.*?>(.*?)</td>.*?'
                             '<td.*?>(.*?)</td>.*?'
                             '<td.*?>(.*?)</td>.*?'
                             '<td.*?>(.*?)</td>.*?</tr>',re.S)
        items = re.findall(pattern,Html)
        for item in items:
            a0.append(item[0].strip())
            a1.append(item[1].strip())
            a2.append(item[2].strip())
            a3.append(item[3].strip())
            a4.append(item[4].strip())
            a5.append(item[5].strip())
            a6.append(item[6].strip())
            a7.append(item[7].strip())
            a8.append(item[8].strip())
            a9.append(item[9].strip())
        return a1,a2,a3,a4,a5,a6,a7,a8,a9
    except:
        return ''

def main():
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    data0 = []
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []
    data7 = []
    data8 = []
    data9 = []
    for i in range(1,51):
        url = 'http://ad.shucong.com/admin/union/user_promotions/?page='+str(i)
        html = geturllist(url)
        Page(html,data0,data1,data2,data3,data4,data5,data6,data7,data8,data9)
        print(i)
    data = {
        'ID':'',
        '书号':'',
        '标题':'',
        '站长':'',
        '书丛订单号':'',
        '充值金额':'',
        '分成比例':'',
        '分成金额':'',
        '结算方式':'',
        '充值时间':''
    }
    data['ID']=data0
    data['书号']=data1
    data['标题']=data2
    data['站长']=data3
    data['书丛订单号']=data4
    data['充值金额']=data5
    data['分成比例']=data6
    data['分成金额']=data7
    data['结算方式']=data8
    data['充值时间']=data9
    df = pd.DataFrame(data)
    df.to_csv('书丛后台数据.csv',mode='a')
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

main()