class InvalidGoodreadsURL(Exception):
    def __init__(self, message='Invalid book URL'):
        self.message = message
        super().__init__(self.message)
