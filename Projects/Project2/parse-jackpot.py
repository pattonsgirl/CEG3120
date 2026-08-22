import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime

# to use with filename
current_date = datetime.now().strftime('%d%m%Y')
outputname = f"{current_date}_CSE_PreReqs.txt"


with open("jackpot.soup", "r") as file:
    dump = file.read()

soup = BeautifulSoup(dump, 'html.parser')

course_links = soup.find_all('a', class_='acalog-course-link')
#course_list = []
catalog_url_list = []

for link in course_links:
    href = link.get('href')
    # getting title from internal page
    #course_list.append(link.get_text())
    #print(link.get_text())
    catalog_url_list.append(href)
    #print(href)

#CS 1180 as demo
#url = "https://catalog.wright.edu/preview_course_nopop.php?catoid=24&coid=154343"

for c in catalog_url_list:
    course_id = ''
    pre_reqs = ''
    #print(c)
    # make nice queries
    time.sleep(2)
    response = requests.get(c)
    # check if URL will load
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"Failed to retrieve content from {c}. Status code: {response.status_code}")
    # snag course title
    course_title = soup.find('h1', id='course_preview_title')
    if course_title:
        text_content = course_title.get_text(strip=True)
        print(text_content)
        course_id = text_content
    else:
        print("H1 tag with the ID course_preview_title not found.")
    # Find the strong tag with the specific text
    prerequisite_tag = soup.find('strong', string='Prerequisite(s):')
    if prerequisite_tag:
        # Get the next sibling, which should be the text after the strong tag
        next_element = prerequisite_tag.next_sibling
        # Check if it's a NavigableString (text node) or another tag
        if next_element:
            if isinstance(next_element, str): # For direct text nodes
                print(next_element.strip())
                pre_reqs = next_element.strip()
            else: # For cases where the text is inside another tag immediately after
                print(next_element.get_text().strip())
                pre_reqs = next_element.get_text().strip()
    else:
        print("Prerequisite(s): tag not found for course.")
    if pre_reqs:
        with open(outputname, "a") as file:
            file.write(course_id + " : " + pre_reqs + "\n")