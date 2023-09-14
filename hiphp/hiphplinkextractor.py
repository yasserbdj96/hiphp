#!/usr/bin/env python
# coding:utf-8
#   |                                                         |   #
# --+---------------------------------------------------------+-- #
#   |    Code by: yasserbdj96                                 |   #
#   |    Email: yasser.bdj96@gmail.com                        |   #
#   |    GitHub: github.com/yasserbdj96                       |   #
#   |    Sponsor: github.com/sponsors/yasserbdj96             |   #
#   |    BTC: bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9      |   #
#   |                                                         |   #
#   |    All posts with #yasserbdj96                          |   #
#   |    All views are my own.                                |   #
# --+---------------------------------------------------------+-- #
#   |                                                         |   #

#START{
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse, urljoin


internal_urls = set()
external_urls = set()

# Define patterns for detecting CMS and versions
cms_patterns = [
    (r'WordPress', r'Version (\d+\.\d+\.\d+)'),
    (r'Joomla', r'Joomla! (\d+\.\d+)'),
    (r'vBulletin', r'vBulletin (\d+\.\d+\.\d+)'),
    # Add more CMS patterns as needed
]


def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_cms_and_version(html):
    """
    Detect CMS and its version in the HTML source code.
    """
    for cms, version_pattern in cms_patterns:
        match = re.search(cms, html, re.IGNORECASE)
        if match:
            version_match = re.search(version_pattern, html, re.IGNORECASE)
            version = version_match.group(1) if version_match else "Unknown"
            return cms, version
    return "Unknown", "Unknown"

def get_all_website_links(url):
    """
    Returns all URLs that belong to the same website and detects CMS and version.
    """
    # All URLs of `url`
    urls = set()
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    html = str(soup)  # Convert soup object back to HTML string for CMS detection
    cms, version = get_cms_and_version(html)
    
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            continue
        if urlparse(url).netloc not in href:
            continue
        if "mailto://" not in href:
            urls.add(href)
            internal_urls.add(href)
    return urls, cms, version
#print(crawl("https://asciinema.org/"))
#}END.