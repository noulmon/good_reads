import os
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from dotenv import load_dotenv

from utils import InvalidGoodreadsURL

# loading environmental variables
load_dotenv()


class GoodreadsAPIClient:

    def __init__(self):
        # getting API_KEY form .env file
        self.api_key = os.getenv('API_KEY')
        # GoodReads base url for book.show api
        self.base_url = 'https://www.goodreads.com/book/show/'

    def _get_title(self, xml_tree):
        '''
        :param xml_tree: api data(xml)
        :return: book title
        '''
        try:
            title = xml_tree.findtext('book/title')
            return title
        except Exception:
            return 'null'

    def _get_average_rating(self, xml_tree):
        '''
        :param xml_tree: api data(xml)
        :return: average rating of the book
        '''
        try:
            average_rating = xml_tree.findtext('book/average_rating')
            return float(average_rating)
        except Exception:
            return 'null'

    def _get_ratings_count(self, xml_tree):
        '''
        :param xml_tree: api data(xml)
        :return: Number of ratings
        '''
        try:
            rating_count = xml_tree.findtext('book/ratings_count')
            return int(rating_count)
        except Exception:
            return 'null'

    def _get_num_pages(self, xml_tree):
        '''
        :param xml_tree: api data(xml)
        :return: number of pages in the book
        '''
        try:
            num_pages = xml_tree.findtext('book/num_pages')
            return int(num_pages)
        except Exception:
            return 'null'

    def _get_image_url(self, xml_tree):
        '''
        :param xml_tree: api data(xml)
        :return: book cover image(url)
        '''
        try:
            image_url = xml_tree.findtext('book/image_url')
            return image_url
        except Exception:
            return 'null'

    def _get_publication_year(self, xml_tree):
        '''
        :param xml_tree: api data(xml)
        :return: book published year
        '''
        try:
            publication_year = xml_tree.findtext('book/publication_year')
            return publication_year
        except Exception:
            return 'null'

    def _get_authors(self, xml_tree):
        '''
        :param xml_tree: api data(xml)
        :return: book author name
        '''
        try:
            authors = xml_tree.findtext('book/authors/author/name')
            return authors
        except Exception:
            return 'null'

    def _get_isbn(self, url):
        '''
        :param url: the book url
        :return: ISBN from the given url
        '''
        try:
            isbn = url.split('show/')[-1].split('.')[0]
            if not isbn.isdigit():
                isbn = isbn.split('-')[0]
                if not isbn.isdigit():
                    raise InvalidGoodreadsURL
            return isbn
        except Exception as e:
            raise e

    def _get_xml_tree(self, isbn):
        '''
        :param isbn: Book ISBN
        :return: xml data
        '''
        try:
            api_url = f'{self.base_url}{isbn}.xml?key={self.api_key}'
            uh = urllib.request.urlopen(api_url)
            data = uh.read()
            xml_tree = ET.fromstring(data)
            return xml_tree
        except Exception as e:
            raise e

    def get_book_details(self, url):
        try:
            details = {}

            isbn = self._get_isbn(url)

            xml_tree = self._get_xml_tree(isbn)

            details['title'] = self._get_title(xml_tree)
            details['average_rating'] = self._get_average_rating(xml_tree)
            details['ratings_count'] = self._get_ratings_count(xml_tree)
            details['num_pages'] = self._get_num_pages(xml_tree)
            details['image_url'] = self._get_image_url(xml_tree)
            details['publication_year'] = self._get_publication_year(xml_tree)
            details['authors'] = self._get_authors(xml_tree)

            return details
        except Exception as e:
            raise e


if __name__ == '__main__':
    # instantiating the API client class
    gr_client = GoodreadsAPIClient()

    # getting input url
    url = sys.argv[1]
    # running get_book_details script
    print(gr_client.get_book_details(url))
