# BOOK DETAILS(GOODREADS)

### Introduction:
_**BOOK DETAILS**_ is a 'Python Script' that fetches the details of a book from 'goodreads.com' when given the url to the book.


### Follow the steps to _setup the script_:

1. Install all the required packages(python modules):

    ```pip install -r requirements.txt```
    
2. Add you API_KEY to the environment variables:

   Open the `.env` file and replace `<YOU_API_KEY_HERE>` with your goodreads API key for the variable API_KEY.

### Running the Script:
To run the script, type following in your command line:
`python get_book_details.py <GOODREADS BOOK URL>`

Replace `<GOODREADS BOOK URL>` with a book url from goodreads.

Example:

`get_book_details.py https://www.goodreads.com/book/show/12177850-a-song-of-ice-and-fire`

### Note:
 - If the url is invalid, the script will raise an exception`InvalidGoodreadsURL`.
 - API_KEY is mandatory for the script to work.

