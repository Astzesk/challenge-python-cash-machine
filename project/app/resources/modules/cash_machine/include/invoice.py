from sympy import simplify 

from .cover import *

class Invoice(Cover):

    moneyPermitted  = [
        [500, 200, 100],
        [50, 20, 10],
        [5, 2, 1],
        [0.50, 0.20, 0.10],
        [0.05, 0.02, 0.01]
    ]

    def __init__(self, lPrice = 0, lPayment = 0):
        self.price = lPrice
        self.payment = lPayment
        self.priceBool = simplify(self.price).is_negative
        self.paymentBool = simplify(self.payment).is_negative
        self.budget = lPayment - lPrice
        self.item = f'{self.budget:.2f}'.split('.')
        self.index = 0
        self.numeral = list()
        self.count = 0

    def __init_subclass__(cls, lPrice = 0, lPayment = 0):
        cls.price = lPrice
        cls.payment = lPayment
        cls.priceBool = simplify(cls.price).is_negative
        cls.paymentBool = simplify(cls.payment).is_negative
        cls.budget = lPayment - lPrice
        cls.item = f'{cls.budget:.2f}'.split('.')
        cls.index = 0
        cls.numeral = list()
        cls.count = 0

    def __del__(self) -> None:
        super().__del__()

    def __del__(cls) -> None:
        super().__del__()

    def pay(self):
        reList = self.swap()

        if self.payment >= self.price and self.price > 0 and self.payment in reList[0:15]:

            if self.paymentBool == False and self.priceBool == False:
                self.operator()
                self.show()
                self.print('msg', 'invoice', 0)
            else:
                self.print('msg', 'invoice', 1)
        else:
            self.print('msg', 'invoice', 1)

            if self.payment <= 0 or self.price <= 0:
                self.print('des', 'invoice', 3);
            elif self.payment <= self.price:
                self.print('des', 'invoice', 4);
            elif self.payment not in reList[0:15]:
                self.print('des', 'invoice', 5);
            else:
                pass
  
    def show(self):
        print("\nGet change :", f'{self.budget:.2f}')

        self.check()

        if float(self.budget) > 0:
            self.print('null', 'invoice', 2)
        else:
            pass

        for x in range(0, len(self.numeral)):

            for y in range(0, len(self.numeral[x])):
                self.count = self.count + 1

                if self.numeral[x][y] != 0:

                    if self.count >= 8 and self.count <= 9:
                        print(self.numeral[x][y], "Coin(s) of "+str(self.moneyPermitted[x][y])+" euro(s).")
                    elif self.count > 9:
                        print(self.numeral[x][y], "Coin(s) of "+str(f'{self.moneyPermitted[x][y]:.2f}')+" cent(s).")
                    else:
                        print(self.numeral[x][y], "Banknote(s) of "+str(self.moneyPermitted[x][y])+" euro(s).")
                else:
                    pass

    def check(self):
        if len(self.moneyPermitted) != len(self.numeral):
            b = len(self.moneyPermitted) - len(self.numeral)

            for x in range(b):
                self.numeral.insert(0, [0, 0, 0])
        else:
            pass

    def matrix(self):
        add, end, rem = 0, 0, 0

        if self.index > 5 and self.index < 10:
            end = abs(self.index - 5)
            add = 1
        elif self.index > 0 and self.index <= 5:
            end = self.index
        else:
            end, rem = 1, 1

        for x in range(1, end + 1, 1):
            a = x - (int(x / 2) * 2)
            b = int(x / 2)
            c = int(x / 5)
            d = a - c - rem
            e = b - c * 2

        return [int(c) + add, int(e), int(d)]

    def operator(self):

        def add(value):
            for x in range(len(self.item[value])):
                self.index = int(self.item[value][x])
                self.numeral.append(self.matrix())

        add(0)
        add(1)

    def swap(self):
        rewrite = list()

        for x in range(len(self.moneyPermitted)):

            for y in range(len(self.moneyPermitted[x])):
                rewrite.append(self.moneyPermitted[x][y])

        return rewrite
