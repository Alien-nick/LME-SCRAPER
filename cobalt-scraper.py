import cfscrape
import json

# Create a CloudflareScraper instance
scraper = cfscrape.create_scraper(delay=25)

# Define the URL to crawl
url = 'https://www.lme.com/api/trading-data/day-delayed?datasourceId=2b5439b2-f8c0-4b3b-8bf7-ba2a851f00ab'

# Make the request
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': '_cfuvid=8idh8ac1si2fEtdlTK7PinRf6quXr6JDlvUgXB4pWDs-1716202576673-0.0.1.1-604800000; shell#lang=en; ai_user=66tORjIrH5zRy8/ZqehbzV|2024-05-20T11:26:13.418Z; lme#lang=en; ASP.NET_SessionId=fm0gcn34m3tqumkisa5c2ver; OptanonConsent=isGpcEnabled=0&datestamp=Mon+May+20+2024+07%3A30%3A43+GMT-0400+(Guyana+Time)&version=6.19.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0002%3A0%2CC0004%3A0&AwaitingReconsent=false; __cf_bm=rQ4D17FQkCefZ4wUro7G5hWnHlyOo_cLTz.O0kGO2OQ-1716223570-1.0.1.1-asKFlMgtm0_fnSop.AbDUeDi3Yqn6HVg_XlQMuV26Uwf0TZXtPRg6lAM6cdT5ol.YQ60pSL4XSrjLzCV3dEI5Q; cf_clearance=nIhYKlahknlIT8AECuuK4B1Mvj6REHdl6zQqEQKpkEk-1716223919-1.0.1.1-OePvLJOUDWGY8mkVclqDp_fLvDI5jH6Dhhso35pbrEVRyMlXYDhteeV1gxXLH7X8fGWKD34EZpJp2_HXkY0PpA',
  'Priority': 'u=0, i',
  'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
  'Sec-Ch-Ua-Arch': '"x86"',
  'Sec-Ch-Ua-Bitness': '"64"',
  'Sec-Ch-Ua-Full-Version': '"124.0.6367.209"',
  'Sec-Ch-Ua-Full-Version-List': '"Chromium";v="124.0.6367.209", "Google Chrome";v="124.0.6367.209", "Not-A.Brand";v="99.0.0.0"',
  'Sec-Ch-Ua-Mobile': '?0',
  'Sec-Ch-Ua-Model': '""',
  'Sec-Ch-Ua-Platform': '"Windows"',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1'
}
res = scraper.get(url, headers=headers)

print(res)

# Load the JSON data
data = json.loads(res.text)

# Initialize variables to hold the values
cash_values = None
three_month_values = None

# Iterate through the rows to find the relevant entries
for row in data['Rows']:
    if row['RowTitle'] == 'Cash':
        cash_values = row['Values']
    elif row['RowTitle'] == '3-month':
        three_month_values = row['Values']

# Check if values are found and construct the JSON response
if cash_values and three_month_values:
    response_data = {
        "3_month_value_1": three_month_values[0],
        "3_month_value_2": three_month_values[1],
        "cash_value_1": cash_values[0],
        "cash_value_2": cash_values[1]
    }
    # Convert the response data to JSON and print it
    print(json.dumps(response_data))
else:
    # If relevant data is not found, print an empty JSON object
    print(json.dumps({}))