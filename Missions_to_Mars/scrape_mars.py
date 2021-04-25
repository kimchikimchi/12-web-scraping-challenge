'''
Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
'''

# Import libraries
import time

from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
from urllib.parse import urljoin
from pprint import pprint


def get_html_soup(browser, url):
    # # Set up Splinter
    # executable_path = {'executable_path': ChromeDriverManager().install()}
    # browser = Browser('chrome', **executable_path, headless=False)
    
    browser.visit(url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # # Close the browser
    # browser.quit()

    return soup

def scrape():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
    '''
    Initially tried using requests lib to get HTML context, but found some
    div tags seen in Dev Tool couldn't be located.  Hence, switched to splinter instead.
    ''' 
    soup = get_html_soup(browser, 'https://mars.nasa.gov/news')

    # Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
    news_title = soup.find('li', class_='slide').find('div', class_='content_title').find('a').text
    news_p = soup.find('li', class_='slide').find('div', class_='article_teaser_body').text

    # Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    soup = get_html_soup(browser, url)

    featured_image_url = soup.find('img', class_='headerimage')['src']

    # Use a lib to recontruct the full URL.  Could have done manually but why work harder?
    # See https://docs.python.org/3/library/urllib.parse.html
    featured_image_url = urljoin(url, featured_image_url)

    '''
    Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
    ...
    Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
    '''
    hemisphere_image_urls = [
        {'title': 'Cerberus Hemisphere', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif'},
        {'title': 'Schiaparelli Hemisphere', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif'},
        {'title': 'Syrtis Major Hemisphere', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif'},
        {'title': 'Valles Marineris Hemisphere', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif'}
    ]

    # Close the browser
    browser.quit()
    data = {
        'news_title': news_title,
        'news_p': news_p,
        'featured_image_url': featured_image_url,
        'hemisphere_image_urls': hemisphere_image_urls
    }

    return(data)


# For Unit Testing
if __name__ == "__main__":
    pprint(scrape())