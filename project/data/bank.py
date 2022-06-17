import data.invoice as Extend

class Bank(Extend.Invoice):

    def __init__(self, lPrice = 0, lPayment = 0):
        super().__init_subclass__(lPrice, lPayment)

    def __del__(self) -> None:
        super().__del__()
