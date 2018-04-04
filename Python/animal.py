class Animal(object) :
    def __init__(self, name, health) :
        self.name = name
        self.health = health
    
    def walk(self) :
        self.health -= 1
        return self
    
    def run(self) :
        self.health -= 5
        return self

    def display(self) :
        print self.health
        return self
a = Animal('george', 100)
a.walk().walk().walk().run().run().display()

class Dog(Animal) :
    def __init__(self, name, health=150) :
        super(Dog, self).__init__(name, health)

    def pet(self) :
        self.health += 5
        return self
    
d = Dog('jay')
d.walk().walk().walk().run().run().pet().display()

class Dragon(Animal) :
    def __init__(self, name, health=170) :
        super(Dragon, self).__init__(name, health)
    
    def fly(self) :
        self.health -= 10
        return self
    
    def display(self) :
        super(Dragon, self).display()
        print "I'm a Dragon."
        return self

g = Animal('fay', 100)
# g.pet()
# g.fly()
g.display()
r = Dragon('smoke')
r.fly()
r.display()