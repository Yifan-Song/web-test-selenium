from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

wait_time1 = 1
wait_time2 = 3

def equalDate(d1, d2):
    date1 = d1.split('-')
    date2a = d2.split('年')
    date2b = date2a[1].split('月')
    date21 = date2a[0]
    date22 = date2b[0]
    date23 = date2b[1].split('日')[0]
    if(int(date1[0]) == int(date21) and int(date1[1]) == int(date22) and int(date1[2]) == int(date23)):
        return 1
    return 0

class WebTest:
    browser = webdriver.Chrome()
    def __init__(self, url):
        self.browser.get(url)

    def testInput(self):
        usernameInput = self.browser.find_element_by_id('userName')
        usernameInput.send_keys("admin")
        usernameValue = usernameInput.get_attribute('value')
        try:
            assert(usernameValue == "admin")
        except AssertionError:
            print("USERNAME_ELE ERROR", usernameValue)
            return 0
            
        passwordInput = self.browser.find_element_by_id('password')
        passwordInput.send_keys("ant.design")
        passwordValue = passwordInput.get_attribute('value')
        try:
            assert(passwordValue == "ant.design")
        except AssertionError:
            print("PASSWORD_ELE ERROR", passwordValue)
            return 0
        print("INPUT TEST PASSED")
        return 1

    def testButton(self):
        loginButton = self.browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/form/div[3]/div/div/span/button')
        loginButton.click()
        time.sleep(wait_time1)
        now_url = self.browser.current_url
        try:
            assert(now_url == "http://127.0.0.1:8000/dashboard/analysis")
        except AssertionError:
            print("LOGIN_ELE ERROR", now_url)
            return 0
        print("BUTTON TEST PASSED")
        return 1

    def testSwtichtag(self):
        main_handle = self.browser.current_window_handle
        docButton = self.browser.find_element_by_xpath('//*[@id="root"]/div/section/section/header/div/div/a/i')
        docButton.click()
        time.sleep(wait_time2)
        all_handles = self.browser.window_handles
        for handle in all_handles:
            if(handle != main_handle):
                self.browser.switch_to.window(handle)
        now_url = self.browser.current_url
        try:
            assert(now_url == "https://pro.ant.design/docs/getting-started")
        except AssertionError:
            print("NEW_TAG ERROR", now_url)
            return 0
        self.browser.close()
        self.browser.switch_to.window(main_handle)
        now_url = self.browser.current_url
        try:
            assert(now_url == "http://127.0.0.1:8000/dashboard/analysis")
        except AssertionError:
            print("SWITCH_BACK_TAG ERROR", now_url)
            return 0
        print("SWITCH TAG TEST PASSED")
        return 1

    def testSidebar(self):
        mainSidebar = self.browser.find_element_by_xpath('//*[@id="root"]/div/section/aside/div/ul/li[3]')
        mainSidebar.click()
        time.sleep(wait_time1)
        subSidebar = self.browser.find_element_by_xpath('//*[@id="root"]/div/section/aside/div/ul/li[3]//*[@id="/list$Menu"]/li[1]')
        subSidebar.click()
        now_url = self.browser.current_url
        try:
            assert(now_url == "http://127.0.0.1:8000/list/table-list")
        except AssertionError:
            print("SIDEBAR ERROR", now_url)
            return 0
        print("SIDEBAR TEST PASSED")
        return 1

    def testCheckbox(self):
        checkBox = self.browser.find_element_by_xpath('//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div[2]/div/div/div/div/div/table/tbody/tr[2]/td[1]/span/label/span/input')
        checkBox.click()
        try:
            assert(checkBox.is_selected() == True)
        except AssertionError:
            print("CHOOSE CHECKBOX ERROR", checkBox.is_selected())
            return 0
        checkBox.click()
        try:
            assert(checkBox.is_selected() == False)
        except AssertionError:
            print("CLEAR CHECKBOX ERROR", checkBox.is_selected())
            return 0
        print("CHECKBOX TEST PASSED")
        return 1

    def prepareTest(self):
        #跳转页面
        mainSidebar = self.browser.find_element_by_xpath('//*[@id="root"]/div/section/aside/div/ul/li[2]')
        mainSidebar.click()
        time.sleep(wait_time1)
        subSidebar = self.browser.find_element_by_xpath('//*[@id="/form$Menu"]/li[1]')
        subSidebar.click()
        now_url = self.browser.current_url
        #检验是否跳转正确
        try:
            assert(now_url == "http://127.0.0.1:8000/form/basic-form")
        except AssertionError:
            print("SIDEBAR ERROR", now_url)
            return 0
        #输入表单内容
        titleInput = self.browser.find_element_by_id("title")
        titleInput.send_keys("title")
        goalInput = self.browser.find_element_by_id("goal")
        goalInput.send_keys("goal")
        standardInput = self.browser.find_element_by_id("standard")
        standardInput.send_keys("standard")
        #检验是否输入正确
        titleValue = titleInput.get_attribute('value')
        goalValue = goalInput.get_attribute('value')
        standardValue = standardInput.get_attribute('value')
        try:
            assert(titleValue == "title" )
            assert(goalValue == "goal")
            assert(standardValue == "standard")
        except AssertionError:
            print("INPUT ERROR", titleValue, goalValue, standardValue)
            return 0
        print("PREPARE FROM TEST PASSED")
        return 1

    def testCalendar(self):
        #选择日期
        calendar = self.browser.find_element_by_xpath('//*[@id="date"]/span/i')
        calendar.click()
        time.sleep(wait_time1)
        startdateEle = self.browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[3]/td[1]')
        startdateTempValue = startdateEle.get_attribute("title")
        startdateEle.click()
        enddateEle = self.browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[1]')
        enddateTempValue = enddateEle.get_attribute("title")
        enddateEle.click()
        #检验是否输入正确
        startdateInput = self.browser.find_element_by_xpath('//*[@id="date"]/span/input[1]')
        enddateInput = self.browser.find_element_by_xpath('//*[@id="date"]/span/input[2]')
        startdateValue = startdateInput.get_attribute('value')
        enddateValue = enddateInput.get_attribute('value')
        try:
            assert(equalDate(startdateValue, startdateTempValue))
            assert(equalDate(enddateValue, enddateTempValue))
        except AssertionError:
            print("CALENDAR ERROR", startdateValue, startdateTempValue, enddateValue, enddateTempValue)
            return 0
        print("CALENDAR TEST PASSED")
        return 1
    

    def testRadiobuttton(self):
        radioButtton = self.browser.find_element_by_xpath('//*[@id="public"]/label[3]/span[1]/input')
        try:
            assert(radioButtton.is_selected() == False)
        except AssertionError:
            print("RADIO BUTTON ERROR", radioButtton.is_selected())
            return 0
        radioButtton.click()
        try:
            assert(radioButtton.is_selected() == True)
        except AssertionError:
            print("RADIO BUTTON ERROR", radioButtton.is_selected())
            return 0
        print("RADIO BUTTON TEST PASSED")
        return 1

    def testForm(self):
        #测试基础表格
        basicForm = self.browser.find_element_by_xpath('//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form')
        basicForm.submit()
        #跳转页面
        subSidebar = self.browser.find_element_by_xpath('//*[@id="/form$Menu"]/li[2]')
        subSidebar.click()
        now_url = self.browser.current_url
        try:
            assert(now_url == "http://127.0.0.1:8000/form/step-form/info")
        except AssertionError:
            print("SIDEBAR ERROR", now_url)
            return 0
        #测试分步表格
        nextButton = self.browser.find_element_by_xpath('//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[5]/div/div/span/button')
        nextButton.click()
        time.sleep(wait_time1)
        now_url = self.browser.current_url
        try:
            assert(now_url == "http://127.0.0.1:8000/form/step-form/confirm")
        except AssertionError:
            print("FORM ERROR1", now_url)
            return 0
        #测试提示框
        self.testAlert()
        submitButton = self.browser.find_element_by_xpath('//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[7]/div/div/span/button[1]')
        submitButton.click()
        now_url = self.browser.current_url
        try:
            assert(now_url == "http://127.0.0.1:8000/form/step-form/result")
        except AssertionError:
            print("FORM ERROR2", now_url)
            return 0
        print("FORM TEST PASSED")
        return 1

    def testAlert(self):
        alert = self.browser.find_element_by_xpath('//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[1]')
        try:
            assert(alert.text == "确认转账后，资金将直接打入对方账户，无法退回。")
        except AssertionError:
            print("ALERT ERROR", alert.text)
            return 0
        alertClose = self.browser.find_element_by_xpath('//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[1]/a')
        alertClose.click()
        time.sleep(wait_time1)
        #TODO:如何检测元素已经消失
        #print(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[1]')))
        print("ALERT TEST PASSED")
        return 1
    
    def testWebPage(self):
        t1 = self.testInput()
        t2 = self.testButton()
        t3 = self.testSwtichtag()
        t4 = self.testSidebar()
        t5 = self.testCheckbox()
        t6 = self.prepareTest()
        t7 = self.testCalendar()
        t8 = self.testRadiobuttton()
        t9 = self.testForm()# 包含testAlert
        if(t1&t2&t3&t4&t5&t6&t7&t8&t9):
            print("ALL TEST PASSED")
        else:
            print("SOME ERROR OCCURED")
        self.browser.close()
    
def main():
    webtest = WebTest("http://127.0.0.1:8000/user/login")
    webtest.testWebPage()
    exit(0)

main()
