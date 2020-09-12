
# Import modules
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import time

# NOTE:  Check where this is function is used


def init_browser():
    executable_path = {
        "executable_path": "C:/Users/todds/Desktop/Library/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# Set path for chrome driver
executable_path = {
    "executable_path": "C:/Users/todds/Desktop/Library/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# Set global dictionary to store values for all scrapes
Mars = {}


# Global scrape function to calll each separate scrape function
# --------------------------------------------------------------
def scrape_all():
    # Calls each scrape function individually to compile complete set of data
    scrape_news()
    scrape_pic()
    scrape_facts()
    scrape_hemis()

    # returns dicationary "Mars" with all scraped data
    return Mars


# Function to scrape Mars news (using Beautiful Soup)
# ---------------------------------------------------------------
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

    return Mars["news"]


# Function to scrape Mars featured image (using Splinter)
# ---------------------------------------------------------------
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

    return Mars["images"]

# Function to scrape Mars facts (using Pandas)
# ----------------------------------------------------------------


def scrape_facts():
    # Set URL and retrieve page
    url2 = "http://space-facts.com/mars/"

    # Read to Pandas; store table
    Mars["facts"] = pd.read_html(url2)[0]

    # For now, this is stored as an array; see what it looks like when rendered
    return Mars["facts"]


# Function to scrape Mars hemisphere images (using Beautiful Soup)
# ----------------------------------------------------------------
def scrape_hemis():
    #  Set URL, visit page, inspect HTML code
    url3 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    response = requests.get(url3)
    browser.visit(url3)

    # Define storage variable
    hemisphere_image_url = []

    # Create Soup object, grab each hemisphere division
    soup = BeautifulSoup(response.text, "html.parser")
    images = soup.find_all("div", class_="item")

   # Loop through stored images and append to list
    for image in images:

        # Extract title and append to hemi_title
        title = image.h3.text

        # Extract href from image and append to base URL to get to image file
        base_url = "https://astrogeology.usgs.gov"
        full_url = base_url+image.a["href"]

        # Create soup object and extract full image URL; append to hemi_url
        response1 = requests.get(full_url)
        soup = BeautifulSoup(response1.text, "html.parser")
        image_url = soup.find("div", class_="downloads").a["href"]

        # Create Hemisphere Image list
        hemisphere_image_url.append({"title": title, "image_url": image_url})

    # Store values
    Mars["hemis"] = hemisphere_image_url

    # Change this to just return Mars["hemis"] when combined with srape_images
    return Mars["hemis"]


scrape_all()
