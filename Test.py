from selenium import webdriver
import time
import datetime

driver = webdriver.Chrome()
def start():
    url = "https://podcastle.ai/editor/login?source=landing"
    driver.get(url)
    #driver.maximize_window()

def Login(email,password):
    email_field = driver.find_element_by_css_selector("input[name='username']").send_keys(email)
    password_field = driver.find_element_by_css_selector("input[name='password']").send_keys(password)
    sign_in_button = driver.find_element_by_css_selector(".pc-auth--green-btn").click()

def negative_test():
    start()
    Login("vahram.mnatsakanyan@gmail.com","Vahram1f2345")
    time.sleep(2)
    error_message = driver.find_element_by_css_selector("div:nth-of-type(2) > .pc-material-input--error-message").text
    if error_message == "Email or password is incorrect.":
        with open("Test_result.log", 'a') as f:
            f.write("Negative test case passed! Users can't login wih invalid password.-- %s \n" % (datetime.datetime.now()))
    else:
        with open("Test_result.log", 'a') as f:
            f.write("Negative test case failed!-- %s \n" % (datetime.datetime.now()))

    time.sleep(2)


def positive_test():
    start()
    Login("vahram.mnatsakanyan@gmail.com", "Vahram12345")
    time.sleep(2)
    get_url = driver.current_url
    if get_url == "https://podcastle.ai/editor/projects":
        with open("Test_result.log", 'a') as f:
            f.write("Positive test case passed! Users can login wih valid password. -- %s \n" % (datetime.datetime.now()))
    else:
        with open("Test_result.log", 'a') as f:
            f.write("Positive test case failed! -- %s \n" % (datetime.datetime.now()))
    time.sleep(2)

def close_window():
    driver.quit()

negative_test()
positive_test()
close_window()

