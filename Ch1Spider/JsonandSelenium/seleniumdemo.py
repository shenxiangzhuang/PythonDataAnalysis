import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def getdata(html):
    pass


def run():
    login_url = 'https://accounts.douban.com/login'  # 要打开的页面
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0")
    driver = webdriver.PhantomJS('/home/shensir/phantomjs-2.1.1-linux-x86_64/bin/phantomjs',
                                 desired_capabilities=dcap)
    driver.get(login_url)  # 打开网页
    time.sleep(5)  # 等待5s，使得网页加载完全

    # 获取登录页面的初始图片
    driver.get_screenshot_as_file('before-login.png')

    # html = driver.page_source  # 获取当前网页源码
    # print(html)

    # 填写帐号密码登录
    driver.find_element_by_xpath('//*[@id="email"]').send_keys('你的帐号')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('你的密码')

    time.sleep(3)
    # 获取填写信息后的页面
    driver.get_screenshot_as_file('after-insert.png')

    # 点击登录
    driver.find_element_by_xpath('//*[@id="lzform"]/div[6]/input').click()
    # 查看登陆后的界面
    time.sleep(3)
    driver.get_screenshot_as_file('after-login.png')

    '''
    进行一些登录后的操作
    html = driver.get('http://...')
    getdata(html)
    '''

    # 若程序异常中断,driver不会自动释放
    # 所以实际使用时最好就上异常处理，保证driver的释放
    driver.quit()


if __name__ == '__main__':
    run()
