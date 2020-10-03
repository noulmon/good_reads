import unittest

from get_book_details import GoodreadsAPIClient


class TestBookDetails(unittest.TestCase):
    gr_client = GoodreadsAPIClient()

    def test_success_response_01(self):
        expected_output = {'title': 'A Song of Ice and Fire (A Song of Ice and Fire, #1-5)', 'num_pages': 5216,
                           'image_url': 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1339340118l/12177850._SX98_.jpg',
                           'publication_year': '2011', 'authors': 'George R.R. Martin'}

        result = self.gr_client.get_book_details("https://www.goodreads.com/book/show/12177850-a-song-of-ice-and-fire")
        result.pop('average_rating')
        result.pop('ratings_count')

        self.assertEqual(result, expected_output)

    def test_success_response_02(self):
        expected_output = {
            'title': 'Disloyal: The True Story of the Former Personal Attorney to President Donald J. Trump',
            'num_pages': 'null',
            'image_url': 'https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png',
            'publication_year': '2020', 'authors': 'Michael   Cohen'}

        result = self.gr_client.get_book_details("https://www.goodreads.com/book/show/54916250-disloyal")
        result.pop('average_rating')
        result.pop('ratings_count')

        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
