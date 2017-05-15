# Create a SQL DSL.
# The SQL DSL will automatically be connected to a database.
# So you don't need to worry about providing a connection to a DB.
# The DB will provide a list of JSON like objects. 
# Meaning you can access each item's attributes with `item['attr']` keyname notation or
# `item.attr` dot notation.
# Provided is a class select (note lower case 's') that has a class attribute db (the
# target Database).
# The select class' constuctor should recieve wanted columns or '*' for all columns.
# i.e.
select('*')

# Or

select('name', 'title')

# The class select has a method from_table which receives a table name and returns a
# callable (method, function, lambda, etc), who can be given zero parameters or keyword
# arguements where and/or order_by.
# i.e.

select('*').from_table('faculty')()

# Notice dot notation and keyname notation
select('*').from_table('faculty')(where=lambda row: row['column'] == "law" and row.diff_column > 6)

select('*').from_table('faculty')(order_by='name')

select('*').from_table('faculty')(where=lambda row: row['column'], order_by='name')

# The where keyword will receive a callable in which to filter our query.
# i.e.
where=lambda row: row.average > 70

# The order_by keyword receives a SINGLE string naming the column to order_by.
# Order_by's default order is ascending, however if the string has desc at the end it
# it will then be descending. (You can write 'asc' for ascending).
# i.e. It can receive one of the following
order_by='name'
order_by='name desc'
order_by='name asc'

# The return from your query should be a list of dictionaries representing rows.
# Remember, unwanted columns should be filtered out!
# Also your DSL should have the same rules as SQL.
# As in:
#   You can filter by columns who will not be in your final result.
#   You can not order_by a column who is not a wanted column.

# After all is said and done, try to use generators and lambdas as much as possible, so
# that you iterate over the original table only once.

# The syntax can look as follows:

select('*') \
.from_table('rooms')()

# Or

select('name', 'average') \
.from_table('students')(
where=lambda r: r.average > 80 and \
                r.room_number == 'A14',
order_by='average')

class select(object):
    # The DataBase will be initialized externally
    db = None
    def __init__(self):
        pass

    def from_table(self, table):
        pass
