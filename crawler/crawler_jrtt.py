from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("http://www.google.com/")

#open tab
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
# You can use (Keys.CONTROL + 't') on other OSs

# Load a page
driver.get('https://blog.stackademic.com/frontend-masters-feature-sliced-design-fsd-pattern-81416088b006')
# Make the tests...

# close the tab
# (Keys.CONTROL + 'w') on other OSs.
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
bs = BeautifulSoup(driver.page_source,"html.parser")

driver.close()