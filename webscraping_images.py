# webscraping_images.py

import requests
from selenium import webdriver
import time

url = "https://www.hentai-foundry.com/"

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
	num_links = len(driver.find_elements_by_class_name("thumbLink"))
	output = []
	
	for n in range(num_links):
		i = driver.find_elements_by_class_name("thumbLink")[n]
		i.click()
		image = driver.find_element_by_class_name("center")
		output.append(image.get_attribute("src"))
		time.sleep(.3)
		driver.back()

	return output
	

image_srcs = get_images(driver)
print(image_srcs)

for num, src in enumerate(image_srcs):
	image = requests.get(src).content
	with open(f"webscraped_image_{num}.png", "wb+") as file:
		file.write(image)

#driver.close()
