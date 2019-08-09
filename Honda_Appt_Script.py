from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


def login():
    
    # open text file to write
    f = open('Honda_Appt_lists.text', 'w')
    # find chrome Driver
    browser = webdriver.Chrome('C:\\Users\\Eddie\\Desktop\\Script\\chromedriver.exe')
    # open browser to site
    browser.get('https://login.xtime.com/')
    # sleep to load full site
    # Maximize window
    browser.maximize_window()
    time.sleep(2)
    # Switch to the Iframe I need
    browser.switch_to.frame('login')
    # input login info and submit
    browser.find_element_by_id('login').send_keys('user')
    browser.find_element_by_id('password').send_keys('pass')
    browser.find_element_by_class_name('basic-button').click()
    # sleep
    time.sleep(5)
    # Launch Honda
    launch_button = 0
    while True:
        honda = browser.find_elements_by_class_name('launch-button')
        try:
            launch_button = launch_button + 1
            honda[launch_button].click()
        except IndexError:
            break
    time.sleep(10)
    # Goes to workbook
    # Applies Filters
    browser.find_element_by_xpath('//*[@id="xt_common_header_button-1042"]').click()
    time.sleep(10)
    element = browser.find_element_by_id('button-1239-btnIconEl')
    browser.execute_script("arguments[0].click();", element)
    web_element = browser.find_element_by_xpath('//*[@id="treeview-1206-record-ext-record-163"]/td/div/span')
    browser.execute_script("arguments[0].click();", web_element)
    browser.find_element_by_xpath('//*[@id="button-1233-btnIconEl"]').click()
    time.sleep(10)
    # Sort by status
    browser.find_element_by_xpath('//*[@id="button-1257-btnIconEl"]').click()
    browser.implicitly_wait(5)
    
    def calender_changer(x):
        
        while 31 > x > 15:
            # Find calender
            div = browser.find_element_by_id('ledgerdateslider-1247-innerCt')
            # hit calender
            div.find_element_by_xpath('//*[@id="component-1250"]/div/table/tbody/tr/td[1]').click()
            # hit calender date
            browser.implicitly_wait(5)
            browser.find_element_by_link_text(str(x)).click()
            time.sleep(10)
            try:
                index = 0
                while True:
                    header = browser.find_elements_by_class_name('x-ledgerdataview-header')
                    try:
                        time.sleep(2)
                        header[index].click()
                        while True:
                            name = browser.find_elements_by_class_name('x-lightcard-customer-name')
                            car = browser.find_elements_by_class_name('x-lightcard-vehicle-inf')
                            apt_time = browser.find_elements_by_class_name('x-lightcard-header-right')
                            contact = browser.find_elements_by_class_name('x-lightcard-contact')
                            note = browser.find_elements_by_class_name('x-lightcard-services')
                            try:
                                # print and write to file name/car/apt_time/contact/note
                                print(name[index].text)
                                f.write("\n" + 'Name: ' + name[index].text + "\n")
                                print(car[index].text)
                                f.write('Car: ' + car[index].text + "\n")
                                print(apt_time[index].text)
                                f.write('Time: ' + apt_time[index].text + "\n")
                                print(contact[index].text)
                                f.write('Contact: ' + contact[index].text + "\n")
                                print(note[index].text)
                                f.write('Service Notes:' + note[index].text + "\n")
                                print(x)
                                f.write('Date:' + str(x) + "\n")
                                index += 1
                                break
                            except IndexError:
                                break

                    except IndexError:
                        x = x - 1
                        break
            except NoSuchElementException:
                print(x)
    calender_changer(30)
    time.sleep(5)
    f.close()
    
    
login()
