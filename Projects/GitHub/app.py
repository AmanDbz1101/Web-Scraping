import streamlit as st 
from bs4 import BeautifulSoup
import requests
import pandas as pd

st.title('GitHub Mini Scrapper')

st.write('This is a mini scrapper that will scrape the top GitHub repositories for different topics.')

# st.button('Start Scraping')

def get_user_project(repo):
    base_url = 'https://github.com'
    a_tags = repo.find_all('a')
    user_tag = a_tags[0].text.strip()
    project_tag = a_tags[1].text.strip()
    project_url = base_url + a_tags[1].get('href')
    return user_tag, project_tag, project_url

#loading the data of the page topics
url = 'https://github.com/topics'
response = requests.get(url )
page = BeautifulSoup(response.text, 'html.parser')

topics = page.find_all('p', class_='f3 lh-condensed mb-0 mt-1 Link--primary')
description = page.find_all('p', class_='f5 color-fg-muted mb-0 mt-1')
links = page.find_all('a', class_='no-underline flex-grow-0')
topics_list = []
for topic in topics:
    topics_list.append(topic.text.strip())

description_list = []
for desc in description:
    description_list.append(desc.text.strip())

links_list = []
for link in links:
    links_list.append('https://github.com' + link.get('href'))
    
data_dict = {
    'Topic': topics_list,
    'Description': description_list,
    'Link': links_list
}

data = pd.DataFrame(data_dict)

st.header("Top topics found")

st.dataframe(data)
    
options = st.multiselect(
    "Choose the topics you want to scrape",
    data['Topic'],
)

# st.write("You selected:", options)

# st.button('Start Scraping')


if st.button:

    for link, topic in zip(data['Link'] , data['Topic']):
        
        if topic in options:
            st.write(f'Scraping top repositories for {topic}')
            
            response = requests.get(link)
            page = BeautifulSoup(response.text, 'html.parser')
            repos = page.find_all('h3', class_ = 'f3 color-fg-muted text-normal lh-condensed')
            stars_count = page.find_all('span', class_ = 'Counter js-social-count')
            description = page.find_all('p', class_ = 'color-fg-muted mb-0')
            user_tags = []
            project_tags = []   
            project_urls = []
            stars = []
            for repo in repos:
                user_tag, project_tag, project_url = get_user_project(repo)
                user_tags.append(user_tag)
                project_tags.append(project_tag)
                project_urls.append(project_url)
            for star in stars_count:
                if ('k' in star.text.strip()):
                    stars.append(int(float(star.text.strip().replace('k', '')) * 1000))
                else:
                    stars.append(int(star.text.strip()))
            description_data = []
            for desc in description:
                description_data.append(desc.text.strip())
            
            page_dict = {
                'User': user_tags,
                'Project': project_tags,
                'Project URL': project_urls,
                'Stars': stars,
                'Description': description_data
            }
            page_df = pd.DataFrame(page_dict)
            st.dataframe(page_df)
        
    