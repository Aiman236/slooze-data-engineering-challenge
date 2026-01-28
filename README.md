# Slooze Data Engineering Take-Home Challenge

## Overview
This project demonstrates an end-to-end data engineering workflow including data collection and exploratory data analysis.

## Data Collection
- Source: Public website (quotes.toscrape.com)  
- Method: Web scraping using Python (requests + BeautifulSoup)  
- Output format: CSV

## Exploratory Data Analysis (EDA)
- Summary statistics  
- Author frequency analysis  
- Visualization of top authors

## Files
- scraper.py : Scrapes data and stores it in CSV format  
- eda.py : Performs exploratory data analysis  
- quotes_data.csv : Output dataset

## How to Run
- Open the project in a Jupyter Notebook
- *Part A – Scraper:* Copy all the code from scraper.py into *one notebook cell* and run it to generate quotes_data.csv  
- *Part B – EDA:* Copy all the code from eda.py into *another notebook cell* and run it after the scraper cell to analyze the data and visualize results

Note: A public demo website (quotes.toscrape.com) was used for this assignment to demonstrate scraping logic in a safe and reproducible manner, as commercial B2B platforms like IndiaMART and Alibaba restrict automated scraping.
