from .modules.cash_machine.include.bank import *

class Init(Bank):

    def __init_subclass__(cls, lPrice = 0, lPayment = 0):
        super().__init_subclass__(lPrice, lPayment)

    def __del__(self) -> None:
        super().__del__()