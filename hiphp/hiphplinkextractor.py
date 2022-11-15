import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

# initialize the set of links (unique links)
internal_urls = set()
external_urls = set()


def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_website_links(url):
    """
    Returns all URLs that is found on `url` in which it belongs to the same website
    """
    # all URLs of `url`
    urls = set()
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href empty tag
            continue
        # join the URL if it's relative (not absolute link)
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            # not a valid URL
            continue
        if href in internal_urls:
            # already in the set
            continue
        if urlparse(url).netloc not in href:
            # external link
            if href not in external_urls:
                #print(f"[!] External link: {href}")
                external_urls.add(href)
            continue
        #print(f"[*] Internal link: {href}")
        if "mailto://" not in href:
            urls.add(href)
            internal_urls.add(href)
    return urls

#print(crawl("https://asciinema.org/"))