class TooShortPasswordException(ValueError):
    def __init__(self):
        super().__init__("Password should be at least 8 characters")
