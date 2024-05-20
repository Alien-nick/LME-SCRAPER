import cfscrape
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the handler class to handle HTTP requests
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Create a CloudflareScraper instance
        scraper = cfscrape.create_scraper(delay=15)

        # Define the URL to crawl
        url = 'https://www.lme.com/api/trading-data/day-delayed?datasourceId=762a3883-b0e1-4c18-b34b-fe97a1f2d3a5'

        # Make the request
        # cookie, user_agent=scraper.get_cookie_string("https://www.lme.com/api/trading-data/day-delayed?datasourceId=762a3883-b0e1-4c18-b34b-fe97a1f2d3a5")
        headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '__cf_bm=pUuRKxSyV1arjECh36D3KwZ4tbglJbzDvsDL1W.t7Xs-1716202573-1.0.1.1-aWSQ20SyouMfOG9IVfRdMwJKU9eruZlWuK58j3zazTp3q06LQQ7UBglAykqmusSMqaXzwRflXThso4ivBuvUXQ; _cfuvid=8idh8ac1si2fEtdlTK7PinRf6quXr6JDlvUgXB4pWDs-1716202576673-0.0.1.1-604800000; cf_clearance=Nb4CxbcEzUfZQn.rAp8RDPzjaTH5Wgeq_ZHV_1lLbVk-1716203246-1.0.1.1-fr5Fa4WtjEW1.9ohSH7jHrIaznq_YB6Dk0uhSTIRfR_Pzr1._UFkafxtMxFogYxKwZvJcGzUhMd3UYNKDkqlOg; __cf_bm=JH0dCj9Wg3f_6OBFjhwSstxUtZFrleh8fTJ2afsBWLM-1716204054-1.0.1.1-N4V0fzTNABWBpcN3fpA0Uq3j7XCrT8IidJqP20WRUIQwztxywONLPoK1WsGH4x9cIGEDvytOPvCty9OBTvTSrw; _cfuvid=GIXpaNI8IChmmA2AZwAFqVJpm7FkyDygjVKIt9C81z8-1716203765151-0.0.1.1-604800000',
        'Priority': 'u=0, i',
        'Referer': 'https://www.lme.com/api/trading-data/day-delayed?datasourceId=762a3883-b0e1-4c18-b34b-fe97a1f2d3a5&__cf_chl_tk=2SHpJJhen6N0u4SG60WhO_jpttjzmXXGpUwZ_4uracY-1716203246-0.0.1.1-1770',
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
            # Convert the response data to JSON
            json_response = json.dumps(response_data)
            # Set the response headers
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # Write the JSON response to the client
            self.wfile.write(json_response.encode())
        else:
            # If relevant data is not found, return a 404 status code
            self.send_response(404)
            self.end_headers()

# Define the server address and port
server_address = ('', 9022)

# Create an HTTP server with the defined handler
httpd = HTTPServer(server_address, RequestHandler)

# Start the HTTP server
print('Starting server...')
httpd.serve_forever()