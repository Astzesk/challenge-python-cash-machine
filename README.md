# Cash Machine Simulation
[![stars](https://img.shields.io/github/stars/astzesk/challenge-python-cash-machine)](https://github.com/astzesk/challenge-python-cash-machine/stargazers)
[![license](https://img.shields.io/github/license/astzesk/challenge-python-cash-machine)](https://github.com/astzesk/challenge-python-cash-machine/blob/master/LICENSE)
[![issues](https://img.shields.io/github/issues/astzesk/challenge-python-cash-machine)](https://github.com/astzesk/challenge-python-cash-machine/issues)
[![issues-pr](https://img.shields.io/github/issues-pr/astzesk/challenge-python-cash-machine)](https://github.com/astzesk/challenge-python-cash-machine/pulls)
[![milestones](https://img.shields.io/github/milestones/open/astzesk/challenge-python-cash-machine)](https://github.com/astzesk/challenge-python-cash-machine/milestones)

The cash machine simulation project consists of a simulation of the cash machine using the object-oriented python programming language that permits the operation of getting change and the number of banknotes and coins in euro. The program contains restrictions on the values of banknotes and coins on payment.

**Payment values permitted**

Euro Banknotes: `500, 200, 100, 50, 20, 10 and 5.`

Euro Coins: `2 and 1.`

Cents Coins: `0.50, 0.20, 0.10, 0.05 0.02 and 0.01.` 

## General Information

### Table of Content
All essential information about the project, see the table.

| Project    | Community |
|    :----   |    :----   |
| [Getting Started](#getting-started) | [Readme](https://github.com/astzesk/challenge-python-cash-machine/blob/master/README.md) |
| [Code Sample](#code-sample) | [Code of Conduct](https://github.com/astzesk/challenge-python-cash-machine/blob/master/CODE_OF_CONDUCT.md) |
| [Screenshots](#screenshots) | [Security Policy](https://github.com/astzesk/challenge-python-cash-machine/blob/master/SECURITY.md)|
| [Technologies](#technologies) | [Contributing](https://github.com/astzesk/challenge-python-cash-machine/blob/master/CONTRIBUTING.md) |
| [Features](#features) | [Discussions](https://github.com/astzesk/challenge-python-cash-machine/discussions) |
| [Author](#author) | [License](https://github.com/astzesk/challenge-python-cash-machine/blob/master/LICENSE) |

### Table of Phases
All essential information about the phases project, see the table.

| Phase    | Discussions | Code Sample | Branch |
|   :----:   |    :----   |    :----   |    :----   |
|     1     | [Phase I - Script Development](https://github.com/Astzesk/challenge-python-cash-machine/discussions/12) | [Phase I - Script Development](#phase-i---script-development) | [master-phase-one](https://github.com/Astzesk/challenge-python-cash-machine/tree/master-phase-one) |

## Getting Started

### Requirements

It is essential to know the requirements of the program before being used.

#### Program Execution

If you want to run the program, see the requirements.

##### Recommended Requirements

- Operation System: Windows, Linux, and macOS or other OS compatible.
- Python Version: Python 3.9.7 or up.

#### Integrated Development Environment

If you want to modify the project code, see the requirements.

##### Recommended Requirements

- Operation System: Windows, Linux, and macOS or other OS compatible.
- Python Version: Python 3.9.7 or up.
- IDE: Visual Studio, and PyDev or other [IDE](https://www.freecodecamp.org/news/what-is-an-ide-in-programming-an-ide-definition-for-developers) compatible.

### Installation

Install it locally on your machine.

#### For Windows, Linux, and macOS

Open the command line or terminal and follow all instructions.

##### 1. Create a project directory.

```
mkdir app
```

##### 2. Set the path of the current directory.

```
cd app
```

##### 3. Clone the repository into a project directory.

```
git clone https://github.com/astzesk/challenge-python-cash-machine.git
```

##### 4. Go to the current directory.

```
cd challenge-python-cash-machine\project
```

##### 5. To run the project using the command line, terminal, or use [IDE](https://www.freecodecamp.org/news/what-is-an-ide-in-programming-an-ide-definition-for-developers).

```
py main.py
```

## Code Sample

This section contains examples of the descriptions of functionalities and constitutions of the application code.

### **Phase I - Script Development**

This subsection contains code examples and descriptions and many more about phase one.

#### Example 1 - Main Description

The current code of the constructor has two variables, and every variable contains an input method with a message. The first variable is the `price` used for the `lPrice` parameter of the `Program` constructor. The `payment` variable only accepts the **payment values permitted** located in the `Invoice` class if the `payment` arguments has been into the `lPayment` parameter of the constructor. The `Program` constructor gets the arguments before running the `pay` method. The `pay` method is essential to execute all functionalities to obtain the getting change and the number of coins and banknotes.

Name File: [**main.py**](https://github.com/Astzesk/challenge-python-cash-machine/blob/master-phase-one/project/main.py)

```python

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

```

The `money` variable specifies the **payment values permitted** for the `lPayment` parameter of the constructors such as `Program`; `Init`; `Bank` and `Invoice` class. It is possible to modify the restriction.

Name File: [**invoice.py**](https://github.com/Astzesk/challenge-python-cash-machine/blob/master-phase-one/project/app/resources/modules/cash_machine/include/invoice.py)

```python

moneyPermited = [
    [500, 200, 100],
    [50, 20, 10],
    [5, 2, 1],
    [0.50, 0.20, 0.10],
    [0.05, 0.02, 0.01]
]

```
For the least, if all top statements don't match the code, the program will return a message with an error explanation.

#### Example 2 - Default Constructor

The `lPrice` and the `lPayment` are parameters of the `Program`; `Init`; `Bank` and `Invoice` constructor. These constructors have default parameters that mustn't require arguments for the parameters. The code represented can be inserted in the `run` method on the `Program` class inside the while loop.

Name File: [**main.py**](https://github.com/Astzesk/challenge-python-cash-machine/blob/master-phase-one/project/main.py)

**2.1.** Show getting change and the number of coins and banknotes provided by the price and payment variables from the input method.

```python

#Set price value to 7.25
price = float(input(self.printReport('request', 0)))

#Set payment value to 20
payment = float(input(self.printReport('request', 1)))

app = Extend

app.Init(price, payment).pay()

```

The final result when compiled the code:

```txt

Insert a price value: 7.25
Insert a payment value: 20

Get change : 12.75

Coin(s) and banknote(s) received:

1 Banknote(s) of 10 euro(s).
1 Coin(s) of 2 euro(s).
1 Coin(s) of 0.50 cent(s).
1 Coin(s) of 0.20 cent(s).
1 Coin(s) of 0.05 cent(s).

Message: Payment has been successfully!

```

**2.2.** Show the getting change and the number of coins and banknotes provided by the non-default arguments of the constructor without the usability of the price and payment variable.

```python

app = Extend

app.Bank(5, 10).pay()

```

The final result when compiled the code:

```txt

Get change : 5.00

Coin(s) and banknote(s) received:

1 Banknote(s) of 5 euro(s).

Message: Payment has been successfully!

```

**2.3.** Show the getting change and the number of coins and banknotes provided by the default arguments of the constructor without the usability of the price and payment variable.

```python

app = Extend

app.Invoice().pay()

```

The final result when compiled the code:

```txt

Message: Payment has been unsuccessfully!

Description: It should insert the payment and price value higher than zero before paying.

```

#### Example 3 - Cover Class

The `Cover` class is responsible for storing and printing some program messages contained in the `message.py` file. It's possible to add, remove and edit the data in the tagDict and reportDict variables and reuse it in other classes. But, it's essential knowing your usability before using it. Have several code examples about your utilization in the application. See it.

Name File: [**main.py**](https://github.com/Astzesk/challenge-python-cash-machine/blob/master-phase-one/project/main.py)

**3.1.** Show the message with **msg** `tagDict`, **program** `reportDict` and `index` of **1**.

```python

app = Extend

app.Cover("msg", "program", 1).show()

```

The final result when compiled the code:

```txt

Message: Try another option!

```

**3.2.** Show the message with **null** `tagDict`, **request** `reportDict` and `index` of **2**.

```python

app = Extend

app.Cover("null", "request", 2).show()

```

The final result when compiled the code:

```txt

Do you want close program (Yes or No)?

```

**3.3.** Show the message with **null** `tagDict`, **null** `reportDict` and `index` of **0** provided by the default arguments of the constructor.

```python

app = Extend

app.Cover().show()

```
The final result when compiling the code is the empty string.

It's essential to remove or reuse the current code.

## Screenshots
| Phase 1    |
|    :----:   |
| [![screenshots-1](https://github.com/Astzesk/challenge-python-cash-machine/blob/master/project/app/assets/screenshots/screenshot_1.png "screenshot-1")](#screenshots) |

## Technologies
* Programming Languages: `python`.
* Libraries: `os`, `sys` and `sympy`.

## Features 
* Option to get the value of change.
* Functionality to get the number of coins and banknotes of the getting change.
* Restriction of Banknotes and coins values on the payment.

## Author
Ryan Pontes
