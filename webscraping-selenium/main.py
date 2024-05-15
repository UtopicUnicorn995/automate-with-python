from selenium import webdriver
# from selenium.webdriver.common.by import By

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    # disable dash infobars -> appears when memory is low/ interfere with the script accessing, taing actions on the browser
    options.add_argument('disable-infobars')
    # So that the browser will start maximized. eg. Some browsers may change content when you resize when you make them smaller. So we want to access the maximized version of the browser
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    # This option is to avaid some issues that occur when you interact with a browser on a linux computer
    options.add_argument('no-sandbox')
    # Some browsers for security have something called sandbox. If we want our program, our scripts to have a greater privileges on that particular web page that the script is going to access and scrape, we want to add this option so that the sandboxing is disabled
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')
    # These expiremental scripts are scripts that helps us access pages that some browsers does not want to be access
    driver = webdriver.Chrome(options=options)
    driver.get('http://automated.pythonanywhere.com')
    return driver

def main():
    driver = get_driver()
    #element = driver.find_element(By.XPATH, value="/html/body/div[1]/div/h1[1]")
    element = driver.find_element(by='xpath', value="/html/body/div[1]/div/h1[1]")
    return element.text

print(main())