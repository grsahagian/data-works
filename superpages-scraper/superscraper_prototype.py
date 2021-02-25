import requests
from bs4 import BeautifulSoup


def parse(keyword, location):

    url = 'https://www.superpages.com/search?search_terms={0}&geo_location_terms={1}'.format(keyword, location)

    print('retrieving ' + url)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
               'referer': 'https://www.google.com',
               'Connection': 'keep-alive',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7',
               'Cache-Control': 'max-age=0',
               'Content-Encoding': 'gzip',
               'Upgrade-Insecure-Requests': '1',
               'Host':'www.superpages.com'}

    for retry in range(10):
        try:
            response = requests.get(url, verify=False, headers=headers)
            print('parsing page')
            print(response.status_code)
            if response.status_code == 200:
                request = response.text
                page = BeautifulSoup(request, 'lxml')


                scraped_results = []


                for result in page.findall('div', class_='result'):
                    name = result.find('a', class_='business-name')
                    business_name = name.span.text
                    #
                    categories = []
                    for category in result.find('div', {'class': 'categories'}):
                        x = category.text
                        categories.append(x)
                    #
                    address = result.find('div', {'class': 'street-address'})
                    address = address.text.split(',', 3)
                    street = address[0]
                    city = address[1]
                    state = address[2]
                    zip = address[3]
                    #
                    phone = result.find('span', {'class': 'call-number'})
                    phone = phone.text
                    #
                    try:
                        website = result.find('a', class_='weblink-button')['href']
                    except TypeError:
                        website = 'None Listed'
                    #
                    business_details = {
                        'business_name': business_name,
                        'telephone': phone,
                        'category': categories,
                        'website': website,
                        'street': street,
                        'locality': city,
                        'region': state,
                        'zipcode': zip,
                    }
                    scraped_results.append(business_details)

                print(scraped_results)
            elif response == 404:
                print("Could not find a matching location", location)
                break
            else:
                print("Failed to process page2")
                return []
        except:
            print("Failed to process page1")
            return []

parse('property+managers','Boston,MA')









