import scrapy
from urllib.parse import urlencode, quote

def get_zenrows_api_url(url, api_key):
    # Creates a ZenRows proxy URL for a given target_URL using the provided API key.
    payload = {
        'url': url,
        'js_render': 'true',
        'antibot': 'true',
        'premium_proxy': 'true'
    }
    
    # Construct the API URL by appending the encoded payload to the base URL with the API key
    api_url = f'https://api.zenrows.com/v1/?apikey={api_key}&{urlencode(payload)}'
    return api_url

class PhishSpider(scrapy.Spider):
    name = "phish"

    def start_requests(self):
        urls = [
            'https://www.phishtank.com/',
        ]
        api_key = 'e59b15ba65ee8f944947f6f230cfaf4fb734f599'
        for url in urls:
            # make a GET request using the ZenRows API URL
            api_url = get_zenrows_api_url(url, api_key)
            yield scrapy.Request(api_url, callback=self.parse)

    def parse(self, response):
        title = response.css('title::text').get()
        self.logger.info(f"Title: {title}")