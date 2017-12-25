# coding = utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import time

#使用selenium
driver = webdriver.PhantomJS(executable_path=r'D:\360安全浏览器下载\phantomjs-2.1.1-windows\bin\phantomjs.exe')
#登录QQ空间
def get_shuoshuo(qq):
    driver.get('http://user.qzone.qq.com/{}/311'.format(qq))#打开好友说说页面
    time.sleep(5)
    try:
        driver.find_element_by_id('login_div')#查看是否需要登录，若需要添加账号密码
        a = True
    except:
        a = False
    if a==True:
        driver.switch_to.frame('login_frame')#定位登录框架
        driver.find_element_by_id("switcher_plogin").click()#点击使用账户密码登录
        driver.find_element_by_id('u').clear()#选择用户名框并清空
        driver.find_element_by_id('u').send_keys('807552114')#添加账户
        driver.find_element_by_id('p').clear()#选择密码框并清空
        driver.find_element_by_id('p').send_keys('########')#添加密码
        driver.find_element_by_id('login_button').click()#点击登录
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')#判断是否有访问权限
        b = True
    except:
        b = False
    if b == True:
        driver.switch_to.frame('app_canvas_frame')#定位到说说框架
        content = driver.find_elements_by_css_selector('.content')#获取全部内容组
        stime = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')#获取全部时间组
        for con,sti in zip(content,stime):
            data = {
                'time':sti.text,
                'shuos':con.text
            }
            print(data)
    driver.close()
    driver.quit()

if __name__ == '__main__':
    get_shuoshuo('823541481')
