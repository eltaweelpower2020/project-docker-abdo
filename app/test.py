from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


facebook_email="Abdelrahmanmahersoliman@gmail.com"
facebook_password="MarketerMaher&@2022"


option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
driver.get("http://www.facebook.com")
driver.maximize_window()

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
username.clear()
username.send_keys(facebook_email)
password.clear()
password.send_keys(facebook_password)
time.sleep(1)

button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(1)
driver.get("https://business.facebook.com/latest/ad_center/all_ads?asset_id=103805231874047&nav_ref=pages_classic_isolated_section_inbox_redirect")
time.sleep(1)
view_result_button=driver.find_elements(by=By.XPATH, value='.//div[@class="rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t d2edcug0 hpfvmrgz rj1gh0hx buofh1pr g5gj957u ph5uu5jm b3onmgus e5nlhep0 ecm0bbzt"]')[0].click()
time.sleep(5)
click=driver.find_elements(by=By.XPATH,value='.//div[@class="gdqlzcdm tf08tbka kfu1jryd tpry4lk2 cu1gti5y a53abz89 lgsfgr3h mcogi7i5 ih1xi9zn kiex77na"]')
print(click[1].text,"texxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxt")
time.sleep(5)
boost_button=driver.find_element(by=By.XPATH,value='//*/div/div[2]/div/div[1]/div/div/div/div/span/div/div').click()
time.sleep(8)


driver.switch_to.frame(driver.find_elements(by=By.TAG_NAME,value='iframe')[0])
time.sleep(2)
images_urls=driver.find_element_by_xpath(".//img[@class='_8b2z img']").get_attribute("src")
print(images_urls,"imageeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeees")
time.sleep(20)


















