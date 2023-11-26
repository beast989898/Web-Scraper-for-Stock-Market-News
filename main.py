import os
from os import listdir
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (StaleElementReferenceException,
                                        NoSuchElementException)
from selenium.webdriver.remote.webelement import WebElement
import time
import sys
import regex as re
from email.message import EmailMessage
import ssl
import smtplib

# Make sure you download both of these files in the same directory as this one
import regex_filters as rf
import filter_phrases as fp

# Pre compiled patterns since they are reused
compiled_regex_filters = [re.compile(phrase) for phrase in rf.regex_filter]


# Configuration for the Firefox browser
# Make sure you have Firefox installed
options = Options()
# If on another platform, replace with your path to firefox
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
# Turns off prompts for notifications
# (useful when testing and headless mode is off)
options.set_preference('dom.push.enabled', False)
# Prevents images from loading
options.set_preference('permissions.default.image', 2)
# Use the browser's default fonts
options.set_preference('browser.display.use_document_fonts', 0)
# Disables the pocket extension
options.set_preference('extensions.pocket.enabled', False)
# Enables incognito windows
options.add_argument('-private')
# Hides the browser window
options.add_argument('-headless')

geckodriver = Service()
driver = webdriver.Firefox(options=options, service=geckodriver)

# uBlock Origin blocks unwanted scripts and helps performance
# Complete with your path to uBlock Origin
try:
    addon_path = os.path.join("<PATH>", "ublock_origin-1.53.0.xpi")
    driver.install_addon(addon_path)
except FileNotFoundError:
    print("To use uBlock Origin, please ensure you downloaded the xpi file and"
          " the version number in path matches")

# Filter to search only specific exchanges
exchange = r"\((nasdaq|nyse)([a-z ]{0,14})?:.*\)"

# Filter to match with quarter reports
# There are many ways to write it, so this is not extensive
quarter_reports = ("(report[a-z]{0,3}|announc[a-z]{1,3}) (results for the )?"
                   r"(\d{4} )?(first|second|third|fourth)[ -]quarter")


def send_email(to_email: str, address: str) -> None:
    """Sends an email from a predetermined address

    Args:
        to_email (str): The body of the email
        address (str): the recipient email address
    """

    # Environemt variables to store your email and its password
    # You can replace this according to your threat model
    email_sender = str(os.environ.get("EMAIL_SENDER"))
    email_password = str(os.environ.get("EMAIL_PASSWORD"))
    email_receiver = address
    subject = "New Article"
    em = EmailMessage()
    body = to_email
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


def find_new_articles(path: str, titles: list[WebElement]) -> list[str]:
    """Finds the new articles from all the articles on a page

    Args:
        path (str): Path to a txt file where the article links will be printed
        titles (list[WebElement]): The elements containing an article url

    Returns:
        list[str]: The new articles
    """

    if not os.path.exists(path):
        open(path, 'w').close()

    with open(path) as file_handler:
        all_articles_list = file_handler.read().splitlines()

    new_articles = []
    for article in titles:
        article_link = article.get_attribute("href")

        if article_link not in all_articles_list:
            new_articles.append(article_link)

            with open(path, 'a') as file_handler:
                file_handler.write("{}\n".format(article_link))

    return new_articles


def new_articles_count(new_articles: list[str]) -> None:
    """Prints out the number of new articles on a webpage
    since the program's last execution

    Args:
        new_articles (list[str]): List of new articles found on a website
    """

    if len(new_articles) == 0:
        print("There is no new article")
    elif len(new_articles) == 1:
        print("There is 1 new article")
    else:
        print("There are " + str(len(new_articles)) + " new articles")


def find_matches(article_content: str) -> None:
    """Looks for matches in the articles, omitting quarter reports

    Args:
        article_content (str): The headline and body of the article
    """

    if not re.search(quarter_reports, article_content):
        if any(re.search(phrase, article_content) for phrase
               in compiled_regex_filters):
            send_email(link, "")  # The recipient email is the second parameter
            print("match: " + link)
        elif any(phrase in article_content for phrase in fp.filter_phrases):
            send_email(link, "")  # The recipient email is the second parameter
            print("match: " + link)


