class ElementNotClicked(Exception):
    def __init__(self, message):
        super().__init__(message)


class ElementNotDisplayed(Exception):
    def __init__(self, message):
        super().__init__(message)

class ElementNotClickable(Exception):
    def __init__(self,message):
        super().__init__(message)

class ElementDisplayed(Exception):
    def __init__(self,message):
        super().__init__(message)

class DataNotAvailable(Exception):
    def __init__(self,message):
        super().__init__(message)

class WrongPassword(Exception):
    def __init__(self,message):
        super().__init__(message)