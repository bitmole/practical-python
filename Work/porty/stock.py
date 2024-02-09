from .typedproperty import String, Integer, Float

class Stock(object):
    """Represents stock holding."""
    __slots__ = ('_name', '_shares', '_price')
    name = String('name')
    shares = Integer('shares')
    price = Float('price')


    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
    
    def __str__(self):
        return repr(self)
    
    def __unicode__(self):
        return str(self)

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, n):
        assert n <= self.shares
        self.shares -= n
        return self
