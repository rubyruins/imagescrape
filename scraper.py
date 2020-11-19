import time
import urllib
import os
import math
import selenium
from selenium import webdriver
from PIL import Image
import requests
import threading
import shutil
import random

def scraper(searchterm, foldername):  
	driver = webdriver.Chrome("../chromedriver_win32/chromedriver.exe")
	driver.get("https://www.google.co.in/search?q=" + searchterm.replace(' ', '%20') + "&source=lnms&tbm=isch")
	for _ in range(500):
		driver.execute_script("window.scrollBy(0,10000)")
		if _%100 == 0:
			try:
				if driver.find_element_by_xpath("//input[@value='Show more results']"):
					driver.find_element_by_xpath("//input[@value='Show more results']").click()
					time.sleep(2)
			except:
				pass
	time.sleep(3)

	driver.execute_script("console.log(urls=Array.from(document.querySelectorAll('.rg_i')))")
	urls = driver.execute_script("return[urls.map(el=> el.hasAttribute('data-src')?el.getAttribute('data-src'):el.getAttribute('data-iurl'))]")
	driver.close()

	if not os.path.exists(foldername):
		os.mkdir(foldername)

	i = 1
	for url in urls[0]:
		if url and i <= maximum:
			img = Image.open(requests.get(str(url), stream = True).raw)
			try:
				img.save(f"{foldername}/{foldername}_{str(i)}.jpg")
				i+=1
			except:
				pass
	
	if i - 1 >= minimum:
		print(f"Found {i - 1} images for class {foldername}...")
	else:
		print(f"Found only {i - 1} images for class {foldername}, discarding class...")
		shutil.rmtree(foldername)

n_classes = int(input("Enter number of classes: "))
maximum = int(input("Enter maximum number of images for each class: "))
minimum = int(input("Enter minimum number of images for each class: "))
split = float(input("Enter train-test split: "))

threads = []

for _ in range(n_classes):
	f = input("Enter class name: ")
	s = input("Enter Google Search term: ")
	thread = threading.Thread(target = scraper, args = (s, f))
	threads.append(thread)
	
os.mkdir("data")
os.chdir("data")
	
for thread in threads:
	thread.start()
	
for thread in threads:
	thread.join()
	
os.chdir("..")

found_classes = [c for c in os.listdir("data")]
os.mkdir("data/train")
os.mkdir("data/test")

for c in found_classes:
	os.mkdir(f"data/train/{c}")
	os.mkdir(f"data/test/{c}")
	all_images = [image for image in os.listdir(f"data/{c}")]
	random.shuffle(all_images)
	split_at = math.floor(len(all_images) * split)
	training_images = all_images[:split_at]
	testing_images = all_images[split_at:]
	for image in training_images:
		shutil.move(f"data/{c}/{image}", f"data/train/{c}")
	for image in testing_images:
		shutil.move(f"data/{c}/{image}", f"data/test/{c}")
	shutil.rmtree((f"data/{c}"))