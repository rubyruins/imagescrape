
Imagescrape 🖼
============

[![](https://img.shields.io/badge/Made_with-Python3-blue?style=for-the-badge&logo=python)]()
[![](https://img.shields.io/badge/Made_with-Pillow-blue?style=for-the-badge&logo=pillow)]()
[![](https://img.shields.io/badge/Made_with-requests-blue?style=for-the-badge&logo=requests)]()
[![](https://img.shields.io/badge/Made_with-selenium-blue?style=for-the-badge&logo=selenium)]()


Build image datasets from the command line.

---

## Features:

- Allows the user to build multiclass image datasets by taking a `class name` and a `Google search term` that scrapes images on Google for that class.
- Allows the user to select the minimum and maximum number of scraped images to be considered for a class. If more images are scraped than the maximum limit, the extra images are removed. If lesser images are scraped than the minimum limit, the class is discarded. Otherwise, whatever images are found will be split into train and test.
- To obtain a fixed number of images for each class (i.e. 100 each, 200 each), just ensure that the `minimum` and `maximum` limits have the same value (as the number of images desired.)
- Allows the user to enter a split ratio (i.e. 0.75 for 75% train, 25% test or 0.8 for 80% train, 20% test) according to which all scraped, valid images are split and arranged into folders.

**The scraped images are downloaded and arranged in a structure similar to [this.](https://machinelearningmastery.com/how-to-load-large-datasets-from-directories-for-deep-learning-with-keras/)** They can be suitably paired with Tensorflow's ImageDataGenerator to load datasets from the directory on the fly.

Depending on the size of classes specified, the script takes a couple minutes to run, download and arrange images. When the process is finished, you can find the results in the `data` folder with `train` and `test` folders in it, each containing subfolders for each class with images in it.

**Note:** currently, it can extract around 300 to 400 images for a class, or even go above 500 for common classes like fruits, animals etc.

---

## Running it locally:

**You must have Python 3.6 or higher to run the file.**

- Create a new virtual environment for running the application. You can follow the instructions [here.](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)
- Navigate to the virtual environment and activate it.
- Install the dependancies using `pip install -r requirements.txt`
- Replace the folder for `chromedriver_win32` with a relevant version which matches your browser.
- Run the `scraper.py` file with `python scraper.py`

---

## Future scope:

- Expanding the functionality to other image search engines like Yahoo, Bing for a larger dataset.
- Add an option for a validation set to be built using a validation split.