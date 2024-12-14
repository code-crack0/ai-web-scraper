import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
def scrape_website(url):
    print("Launching the browser...")
    chrome_driver_path = "./chromedriver/chromedriver-win64/chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(url)
        print("Webiste Loaded")
        html = driver.page_source
        return html
    finally:
        driver.quit()

def extract_body_content(html):
    # Add the code to extract the body content here
    souo = BeautifulSoup(html, 'html.parser')
    body = souo.body
    if body:
        return str(body)
    return ""
def clean_body_content(body_content):
    # Add the code to clean the body content here
    soup = BeautifulSoup(body_content, 'html.parser')
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join([line.strip() for line in cleaned_content.split("\n") if line.strip()])
    return cleaned_content

def split_dom_content(dom_content,max_length=6000):
    return [dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)]