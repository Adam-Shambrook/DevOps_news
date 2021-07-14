import requests
from bs4 import BeautifulSoup
import pprint

# Keyword list:
list = ['cloud', 'Puppet', 'DevOps', 'Dev', 'IT','SSH', 'WinRM','Open-Source','Kubernetes', 'k8', 'Linux','Windows', 'Enterprise', 'Bank', 'Sysadmin', 'Compl', 'Secur']


res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
res3 = requests.get('https://news.ycombinator.com/news?p=3')
res4 = requests.get('https://news.ycombinator.com/news?p=4')
res5 = requests.get('https://news.ycombinator.com/news?p=5')
res6 = requests.get('https://news.ycombinator.com/news?p=6')

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
soup3 = BeautifulSoup(res3.text, 'html.parser')
soup4 = BeautifulSoup(res4.text, 'html.parser')
soup5 = BeautifulSoup(res5.text, 'html.parser')
soup6 = BeautifulSoup(res6.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')
links3 = soup3.select('.storylink')
subtext3 = soup3.select('.subtext')
links4 = soup4.select('.storylink')
subtext4 = soup4.select('.subtext')
links5 = soup5.select('.storylink')
subtext5 = soup5.select('.subtext')
links6 = soup6.select('.storylink')
subtext6 = soup6.select('.subtext')


mega_links = links + links2 + links3 + links4 + links5 + links6
mega_subtext = subtext + subtext2 + subtext3 + subtext4 + subtext5 + subtext6

def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      
      points = int(vote[0].getText().replace(' points', ''))
      for keyword in list:
        if keyword in title:
          hn.append({'title': title, 'link': href, 'votes': points})
  return sort_stories_by_votes(hn)
 
pprint.pprint(create_custom_hn(mega_links, mega_subtext))
