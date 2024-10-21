import requests
from bs4 import BeautifulSoup
import csv

#Access the webpage using the Requests module
url = "https://microdata.worldbank.org/index.php/catalog/4180/data-dictionary/F7?file_name=mn.sav"
result = requests.get(url)
print(result.status_code) #To confirm the page is available
page_content = result.content

#Use BeautifulSoup module to parse the page's html content
soup = BeautifulSoup(page_content, "html.parser")
#Isolate the specific container where the variables are kept
variables = soup.find('div', class_='container-fluid variables-container')

#File creation to import scraped data into
with open('headers_creation.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    headers = ['Abbreviations', 'Definitions']
    writer.writerow(headers)
    csvfile.close()

#The MICs dictionary content is wrapped in link tags <a> </a>
#The pattern is: Odd links contain the abbreviation; Even links contain the definition

link_text = []
abbreviations = []
definitions = []

#Extract all links in the soup and isolate the text from each one
for link in variables.find_all('a'):
    text_only = link.text
    text_only = text_only.strip() #Initially returned with excess whitespace
    link_text.append(text_only)

#Sort the list of text into abbreviations and definitions based on pattern
for i in range(0, len(link_text)):
    if i%2 == 0:
        abbreviations.append(link_text[i])
    else:
        definitions.append(link_text[i])

#Append these to the file and headers created earler
with open('headers_creation.csv', 'a', newline='', encoding='utf-8') as csvfile: 
    writer = csv.writer(csvfile) 
    for Abb, Defn in zip(abbreviations, definitions): 
        writer.writerow([Abb, Defn])
    csvfile.close()
