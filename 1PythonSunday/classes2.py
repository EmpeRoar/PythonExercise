class NumberHolder:
    def __init__(self, number):
        self.number = number

    def returnNumer(self):
        return self.number

var = NumberHolder(42)
print(var.returnNumer())