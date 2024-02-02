class Stock(object):
    """Represents stock holding."""
    __slots__ = ('name', '_shares', 'price')

    def __init__(self, name, shares, price):
        self.name, self.shares, self.price = name, shares, price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
    
    def __str__(self):
        return repr(self)
    
    def __unicode__(self):
        return str(self)

    @property
    def cost(self):
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('expected an integer')
        self._shares = value

    def sell(self, n):
        assert n <= self.shares
        self.shares -= n
