from selenium import webdriver 

driver= webdriver.Chrome()
driver.get("https://globo.com")
assert "globoesporte" in driver.title

manchetes= driver.find_element_by_class_name("ola")
for manchete in manchetes:
    print(manchete.text)
    
driver.implicitly_wait(5)

driver.close()