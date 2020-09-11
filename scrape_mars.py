
# Import modules
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import time


def init_browser():
    executable_path = {
        "executable_path": "C:/Users/todds/Desktop/Library/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# Set path for chrome driver
executable_path = {
    "executable_path": "C:/Users/todds/Desktop/Library/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

# NOTE:  RESET THIS FUNCTION AND CORRECTLY TAB ALL CODE BELOW
# def scrape_images():
# Ultimate calls sub-functions:
# scrape_news()
# scrape_pic()
# scrape_facts()
# scrape_hemis()


# Set global dictionary to store values for all scrapes
Mars = {}


# Function to scrape Mars news
# ------------------------------------------------------------------------------------------------
def scrape_news():
    # Define storage variables

    # Set URL and retrieve page
    url = "http://mars.nasa.gov/news/"
    response = requests.get(url)
    browser.visit(url)

    # Create Beautiful Soup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Scrape content
    news_title = soup.body.find("div", class_="content_title").a.text.strip()
    news_para = soup.body.find(
        "div", class_="rollover_description_inner").text.strip()

    # Store news summaries
    Mars["news"] = {"headline": news_title, "summary": news_para}

    return print(Mars["news"])


# Function to scrape Mars featured image
# ------------------------------------------------------------------------------------------------
def scrape_pic():
    # Define storage variables

    # Set URL and retrieve page
    url1 = "https://www.jpl.nasa.gov/spaceimages/"
    browser.visit(url1)

    # Navigate to large image using image
    browser.links.find_by_partial_text("FULL IMAGE").click()
    browser.links.find_by_partial_text("more info").click()
    browser.find_by_tag("figure.lede").first.click()

    # Scrape image
    image_url = browser.url

    # Store image
    Mars["images"] = {"featured image": image_url}

    return print(Mars["images"])


# Function to scrape Mars hemisphere images
# ------------------------------------------------------------------------------------------------
def scrape_hemis():
    #  Set URL, visit page, inspect HTML code
    url3 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    response = requests.get(url3)
    browser.visit(url3)

    # Define storage variables
    #hemi_title = []
    #hemi_url = []
    hemisphere_image_url = []

    # Create Soup object, grab each hemisphere division
    soup = BeautifulSoup(response.text, "html.parser")
    images = soup.find_all("div", class_="item")

   # Loop through stored images and append to list
    for image in images:

        # Extract title and append to hemi_title
        title = image.h3.text
        # hemi_title.append(title)

        # Extract href from image and append to base URL to get to image file
        base_url = "https://astrogeology.usgs.gov"
        full_url = base_url+image.a["href"]

        # Create soup object and extract full image URL; append to hemi_url
        response1 = requests.get(full_url)
        soup = BeautifulSoup(response1.text, "html.parser")
        image_url = soup.find("div", class_="downloads").a["href"]
        # hemi_url.append(image_url)

        # Create Hemisphere Image list
        hemisphere_image_url.append({"title": title, "image_url": image_url})

        # print(hemisphere_image_url)
    # Store values
    Mars["hemis"] = hemisphere_image_url

    # Change this to just return Mars["hemis"] when combined with srape_images
    return print(Mars["hemis"])


# Calls scrape_hemis functions, which for now prints Mars["hemis']; See scrape_images() function
scrape_news()
scrape_pic()
scrape_hemis()
