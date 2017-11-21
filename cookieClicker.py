from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tkinter import *
import re
upgrade_num = 15

def save_game():
	el_options = driver.find_elements_by_id("prefsButton")
	if(len(el_options)):
		el_options[0].click()
	time.sleep(1)
	
	el_export_save = driver.find_elements_by_link_text('Export save')
	if(len(el_export_save)):
		el_export_save[0].click()
		
	time.sleep(1)
	el_text_area = driver.find_elements_by_id('textareaPrompt')
	if(len(el_text_area)):
		el_text_area[0].send_keys(Keys.CONTROL, 'c')
		data = Tk().clipboard_get()
		file = open("save.txt", "w")
		file.write(data)
		file.close()
		el_text_area[0].send_keys(Keys.RETURN)
	el_options[0].click()
	
	
def load_game():
	el_options = driver.find_elements_by_id("prefsButton")
	if(len(el_options)):
		el_options[0].click()

	time.sleep(1)
	el_export_load = driver.find_elements_by_link_text('Import save')
	if(len(el_export_load)):
		el_export_load[0].click()
	
	file = open("save.txt", "r")
	data = file.readline()
	el_text_area = driver.find_elements_by_id('textareaPrompt')
	if(len(el_text_area)):
		el_text_area[0].send_keys(data)
		el_text_area[0].send_keys(Keys.RETURN)
		time.sleep(1)
	el_options[0].click()

def some_clicks():
	el_bigCookie = driver.find_elements_by_id("bigCookie")
	if(len(el_bigCookie)):
		b=0
		while b <= 100:
			el_bigCookie[0].click()
			b=b+1
			
	
def how_many_cookies():
	how_many_cookies = driver.find_elements_by_id("cookies")
	if(len(how_many_cookies) > 0):
		num_cookies = how_many_cookies[0].text
		num = ''
		mul = 1
		num.join("asd")
		for x in num_cookies:
			if(x=='s'):
				break
			if(x.isdigit() or x=='.'):
				num=num+x
			if(x=='m'):
				mul=1000000
			elif(x=='b'):
				mul=1000000000
		return float(num)*mul
	else:
		print("can't get number of your cookies :(")

	
def buy_upgrade():
	upgrade = driver.find_elements_by_id("upgrade0")
	if(len(upgrade)):
		upgrade[0].click()
	time.sleep(1)
		
def buy_products():
	for x in range(0, 15):
		product_id = "product"+str(x)		
		xpath = '//div[@id="'+product_id +'"][@class="product unlocked enabled"]'
		print(xpath)
		product = driver.find_elements_by_xpath(xpath)
		if(len(product)):
			print(product[0].text)
			product[0].click()
			time.sleep(1)
			
	
def program():
	while 1==1:
		for i in range(0,50):
			some_clicks()
			buy_products()
			buy_upgrade()			
		save_game()
		
	

print ("program started")

driver = webdriver.Chrome()
driver.get("http://orteil.dashnet.org/cookieclicker/")
time.sleep(1)
load_game()
program()


	