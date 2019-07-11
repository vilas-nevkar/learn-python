import logging
import requests


class Crawler:
    def __init__(self, url=''):
        logging.basicConfig(level=logging.INFO, filename='crawler.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        self.url = url

    def send_request(self, url='', retries=2):
        try:
            response = requests.get(url=url)
            self.logger.info("downloading response from url {}".format(url))
        except Exception as e:
            response = None
            self.logger.error('request failed', e)
            if retries > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    self.logger.info('retrying page request')
                    return self.send_request(url, retries - 1)
        self.logger.info("response fetched from url {}".format(url))
        return response.text

    def make_dict(self, response):
        pass


def main():
    url = 'http://www.santabanta.com/photos/mk-boina/26051016.htm'
    parser = Crawler(url=url)
    response = parser.send_request(url=url)
    print(response)


if __name__ == '__main__':
    main()