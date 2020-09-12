# Web-Scraping-Challenge

Overall Notes:
- Program properly scrapes and stores data, but I am unable to complete the full rendering.  It also appears to srape twice, and i'd lik to spend more time cleaning and refining the programs.  They are not as tight as I woudl like. 
- Biggest remaining hurdle was trying to figure out how to iterate through the Mars.hemi list of URL's in order to property display the images; I was unable to get this to work


9/12:
- Basic Flask app loading; mars facts table not loading properly
- Considered splitting table into keys and values;  tried reading panda dataframe to html as simpler process
- Code is working but cannot complete final rendering; two issues outstanding - the table displaying mars.facts and the hemispherical images; elected to show the URL link in text so that you can see the output works

9/11:
- Working scrape_mars.py file; created separate functions to scrape data sections and then a global function which calls each separate function
- While some of the code may be redundant, I felt the code would be better organized and cleaner by not trying to do too much with one function

9/10:
- Starting scrape_mars.py file
- Reviewing MongoDB documentation to determine best way to store scraped data in order to recall for the app.py

9/7:  USGS Astreology Site images
- Tried using Splinter to navigate image pages and pull URL from final page; however, I could not get the Splinter function "browser.url" to load the proper URL so I reverted to BeautifulSoup 
- I created a Soup object "images" to capture the division class "item" for all four mars hemispheres; each "image" contains the title to the image file and a partial href
- Loop through each "image" object to extract the title and append the hemi_title list; appended partial href to the base href, and created another Soup object with the full href; extracted image_url appended to hemi_url list

9/6:  Mars News, JPL Images, and Mars Facts
- Initial scraping for parts 1A-1C successful, using combination of BeautifulSoup and Splinter