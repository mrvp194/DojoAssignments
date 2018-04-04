class Call(object) :
    def __init__(self, id, name, number, time, reason) :
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    
    def display(self) :
        print "id is {}. Name is {}. number is {}. time is {}. reason is {}".format(self.id, self.name, self.number, self.time, self.reason)

class CallCenter(object) :
    def __init__(self, calls, queue) :
        self.calls = calls
        self.queue = queue
    
    def add(self, call) :
        self.calls.append(call)
        self.queue += 1
    
    def remove(self, call) :
        self.calls.pop(0)
        self.queue -= 1

    def info(self) :
        for call in self.calls :
            call.display()
        print self.queue

a = []
for n in range(10) :
    a.append(Call(1, 'lucy', '3126361462', '10pm', 'hate!!!'))

j = CallCenter(a, len(a))
j.info()