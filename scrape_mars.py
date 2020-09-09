
# Import modules
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import time


def init_browser():
    executable_path = {
        "executable_path": "C:/Users/todds/Desktop/Library/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

# Function to pull Mars hemisphere images
# ------------------------------------------------------------------------------------------------


# NOTE:  RESET THIS FUNCTION AND CORRECTLY TAB ALL CODE BELOW
# def scrape_images():

executable_path = {
    "executable_path": "C:/Users/todds/Desktop/Library/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

# Define storage variables
hemi_title = []
hemi_url = []
hemisphere_image_url = []

# Set URL, visit page, inspect HTML code
url3 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
response = requests.get(url3)
browser.visit(url3)

# Create Soup object, grab each hemisphere division
soup = BeautifulSoup(response.text, "html.parser")
images = soup.find_all("div", class_="item")

# Loop through stored images and append to list
for image in images:

    # Extract title and append to hemi_title
    title = image.h3.text
    hemi_title.append(title)

    # Extract href from image and append to base URL to get to image file
    base_url = "https://astrogeology.usgs.gov"
    full_url = base_url+image.a["href"]

    # Create soup object and extract full image URL; append to hemi_url
    response1 = requests.get(full_url)
    soup = BeautifulSoup(response1.text, "html.parser")
    image_url = soup.find("div", class_="downloads").a["href"]
    hemi_url.append(image_url)

    # Create Hemisphere Image list
    hemisphere_image_url.append({"title": title, "image_url": image_url})

print(hemisphere_image_url)
