UCSD Data Science Bootcamp Spring 2019
Cris Bangaoil

Homework 12 Web Scraping
Mission to Mars

In this assignment, we were to build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

This repo contains the following files:

Mission_to_mars.ipynb is a Jupyter Notebook file that contains the web scraping from various sites.

Scrape_mars is python script. It contains a function titled “scrape” that mirrors the Jupyter Notebook functionality and stores the data in Mongo DB collection.

App.py is a python script to import the scrape_mars.py script and call the ‘scrape’ function. It will also query the Mongo DB and pass the mars data into an HTML template to display the data

In the templates folder, is an Index.html document that takes the mars data dictionary and display all of the data with proper HTML elements.

Chromedriver.exe is a resource needed to run the Jupyter Notebook and scrape_mars python script.
 
