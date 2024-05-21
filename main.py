from aluminum import scrape_aluminum
from cobalt import scrape_cobalt
from copper import scrape_copper
from lead import scrape_lead
from nickel import scrape_nickel
from tin import scrape_tin
from zinc import scrape_zinc

def main():
    # Call each scraper function
    scrape_aluminum()
    scrape_cobalt()
    scrape_copper()
    scrape_lead()
    scrape_nickel()
    scrape_tin()
    scrape_zinc()

if __name__ == "__main__":
    main()
