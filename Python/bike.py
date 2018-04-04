class Bike(object) :
    def __init__(self, price, max_speed, miles=0) :
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self) :
        print "This bike costs: {}.  It's max speed is {}.  It's total miles is {}.".format(self.price, self.max_speed, self.miles)
    
    def ride(self) :
        print "Riding..."
        self.miles += 10
        return self
    
    def reverse(self) :
        print "Reversing..."
        if self.miles >= 5 :
            self.miles -= 5
        else :
            self.miles -= self.miles
            print "Could only reverse {} miles".format(self.miles)
        return self

bike1 = Bike(200, "25mph")
bike2 = Bike(300, "35mph")
bike3 = Bike(400, "45mph")
bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()