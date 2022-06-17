import os

import data.bank as Extend

class Program(Extend.Bank):

    def __init__(self, lPrice = 0, lPayment = 0):
        super().__init_subclass__(lPrice, lPayment)

        self.state = 1

    def __del__(self) -> None:
        super().__del__()

    def confirm(self):
        step = input(self.message.reportDict['request'][2])
        
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
                price = input(self.message.reportDict['request'][0])
                payment = input(self.message.reportDict['request'][1])

                Program(
                    float(price), 
                    float(payment)
                ).pay()

            except ValueError:
                self.print('msg', 'error', 1)
            except:
                self.error()
            finally:
                self.confirm()

def main():
    app = Program()
    app.run()

main()
