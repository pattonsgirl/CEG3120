from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Set up Selenium WebDriver (e.g., for Chrome)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
url = "https://engineering-computer-science.wright.edu/computer-science-and-engineering/courses"
driver.get(url)
# You can add explicit waits here if needed, for specific elements to appear
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dynamic_content")))
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# Now you can parse the soup object which contains the dynamic content
# ...
driver.quit()
print(soup)
with open('jackpot.soup', 'w') as f:
    print(soup, file=f)