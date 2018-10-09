import emails as em
from bs4 import BeautifulSoup as bs
import requests as rq

"""
Functions:
get_top() - get top posts from subreddit
format() - format email body

Vars:
time_of_send - time the scraper is currently set to run

"""
def get_top(subreddit, sort='day'):
    """ Gets top 3 entries from specified subreddit based on sort
    
    Args:
    subreddit - subreddit to extract posts from
    sort - sorting of subreddit posts to apply

    """

def main():
    credentials = em.get_credentials()
    service = em.get_service(credentials)

    sender = 'me'
    to = 'christopher.j.sparling@gmail.com'
    subject = 'Testing'
    body = 'Testing Body'
    msg = em.create_message(sender, to, subject, body)
    em.send_message(service, 'me',msg)

if __name__ == '__main__':
    main()