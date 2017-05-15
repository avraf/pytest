# Part A: Create a class Dessert with attributes name, calories, is_healthy, and
# is_delicious. `is_healthy` returns true if a dessert has less than 200 calories, and
# is_delicious returns true for all desserts.

# The attributes calories and name can be changed after instansiation.
# So if calories is changed to more or less than 200 the is_healthy attribute should
# return a new value.
# As in:
    # apple = Dessert('apple', 5)
    # apple.is_healthy # => True
    
    # apple.name = 'candied apple'
    # apple.calories = 312
    # apple.is_healthy # => False

# is healthy can not be called as a method.
# This is illegal:
    # apple.is_healthy()

# Here is the framework:

class Dessert(object):
    def __init__(self, name, calories):
        pass

# Note: You may define additional helper methods.
# Hint Descriptor protocol or magic getters

# Part B: Create a class JellyBean that extends Dessert, and add an attribute flavor.
# Modify is_delicious to return false if the flavor is "black licorice" (but
# is_delicious should still return true for all other flavors and for all non-JellyBean
# desserts).

# The JellyBean class should look like this:

class JellyBean(Dessert):
    def __init__(self, name, calories, flavor):
       pass

# Note: As before, you may define additional helper methods.
