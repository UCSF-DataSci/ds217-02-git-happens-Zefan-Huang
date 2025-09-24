## Here is an alternative implementation using iteration instead of recursiongit
class MySecondClass:
    def __init__(self):
        self.result = []
    
    def sum_q2(self, n=1000):
        for i in range(n):
            if i % 3 == 0 or i % 5 == 0:
                self.result.append(i)

obj2 = MySecondClass()
obj2.sum_q2()
print( sum(obj2.result) )