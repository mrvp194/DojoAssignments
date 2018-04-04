class Product(object) :
    def __init__(self, price, name, weight, brand, status="for sale") :
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = status
        self.display()
    
    def sell(self) :
        self.status = "sold"
        return self

    def add_tax(self, tax) :
        self.price += self.price * tax
        return self

    def ret(self, reason) :
        if reason == "defective" :
            self.status = reason
            self.price = 0
        elif reason == "in box" :
            self.status = "for sale"
        elif reason == "opened" :
            self.status = "used"
            self.price -= self.price * .2
        return self
    
    def display(self) :
        print "The price is {}.  The name is {}.  The weight is {}.  The brand is {}.  The status is {}.".format(self.price, self.name, self.weight, self.brand, self.status)
        return self
    
p = Product(20, 'baseball', 5, 'rawlings')
p.add_tax(.1)
p.ret('opened')
p.display()