class Stock(object):
    """Represents stock holding."""
    def __init__(self, name, shares, price):
        self.name, self.shares, self.price = name, shares, price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
    
    def __str__(self):
        pass
    
    def __unicode__(self):
        pass

    def cost(self):
        return self.shares * self.price

    def sell(self, n):
        assert n <= self.shares
        self.shares -= n
