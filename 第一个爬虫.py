from bs4 import BeautifulSoup
import requests
'''
url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html#ATTRACTION_SORT_WRAPPER'
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text,'lxml')
titles = soup.select('div.listing_title > a[target="_blank"]')
imgs = soup.select('img[width="180"]')
cates = soup.select('div.p13n_reasoning_v2')
for title,img,cate in zip(titles,imgs,cates):
    data = {
        'title':title.get_text(),
        'img':img.get('src'),
        'cate':list(cate.stripped_strings),
    }
    print(data)
'''
headers = {
    'Uesr-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
    'Cookie':'ServerPool=B; TASSK=enc%3AACz%2Bs2ctwjcujn7W24EpjYjTU9jEfc6CqSfigPX2iWIr6Fov9iwAHZ3Q2n3yd7efQ6ePMWSSM%2Bj6Gc4Kb9UqTSlxg0txCpyToys4Iz4NRwVnLKYJMWlVJnFithiM8PWv2w%3D%3D; TAUnique=%1%enc%3AwAZ3pKpTktjhhjidKnabzjonD4UQ3yi47HHw916Orm%2FmhWnEwXwJZw%3D%3D; _jzqckmp=1; __gads=ID=d83ce4c913fec176:T=1509434210:S=ALNI_MbLiD0RE5SV-9t7ql10ZxBNvtzvaQ; _smt_uid=59f82383.3b0432d5; BEPIN=%1%15f71505d59%3Bbak11c.daodao.com%3A10023%3B; SecureLogin2=3.4%3AAOQjBraAvGXLCWI7qEsw8BRa8TY0ZSBDxvn%2FdnsUjvY%2FqVezopJ1erhyjQ2Li4v2iE8o24BGYv8yv3NKxSTIwa6VsHFyHw%2FHFmUDXWAS6WRIPzVDLf%2B4e8rBwkjRVWNnluD4DIJNh6TvP6HYsfu77DFKFWLNokIAhn%2BCTMCLdmTGM0f8CnOnm73MhsXwGBaCo5%2FS%2BkkjBpAKX7YiPVPFZO0%3D; TAAuth3=3%3A70cad4c15ef0732bf8a96f45df754594%3AAHQfQCX%2FBxlgMyDC1kBYImTAR48s2h7b68z%2B%2FK%2FWCjBnpaDfNCg5ueMXKfxH5ZeUeox%2Bm8jkGEaH%2BdO6mT97XSltlhzmXwhyGDynu%2FUNnOAaKf1vaphGvFrnf%2BeIwj8NkTD69xJP0zxA2OZZw58Y8%2BI7d0eVyGODsEMIGzonkVA458hR8wS9%2BXHHSQ5u68iPzA%3D%3D; _jzqx=1.1509438084.1509438084.1.jzqsr=tripadvisor%2Ecn|jzqct=/hotels-g60763-new_york_city_new_york-hotels%2Ehtml.-; CommercePopunder=SuppressAll*1509438322539; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C2%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttraction_Review-g60763-d105125-Reviews-The_Metropolitan_Museum_of_Art-New_York_City_New_York.html; roybatty=TNI1625!AIQN4H9psWsvIgA3EgMWqCijJmi3WYUQEU0mrC2H7LAcH%2Bx9H0hykm%2FxDVJo2nLBtX8xYxP4VUVagXXa8Ca67vHWOlakjO%2Ft8FegybtlIpDV1Q9bsct9H13eMkUGE%2FVl9e4CHXx9O6%2F9MViLAb%2BaTOiCfvNXiBKJ3X2Py%2BJB0CQn%2C1; _ga=GA1.2.1928483625.1509434243; _gid=GA1.2.1953777625.1509434243; _gat_UA-79743238-4=1; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1509434244; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1509438541; ki_t=1509434404076%3B1509434404076%3B1509438540829%3B1%3B28; ki_r=; _qzja=1.1129078336.1509434244034.1509434244034.1509438084011.1509438533710.1509438540834..0.0.29.2; _qzjb=1.1509438084011.26.0.0.0; _qzjc=1; _qzjto=29.2.0; _jzqa=1.3672050219355505700.1509434244.1509434244.1509438084.2; _jzqc=1; _jzqb=1.26.10.1509438084.1; TASession=%1%V2ID.D36722E1493ADFD450B13979F11BBF04*SQ.133*LP.%2F*PR.427%7C*LS.DemandLoadAjax*GR.92*TCPAR.21*TBR.50*EXEX.98*ABTR.4*PHTB.91*FS.94*CPU.72*HS.featured*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.211A9DE7992E3486B4E74243B0905B49*LF.zhCN*FA.1*DF.0*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.105125; TATravelInfo=V2*AY.2017*AM.11*AD.12*DY.2017*DM.11*DD.13*A.2*MG.-1*HP.2*FL.3*RVL.587661_304l105127_304l1687489_304l60763_304l105125_304*DSM.1509438506433*RS.1; TAUD=LA-1509434208802-1*RDD-1-2017_10_31*HC-4185876*HDD-4194616-2017_11_12.2017_11_13*LD-4297615-2017.11.12.2017.11.13*LG-4297617-2.1.F.'
}

url_saves = 'https://www.tripadvisor.cn/Saves/906561'
web_data = requests.get(url_saves,headers=headers)
soup = BeautifulSoup(web_data.text,'lxml')
print(soup)
titles = soup.select('div.location_summary > a')
imgs = soup.select('div.media-leftmedia-left')
cates = soup.select('span.text')
print(titles)


'''
for title,img,cate in zip(titles,imgs,cates):
    data = {
        'title':title.get_text(),
        'img':img.get('src'),
        'cate':list(cate.stripped.strings),
    }
    print(data)
    '''