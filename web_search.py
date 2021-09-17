import requests
import urllib
from requests_html import HTMLSession
import re
from bs4 import BeautifulSoup


def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        print(response)
        return response

    except requests.exceptions.RequestException as e:
        print(e)


def scrape_google(query):
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.',
                      'https://google.',
                      'https://webcache.googleusercontent.',
                      'http://webcache.googleusercontent.',
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    list_filtered = [re.sub(r'(https://translate.google.com/translate)', '', file) for file in links]
    filtered_values = list(filter(lambda v: re.match('(https://(gatherer\.wizards)[.][a-z]{2,4}/(?:[^\s()<>]+))', v), list_filtered))
    filtered_url = "".join(filtered_values)
    page = requests.get(filtered_url, verify=False)
    soup = BeautifulSoup(page.content, "html.parser")
    # results = soup.find(id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_rightCol")
    name_elements = soup.find(id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_nameRow")
    job_elements = name_elements.find_all("div", class_="value")
    cardname_list = []
    for job_element in job_elements:
        cardname_list.append(job_element)
    cardname_final = " ".join(cardname_list)
    print(cardname_final)
    # for job_element in job_elements:
    #     cardname = job_element.find_all("div", class_="value")
    #     print(cardname)

    # job_elements = results.find_all("div", class_="gathererContent")
    # for job_element in job_elements:
    #     print(job_element, end="\n" * 2)
    # for job_element in job_elements:
    #     cardname = job_element.find(id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_nameRow")
    #     print(cardname)
    # cardbox_list = []
    # for job_element in job_elements:
    #     cardtextbox = job_element.find_all("div", class_="cardtextbox")
    #     for text in cardtextbox:
    #         cardbox_list.append(text.text)
    # print(cardbox_list)
    # for job_element in job_elements:
    #     name_element = job_element.find("Card Name:", class_="label")
        # company_element = job_element.find("h3", class_="company")
        # location_element = job_element.find("p", class_="location")
        # print(name_element)
        # print(company_element)
        # print(location_element)

    return filtered_url




