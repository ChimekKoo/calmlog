class Level:
    def __init__(self, levelname):
        if not isinstance(levelname, str):
            raise TypeError("'levelname' param must be a string.")
        else:
            self.name = levelname

    def getname(self):
        return self.name


DEBUG = Level("DEBUG")
INFO = Level("INFO")
WARRING = Level("WARRING")
ERROR = Level("ERROR")
FATAL = Level("FATAL")
