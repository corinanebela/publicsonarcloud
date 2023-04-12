#By contract, every Python function returns something, even if it’s the None value, which can be returned implicitly by omitting the return statement, or explicitly.

#The __init__ method is required to return None. A TypeError will be raised if the __init__ method
#either yields or returns any expression other than None. Returning some expression that evaluates to None will not raise an error, but is considered bad practice.


class MyClass(object):
    def __init__(self):
        self.message = 'Hello'
        return self  # Noncompliant
