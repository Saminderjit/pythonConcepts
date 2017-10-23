"""For more info visit
https://stackoverflow.com/questions/38524332/declaring-decorator-inside-a-class """


def enter_exit_formatting(func):
    def wrapper(self, *args, **kw):
        print "Inside decorator calling function", func.__name__
        func(self)
        print "Inside decorator but outside function", func.__name__
        return None
    return wrapper


class Names(object):
    """ Module to print names in uppercase and lowercase """
    def __init__(self, name):
        self.name = name

    @enter_exit_formatting
    def print_name_in_lowercase(self):
        print "Inside original function"
        print self.name.lower()

    def print_name_in_uppercase(self):
        print self.name.upper()


sample = Names('Saminder')
a = sample.print_name_in_lowercase()
sample.print_name_in_uppercase()
