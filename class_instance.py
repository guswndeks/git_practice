#1번
class Calculator1:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


cal = Calculator1()
cal.add(5)
cal.add(10)
print(cal.value)

#2번
class Calculator2:

    def __init__(self, init_value):
        self.value = init_value

    def add(self, val):
        self.value += val

cal = Calculator2(10)
cal.add(5)
cal.add(10)
print(cal.value)

#3번
class Calculator3:

    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgeradeCalculator3(Calculator3):

    def minus(self, val):
        self.value -= val

cal = UpgeradeCalculator3()
cal.add(10)
cal.minus(7)
print(cal.value)

#4번
class Calculator4:

    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator4(Calculator4):

    def add (self, val):
        if self.value + val > 100:
            self.value = 100
        else:
            self.value += val

cal = MaxLimitCalculator4()
cal.add(50)
cal.add(60)
print(cal.value)

#5번
class Calculator5:
    def __init__(self, init_value=0):
        self.value = init_value

    def add(self, val):
        self.value += val
    
    def sum(self):
        return sum(self.value)
    
    def avg(self):
        return sum(self.value) / len(self.value)

cal1 = Calculator5([1, 2, 3, 4, 5])
print(cal1.sum())
print(cal1.avg())
cal2 = Calculator5([6, 7, 8, 9, 10])
print(cal2.sum())
print(cal2.avg())