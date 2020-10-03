class InvalidGoodreadsURL(Exception):
    def __init__(self, message='Invalid URL'):
        self.message = message
        super().__init__(self.message)
