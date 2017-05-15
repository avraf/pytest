# Create a decorator function called historian.
# The historian decorator, when applied, should record the history of an instance method.
# For any instance method that the historian decorates, the historian function should
# create an attribute with the same name as the method with the string '_history' sufixed
# to it. This attribute is a list of all previous calls represented as a tuple where its
# first element is a tuple of actual call arguments and the second element being a dict
# of the keyword arguments that were supplied. If the function was not supplied args or
# kwargs then the tuple of args and dict of kwargs will be empty.
# i.e

A_function_history == [
    ( # First call to function
        (1,2), # First set of arguements supplied
        {'name': 'Bobby', 'last_name': 'jones'} # First set of kwargs supplied
    ),
    ( # second call to function
        (), # No arguments were supplied
        {'name': 'Larry', 'last_name': 'Mendes'}
    )
]

# Use of your decorator should look like this:

class Cow(object):
    name = 'Dan'
    @historian
    def moo(self):
        return self.name

    @historian
    def chew(self, food='hay'):
        return self.name

betsy = Cow()
betsy.chew()
betsy.moo()
betsy.chew('corn')
betsy.moo()
betsy.chew(food='nachos')

betsy.chew_history # => [ ( (), {} ),( ('corn',), {} ), ( (), {'food': 'nachos'} ) ]
betsy.moo_history # => [ ( (), {} ), ( (), {} ) ]