def find_matches_with_exchange(article_content: str) -> None:
    """Looks for matches in the articles, omitting quarter reports
    Only articles of specified stock exchanges will match

    Args:
        article_content (str): The headline and body of the article
    """

    if re.search(exchange, article_content) \
            and not re.search(quarter_reports, article_content):
        if any(re.search(phrase, article_content) for phrase in
               compiled_regex_filters):
            send_email(link, "")  # The recipient email
            print("match: " + link)
        elif any(phrase in article_content for phrase in fp.filter_phrases):
            send_email(link, "")  # The recipient email
            print("match: " + link)


print("Now checking GlobeNewswire")


driver.get("https://www.globenewswire.com/search/exchange/nasdaq,nyse"
           "/lang/en?pageSize=20")

article_titles = driver.find_elements(By.XPATH,
                                      "//a[@data-autid='article-url']")

# The location where you want the txt files to save
# This file can be deleted to reset the list of articles seen
new_articles = find_new_articles(
    os.path.join("<PATH>" "articles.txt"), article_titles)
new_articles_count(new_articles)

for link in new_articles:
    driver.get(link)
    article_content = ""
    try:  # Attempt to find the contents of each article
        article_content = driver.find_element(By.CLASS_NAME,
                                              "main-container.container"
                                              "-overwrite").text.lower()
    except (StaleElementReferenceException, NoSuchElementException):
        # If the content of the article cannot be found
        print("Article body not found")
    find_matches(article_content)


print("Now checking Business Wire")

driver.get("https://www.businesswire.com/portal/site/home/news/")

article_titles_2 = driver.find_elements(By.XPATH, "//a[@class='bwTitleLink']")

# The location where you want the txt files to save
# This file can be deleted to reset the list of articles seen
new_articles_2 = find_new_articles(os.path.join(
    "<PATH>" "articles2.txt"), article_titles_2)
new_articles_count(new_articles_2)

for link in new_articles_2:
    driver.get(link)
    article_content = ""
    try:  # Attempt to find the contents of each article
        article_content = driver.find_element(By.CLASS_NAME,
                                              "bw-release-main").text.lower()
    except (StaleElementReferenceException, NoSuchElementException):
        # If the content of the article cannot be found
        print("Article body not found")
    find_matches_with_exchange(article_content)


print("Now checking ACCESSWIRE")

driver.get("https://www.accesswire.com/newsroom/")

article_titles_3 = driver.find_elements(By.CLASS_NAME, "articletitle.new")

# The location where you want the txt files to save
# This file can be deleted to reset the list of articles seen
new_articles_3 = find_new_articles(os.path.join(
    "<PATH>" "articles3.txt"), article_titles_3)
new_articles_count(new_articles_3)

for link in new_articles_3:
    driver.get(link)
    article_content = ""
    try:  # Attempt to find the contents of each article
        article_content = driver.find_element(By.CLASS_NAME,
                                              "section-4.article-u-pdate."
                                              "wf-section").text.lower()
    except (StaleElementReferenceException, NoSuchElementException):
        # If the content of the article cannot be found
        print("Article body not found")
    find_matches_with_exchange(article_content)


print("Now checking PR Newswire")

driver.get("https://www.prnewswire.com/news-releases/news-releases-list/"
           "?page=1&pagesize=50")

article_titles_4 = driver.find_elements(By.CLASS_NAME,
                                        "newsreleaseconsolidatelink.display"
                                        "-outline.w-100")

# The location where you want the txt files to save
# This file can be deleted to reset the list of articles seen
new_articles_4 = find_new_articles(os.path.join("<PATH>" "articles4.txt"),
                                   article_titles_4)
new_articles_count(new_articles_4)

for link in new_articles_4:
    driver.get(link)
    article_content = ""
    try:  # Attempt to find the contents of each article
        article_content = driver.find_element(By.TAG_NAME,
                                              "article").text.lower()
    except (StaleElementReferenceException, NoSuchElementException):
        # If the content of the article cannot be found
        print("Article body not found")
    find_matches_with_exchange(article_content)

# Cleanup of temp files
driver.quit()
# Replace <YOUR_TEMP_FOLDER> with the path to your temp folder
# This deletes the copy of uBlock Origin stored in the temp folder
# A new one is created for each execution
for file_name in listdir("<YOUR_TEMP_FOLDER>"):
    if file_name.endswith('.xpi'):
        os.remove("<YOUR_TEMP_FOLDER>" + file_name)

print("Preparing to refresh", time.strftime("%H:%M:%S"))
time.sleep(30)
print("30 seconds passed, refreshing...")

# Rerun program from start
os.execv(sys.executable, [sys.executable, os.path.realpath(__file__)]
         + sys.argv[1:])
