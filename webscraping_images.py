# webscraping_images.py

import time
import sys
import pickle

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException

url = r"https://www.hentai-foundry.com/"
start = 0  # page number
stop = 0  #  stop after this many pictures

site_username, site_password, email, email_password = sys.argv[1:]

driver = webdriver.Firefox()
'''
driver.get(url)

driver.find_element_by_id("frontPage").click()
driver.find_element_by_name("LoginForm[username]").send_keys(site_username)
driver.find_element_by_name("LoginForm[password]").send_keys(site_password)

input_fields = driver.find_elements_by_css_selector("input")
input_fields = filter(lambda a: a.get_attribute("type") == "submit" and a.get_attribute("value") == "Login", input_fields)
tuple(input_fields)[0].click()

driver.find_element_by_link_text(site_username).click()

more = driver.find_elements_by_link_text("MORE")
def find_more(elem):
	attr = elem.get_attribute("href")
	return attr == rf"https://www.hentai-foundry.com/user/{site_username}/faves/pictures"

more = filter(find_more, more)
tuple(more)[0].click()

def get_images(driver):
	global count
	
	num_links = len(driver.find_elements_by_class_name("thumbLink"))
	
	for n in range(num_links):
		try:
			i = driver.find_elements_by_class_name("thumbLink")[n]
		except IndexError:
			time.sleep(.5)
			i = driver.find_elements_by_class_name("thumbLink")[n]
			print(i)
		
		i.click()
		image = driver.find_element_by_class_name("center")
		pic = requests.get(image.get_attribute("src")).content

		try:
			with open(f"webscraped_image_{count}.png", "wb+") as file:
				file.write(pic)
		except Exception as e:
			print(e)
			print(f"could not save: page {count // 25} number {count % 25}")
	
		count += 1
		time.sleep(.25)
		driver.back()

time.sleep(.3)
goto = driver.find_element_by_link_text(f"{start + 1}")	
goto.click()

count = start * 25
#get_images(driver)
next = driver.find_element_by_class_name("next")
while next and count - start * 25 < stop:
	print(count - start * 25, ", ", stop)
	try:
		next.click()
		get_images(driver)
		next = driver.find_element_by_class_name("next")
	except:
		print(f"stutter: page {count // 25} number {count % 25}")
'''

driver.get(r"https://photos.google.com/")

with open(r"C:\Users\Max\Documents\Python\Image_Webscraping\cookies.txt", "rb") as file:
	cookies = pickle.load(file)
for i in cookies:
	driver.add_cookie(i)

driver.find_element_by_id("js-hero-btn").click()

'''
driver.find_element_by_id("identifierId").send_keys(email + Keys.RETURN)
time.sleep(1)
google_password = driver.find_elements_by_tag_name("input")
google_password = list(filter(lambda a: a.get_attribute("jsname") == "YPqjbf" and a.get_attribute("class") == "whsOnd zHQkBf", google_password))
google_password[0].send_keys(email_password + Keys.RETURN)
'''

main_window_handle = driver.current_window_handle

upload = driver.find_elements_by_tag_name("span")
upload = list(filter(lambda a: a.get_attribute("class") == "RveJvd snByac", upload))
upload[0].click()

signin_window_handle = None
while not signin_window_handle:
    for handle in driver.window_handles:
        if handle != main_window_handle:
            signin_window_handle = handle
            break

driver.switch_to.window(signin_window_handle)
element = driver.find_element_by_id("fileUpload")
element.send_keys("C:\myfile.txt")

#driver.close()
print("Complete")
