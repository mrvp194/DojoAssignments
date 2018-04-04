class MathDojo(object) :
    def __init__(self) :
        self.result = 0
    
    def add(self, first, *second) :
        total = 0
        total2 = 0
        if type(first) == list or type(first) == tuple :
           for n in first :
               total2 += n
        else :
            total2 += first 
        if len(second) == 0 :
            self.result += first
        else :
            for n in second :
                if type(n) == list or type(first) == tuple :
                    for j in n :
                        total += j
                else :
                    total += n
            self.result += total2 + total
        return self
    
    def subtract(self, first, *second) :
        total = 0
        total2 = 0
        if type(first) == list or type(first) == tuple :
           for n in first :
               total2 += n
        else :
            total2 += first 
        if len(second) == 0 :
            self.result -= first
        else :
            for n in second :
                if type(n) == list or type(first) == tuple :
                    for j in n :
                        total += j
                else :
                    total += n
            self.result -= total2 + total
        return self

md = MathDojo()
s = MathDojo()
print md.add(2).add(2,5).subtract(3,2).result
print s.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result