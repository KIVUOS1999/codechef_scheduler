from bs4 import BeautifulSoup
from msedge.selenium_tools import *
from selenium.webdriver.common.by import *
import selenium

def extract_data(soup):
    present_rows = soup.find_all('tr')
    present_contest = []
    for i in present_rows:
        temp = []
        for columns in i.find_all('td'):
            temp.append(columns.text)
        present_contest.append(temp)
    return present_contest

options = EdgeOptions()
options.use_chromium = True
options.add_argument("disable-gpu")
options.add_argument("headless")

url = "https://www.codechef.com/contests/?itm_medium=navmenu&itm_campaign=allcontests_head"

driver = Edge('E:/Django/msedgedriver.exe', options = options)
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

present_data = soup.find('tbody', {'id':'present-contests-data'})
future_data = soup.find('tbody', {'id':'future-contests-data'})

present_contest = extract_data(present_data)
future_contest = extract_data(future_data)
print(future_contest)