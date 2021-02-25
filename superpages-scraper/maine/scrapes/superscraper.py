import requests
from lxml import html
import unicodecsv as csv
import argparse


def parse(keyword, location):

    url = 'https://www.superpages.com/search?search_terms={0}&geo_location_terms={1}'.format(keyword, location)

    print('retrieving ' + url)

    response = requests.get(url, verify=False, timeout=1)
    print("parsing page")
    if response.status_code == 200:
        parser = html.fromstring(response.text)

        base_url = 'https://www.superpages.com'
        parser.make_links_absolute(base_url)
        XPATH_LISTINGS = "//div[@class='search-results organic']//div[@class='v-card']"
        listings = parser.xpath(XPATH_LISTINGS)

        scraped_results = []
        for results in listings:
            XPATH_BUSINESS_NAME = ".//a[@class='business-name']//text()"
            XPATH_TELEPHONE = ".//a[@class='phones phone primary']//text()"
            XPATH_STREET = ".//div[@class='street-address']//text()"
            XPATH_CATEGORIES = ".//div[@class='info']//div[contains(@class,'info-section')]//div[@class='categories']//text()"
            XPATH_WEBSITE = ".//a[@class='weblink-button']/@href"

            raw_business_name = results.xpath(XPATH_BUSINESS_NAME)
            raw_telephone = results.xpath(XPATH_TELEPHONE)
            raw_address = results.xpath(XPATH_STREET)
            raw_categories = results.xpath(XPATH_CATEGORIES)
            raw_website = results.xpath(XPATH_WEBSITE)

            business_name = ''.join(raw_business_name).strip() if raw_business_name else None
            business_category = ','.join(raw_categories).strip() if raw_categories else None
            telephone = ''.join(raw_telephone[0]).strip() if raw_telephone else None
            street_address_full = ''.join(raw_address).strip() if raw_address else None
            street_address_split = street_address_full.split(',', 3) if street_address_full else None
            website = ''.join(raw_website).strip() if raw_website else None

            try:
                street = street_address_split[0]
            except:
                street = None
            try:
                city = street_address_split[1]
            except:
                city = None
            try:
                state = street_address_split[2]
            except:
                state = None
            try:
                zipcode = street_address_split[3]
            except:
                zipcode = None




            business_info = {
                'business_name': business_name,
                'telephone': telephone,
                'website': website,
                'category': business_category,
                'street': street,
                'locality': city,
                'region': state,
                'zipcode': zipcode
            }
            scraped_results.append(business_info)

        return (scraped_results)

    elif response.status_code == 404:
        print('Could not find matching location')
        pass
    else:
        print('Could not process page')




if __name__ == "__main__":

    argparser = argparse.ArgumentParser()
    argparser.add_argument('keyword', help='Search Keyword')
    argparser.add_argument('location', help='Place Name')

    args = argparser.parse_args()
    keyword = args.keyword
    location = args.location

    scraped_data = parse(keyword, location)

    if scraped_data:
        print("Writing scraped data to %s-%s-superpages-scraped-data.csv" % (keyword, location))
        with open('%s-%s-superpages-scraped-data.csv' % (keyword, location), 'wb') as csvfile:
            fieldnames = ['business_name', 'telephone', 'category', 'website',
                          'street', 'locality', 'region', 'zipcode']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer.writeheader()
            for data in scraped_data:
                writer.writerow(data)
