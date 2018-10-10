import emails as em
from bs4 import BeautifulSoup as bs
import requests as rq
import example_html as exam
import templates as tmp
"""
Functions:
get_top() - get top posts from subreddit
format() - format email body

Vars:
time_of_send - time the scraper is currently set to run
subreddits - list of subreddits to scrape
"""
BASE = 'https://www.reddit.com/r/'
SUFFIX = '/top/?sort=top&t='
SUBREDDITS= ['machinelearning',
             'deeplearning',
             'datascience'
             'artificial']

def get_top(subreddits, sort='day'):
    """ Gets top 3 entries from specified subreddit based on sort
    
    Args:
    subreddit - subreddit to extract posts from [list]
    sort - sorting of subreddit posts to apply

    Returns:
      Dictionary of subreddits with list of lists as value 
    """
    
# def format_title(text):

def format_main(subreddit_dict):
    """ Populates HTML string for message body using section templates
    Args:
    subreddit_dict - list of dictionaries; one per subreddit
    
    Returns:
      Populated multi-line string
    """
    # Bundle the item groups together
    def format_items(item_list):
        to_join = [tmp.item.format(item[0],item[1]) for item in item_list]
        return ' '.join(to_join)

    # Bundle the section groups together
    def format_sections(section_list):
        to_join = [tmp.section.format(subreddit,format_items(value)) for subreddit,value in section_list.items()]
        return ' '.join(to_join)

    return tmp.main.format('date goes here', format_sections(subreddit_dict))

def main():
    credentials = em.get_credentials()
    service = em.get_service(credentials)

    # temp = 'https://us6.proxysite.com/process.php?d=q9Dy%2BJkZhKqpXas9Pb4rSGZ%2ByCeziWn6hMVdrD9dolRaN1GBfajFnttSFqyi1An0LN4vgWSWh8Q%3D&b=1&f=norefer'
    # temp = 'https://us6.proxysite.com/process.php?d=q9Dy%2BJkZhKqpXas9Pb4rSGZ%2ByCeziWn6hMVdrD9dolRaN1GB&b=1&f=norefer'
    # data = rq.get(BASE + SUBREDDITS[0] + SUFFIX)
    # data = rq.get(temp)
    soup = bs(exam.document, 'html5lib')
    # print(soup.prettify())

    # Extract and format 3 titles 
    headers = soup.find_all('h2',class_='s56cc5r-0', limit=3)
    for counter, item in enumerate(headers):
        headers[counter] = ' '.join(item.text.split())
        print(headers[counter])
    # Extract links to items
    links = soup.find_all('a',class_='SQnoC3ObvgnGjWt90zD9Z', limit=3)
    for counter,item in enumerate(links):
        links[counter] = item['href']

    sender = 'me'
    to = 'christopher.sparling@litens.com'
    subject = 'Testing'
    

    msg = em.create_message(sender, to, subject, body)
    em.send_message(service, 'me',msg)


if __name__ == '__main__':
    main()