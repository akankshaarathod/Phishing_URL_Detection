
try:
    import whois
except:
    import sys
    import subprocess
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    'python-whois']) # For getting domain age
import requests
import pandas as pd
import whois
from bs4 import BeautifulSoup
from dateutil.parser import parse
from datetime import datetime


def check_google_index(url):
    try:
        response = requests.get(f"http://www.google.com/search?q=site:{url}")
        if response.status_code == 200 and url in response.text:
            return 1
    except requests.RequestException as e:
        print(f"Error accessing Google search: {e}")
    except Exception as ex:
        print(f"An error occurred: {ex}")
    return 0


def calculate_digit_ratio(url): #ratio bwn no of digits to the length of the url
    digit_count = sum(char.isdigit() for char in url)
    digit_ratio = digit_count / len(url)
    return digit_ratio

#hyperlink counts in your website, counts number of anchor tags and returns


# def count_hyperlinks(url):
#     try:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         hyperlink_tags = soup.find_all('a')
#         return len(hyperlink_tags)
#     except requests.RequestException as e:
#         print(f"Error accessing URL: {e}")
#     except Exception as ex:
#         print(f"An error occurred: {ex}")
#     return 0

def nb_qm_slash_www(url):
    question_mark_count = url.count('?')
    slash_count = url.count('/')
    www_count = url.count('www')
    return question_mark_count, slash_count, www_count



def get_domain_age(url):
    try:
        domain = whois.whois(url)
        creation_date = domain.creation_date
        if creation_date is not None:
            if isinstance(creation_date, list):
                creation_date = creation_date[0]
            if creation_date:
                # Parse the creation date string and calculate the age in days
                creation_date = parse(str(creation_date))
                age = (datetime.now() - creation_date).days
                return age
        else:
            return -1
    except:
        return -1


def feature_extractor(url):
    nb_qm, nb_slash, nb_www = nb_qm_slash_www(url)
    test_input = pd.DataFrame({
            'google_index' : [check_google_index(url)],
            'ratio_digits_url' : [calculate_digit_ratio(url)],
            'nb_qm' : [nb_qm],
            'length_url' : [len(url)],
            'nb_slash' : [nb_slash],
            'domain_age' : [get_domain_age(url)],
            # 'nb_hyperlinks' : [count_hyperlinks(url)],
            'nb_www' : [nb_www]
        })

    return test_input
