class ExceptionExample(Exception):
    def _init_(self, message):
        self.message = message

    def _str_(self):
        return repr(self.message)


try:
    x = input("Insert a word:\n")
    if x.isdigit():
        raise ExceptionExample
except ExceptionExample:
    print("Found a number.")
except Exception:
    print("Any exception.")