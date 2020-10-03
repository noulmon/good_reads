# BOOK DETAILS(GOODREADS)

### 1. Introduction:
_**BOOK DETAILS**_ is a 'Python Script' that fetches the details of a book from 'goodreads.com' when given the url to the book.


### 2. Follow the steps to _setup the script_:

1.1. Install all the required packages(python modules):

    ```pip install -r requirements.txt```
    
1.2. Add you API_KEY to the environment variables:

   Open the `.env` file and replace `<YOU_API_KEY_HERE>` with your goodreads API key for the variable API_KEY.

### 3. Running the Script:
To run the script, type following in your command line:

`python get_book_details.py <GOODREADS BOOK URL>`

Replace `<GOODREADS BOOK URL>` with a book url from goodreads.

Example:

`python get_book_details.py https://www.goodreads.com/book/show/12177850-a-song-of-ice-and-fire`

### 3. Running the Tests:

To run the tests, type the following in the command line:

`python -m unittest test`

### 4. Note:
 - If the url is invalid, the script will raise an exception `InvalidGoodreadsURL`.
 - API_KEY is mandatory for the script to work.

