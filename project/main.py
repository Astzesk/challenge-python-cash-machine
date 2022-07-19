import os

import app.resources.init as Extend

class Program(Extend.Init):

    def __init__(self, lPrice = 0, lPayment = 0):
        super().__init_subclass__(lPrice, lPayment)

        self.state = 1

    def __del__(self) -> None:
        super().__del__()

    def confirm(self):
        step = input(self.printReport('request', 2))
        
        clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

        if step == "Yes":
            self.state = 0
            self.print('msg', 'program', 0)
        elif step == "No":
            clear()
        else:
            self.confirm()

    def run(self):

        while self.state == 1:

            try:
                price = float(input(self.printReport('request', 0)))
                payment = float(input(self.printReport('request', 1)))
                
                Program(
                    price,
                    payment
                ).pay()

            except ValueError:
                self.print('msg', 'invoice', 1)
                self.print('des', 'invoice', 6)
            except:
                self.error()
            finally:
                self.confirm()

def window():
    app = Program()
    app.run()

window()
