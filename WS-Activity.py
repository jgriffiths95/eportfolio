import requests
from bs4 import BeautifulSoup
import json

#Using the get function from requests to access the webpage
#print the status code to make sure the site exists
#404 - page does not exist
#202 - page exists
result = requests.get("https://online.essex.ac.uk/courses/msc-data-science/")
print(result.status_code)

#print the HTTP headers of the webpage
#print(result.headers)

#Store the page content (html code) in a variable
page_content = result.content

#Parse and process the page content by creating a BeautifulSoup variable
soup = BeautifulSoup(page_content, "html.parser")

page_text = soup.get_text().lower()
word_count = page_text.count("data scientist")

#Presenting information of interest in a dict so it can be neatly parsed into a JSON
parsable_data = {
    'url': "https://online.essex.ac.uk/courses/msc-data-science/",
    'keyword': "data scientist",
    'number of appearances': word_count
}

#Parsing data into the JSON
with open('website_wordcounts.json', 'w') as f:
    json.dump(parsable_data, f, indent=4)