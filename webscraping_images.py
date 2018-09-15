# webscraping_images.py

import requests
from selenium import webdriver
import time

url = "https://www.hentai-foundry.com/"
start = 0
stop = 1

driver = webdriver.Firefox()

driver.get(url)

driver.find_element_by_id("frontPage").click()
driver.find_element_by_name("LoginForm[username]").send_keys("RedKnite")
driver.find_element_by_name("LoginForm[password]").send_keys("Gf6HL98&pi")

input_fields = driver.find_elements_by_css_selector("input")
input_fields = filter(lambda a: a.get_attribute("type") == "submit" and a.get_attribute("value") == "Login", input_fields)
tuple(input_fields)[0].click()

driver.find_element_by_link_text("RedKnite").click()

more = driver.find_elements_by_link_text("MORE")
def find_more(elem):
	attr = elem.get_attribute("href")
	return attr == "https://www.hentai-foundry.com/user/RedKnite/faves/pictures"

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

goto = driver.find_element_by_link_text(f"{start + 1}")
goto.click()

count = start * 25
get_images(driver)
next = driver.find_element_by_class_name("next")
while next and count // 25 < stop:
	try:
		next.click()
		get_images(driver)
		next = driver.find_element_by_class_name("next")
	except:
		print(f"stutter: page {count // 25} number {count % 25}")

driver.close()
print("Complete")
