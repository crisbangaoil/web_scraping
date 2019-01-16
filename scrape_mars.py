# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import pandas as pd

# Convert Jupyter to Scrape function
def scrape():

    mars_data = {}

    # most recent news article title and paragraph
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'

    # Retrieve page with the requests module
    response = requests.get(url)

    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')

    #find news title
    news_article = soup.find('div', class_='content_title') 
    news_title = news_article.a.text.strip()

    #find news paragraph
    news_p = soup.find('div', class_='rollover_description_inner').text.strip()

    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p

    # featured image
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Find image url
    footer = soup.find('footer')
    img = footer.find('a')
    link = img['data-fancybox-href']
    featured_image_url = 'https://www.jpl.nasa.gov' + link
    
    mars_data['featured_image_url'] = featured_image_url
    
    browser.quit()

    # weather from twitter

    # URL of page to be scraped
    url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')

    weather = soup.find('div',class_='js-tweet-text-container').text

    mars_data['weather'] = weather

    # scrape facts
    url = 'https://space-facts.com/mars/'
    table = pd.read_html(url)

    # convert to data frame
    facts_df=table[0]
    facts_df.columns=['Description','Value']
    facts_df.set_index('Description', inplace=True)

    #convert to html string
    facts=facts_df.to_html()

    mars_data['facts'] = facts

    # Return results
    return mars_data
