from selenium import webdriver
import time


def login():
    browser = webdriver.Chrome('C:\\Users\\BlackHazrd\\Desktop\\Script\\XtimeScript\\chromedriver.exe')
    browser.get('https://login.xtime.com/')
    time.sleep(5)
    browser.switch_to.frame('login')
    browser.find_element_by_id('login').send_keys('ebeard')
    browser.find_element_by_id('password').send_keys('Aa268618402')
    browser.find_element_by_class_name('basic-button').click()
    time.sleep(5)
    browser.find_element_by_class_name('launch-button').click()
    time.sleep(10)
    browser.find_element_by_xpath('//*[@id="xt_common_header_button-1042"]').click()
    time.sleep(10)
    element = browser.find_element_by_id('button-1239-btnIconEl')
    browser.execute_script("arguments[0].click();", element)
    web_element = browser.find_element_by_xpath('//*[@id="treeview-1206-record-ext-record-156"]/td/div/span')
    browser.execute_script("arguments[0].click();", web_element)
    time.sleep(5)
    browser.find_element_by_xpath('//*[@id="button-1233-btnIconEl"]').click()
    time.sleep(10)
    browser.find_element_by_xpath('//*[@id="button-1257-btnIconEl"]').click()
    time.sleep(5)
    browser.find_element_by_xpath('//*[@id="ext-gen1683"]').click()
    # hit calender
    id = 'ext-gen1683'
    browser.find_element_by_id(id).click()
    browser.implicitly_wait(5)
    browser.find_element_by_link_text('30').click()
    time.sleep(10)
    browser.find_element_by_id('inner-card-X10RDT76WY').click()
    time.sleep(10)
    name = browser.find_element_by_class_name('//*[@id="light_card-1295-headerEl"]/div/div[2]/div[2]')
    custname = name.text
    vehicle = browser.find_element_by_class_name('x-lightcard-vehicle-inf')
    car = vehicle.text
    apptime = browser.find_element_by_class_name('x-lightcard-hour x-lightcard-header-promised-time x-lightcard-small-value-label x-lightcard-header-time')
    apptime = apptime.text
    number = browser.find_element_by_class_name('x-lightcard-contact')
    phone = number.text
    service = browser.find_element_by_class_name('x-lightcard-list-value-comment-wrapper')
    servicef = service.text

    print('Name: ' + custname)
    print('car: ' + car)
    print('App Time: ' + apptime)
    print('Phone: ' + phone)
    print('Service: ' + servicef)


    # browser.find_element_by_xpath('//*[@id="button-1295-btnIconEl"]').click()

    # Hit calender date icon
    # browser.find_element_by_xpath('//*[@id="ext-gen1679"]/a').click()
    # time.sleep(5)

login()
