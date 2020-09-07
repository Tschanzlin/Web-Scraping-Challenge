# Web-Scraping-Challenge

9/7:  USGS Astreology Site images
- Tried using Splinter to navigate image pages and pull URL from final page; however, I could not get the Splinter function "browser.url" to load the proper URL so I reverted to BeautifulSoup 
- I created a Soup object "images" to capture the division class "item" for all four mars hemispheres; each "image" contains the title to the image file and a partial href
- Loop through each "image" object to extract the title and append the hemi_title list; appended partial href to the base href, and created another Soup object with the full href; extracted image_url appended to hemi_url list

9/6:  Mars News, JPL Images, and Mars Facts
- Initial scraping for parts 1A-1C successful, using combination of BeautifulSoup and Splinter