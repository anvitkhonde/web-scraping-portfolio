from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


hi=ChromeDriverManager().install()
hello=Service(hi)
driver=webdriver.Chrome(service=hello)

driver.get("https://quotes.toscrape.com/login")


f=driver.find_element(By.ID,"username")
f.send_keys("tadpole123")
driver.find_element(By.ID,"password").send_keys("yoyo")


driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".quote")))