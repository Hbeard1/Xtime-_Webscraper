from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


# find chrome Driver
browser = webdriver.Chrome('C:\\Users\\Eddie\\Desktop\\Script\\chromedriver.exe')


def login():
    # Open text file to write
    f = open('Acura_Missed_Appt_lists.text', 'w')
    # open browser to site
    browser.get('https://login.xtime.com/')
    # sleep to load full site
    # Maximize window
    browser.maximize_window()
    time.sleep(2)
    # Switch to the Iframe I need
    browser.switch_to.frame('login')
    # input login info and submit
    browser.find_element_by_id('login').send_keys('ebeard')
    browser.find_element_by_id('password').send_keys('Aa268618402')
    browser.find_element_by_class_name('basic-button').click()
    # sleep to loaf full site
    time.sleep(5)
    # Launch Acura
    # Sleep to let web elements load
    browser.find_element_by_class_name('launch-button').click()
    time.sleep(7)
    # Goes to workbook
    # Applies Filters for Call center appoinments
    # Sleep to let web_elements and JS to load
    browser.find_element_by_xpath('//*[@id="xt_common_header_button-1042"]').click()
    time.sleep(2)
    element = browser.find_element_by_id('button-1239-btnIconEl')
    browser.execute_script("arguments[0].click();", element)
    web_element = browser.find_element_by_xpath('//*[@id="treeview-1206-record-ext-record-152"]/td/div/span')
    browser.execute_script("arguments[0].click();", web_element)

    no_show_filter = browser.find_element_by_xpath('//*[@id="treeview-1213-record-ext-record-157"]/td/div')
    browser.execute_script("arguments[0].click();", no_show_filter)
    browser.find_element_by_xpath('//*[@id="button-1233-btnIconEl"]').click()
    time.sleep(2)
    # Sort by status
    # Wait while sorting
    browser.find_element_by_xpath('//*[@id="button-1257-btnIconEl"]').click()
    browser.implicitly_wait(2)

    def calender_changer():
        current_date = time.strftime("%d")
        today_date = int(current_date) - 1

        while 31 > today_date > 0:
            # Find calender
            div = browser.find_element_by_id('ledgerdateslider-1247-innerCt')
            # hit calender
            div.find_element_by_xpath('//*[@id="component-1250"]/div/table/tbody/tr/td[1]').click()
            # hit calender date
            browser.implicitly_wait(2)
            browser.find_element_by_link_text(str(today_date)).click()
            time.sleep(2)
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
                                print(today_date)
                                f.write('Date:' + str(today_date) + "\n")
                                time.sleep(3)
                                index += 1
                                break
                            except IndexError:
                                break
                    except IndexError:
                        today_date -= 1
                        break
            except NoSuchElementException:
                print(today_date)
    calender_changer()
    time.sleep(5)
    f.close()


login()
