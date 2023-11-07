import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.kabum.com.br")
browser.maximize_window()
sleep(5)

search_button = browser.find_element(By.XPATH, '//*[@class="id_search_input"]')
search_button.click()
search_button.send_keys("Mouse Gamer")
search_button.submit()
sleep(5)

names = []
prices = []

while True:
	mouses = browser.find_elements(By.XPATH, '//*[@class="sc-cdc9b13f-7 gHEmMz productCard"]')
	for mouse in mouses:
		name = mouse.find_element(By.XPATH, './/*[@class="sc-iuAqRD dkehBR"]').text
		try:
			price = mouse.find_element(By.XPATH, './/*[@class="sc-620f2d27-2 bMHwXA priceCard"]').text
		except Exception as error:
			price = 'Indisponivel'
		names.append(name)
		prices.append(price)

	next_button = browser.find_element(By.XPATH, '//*[@class="nextLink"]')
	try:
		next_button.click()
		sleep(2)
	except Exception:
		break

df = pd.DataFrame()
df['Name'] = names
df['Price'] = prices

df.to_excel('Pasta.xlsx', index=False)

browser.quit()
