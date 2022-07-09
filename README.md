# Cash Machine Simulation
[![stars](https://img.shields.io/github/stars/astzesk/challenge-python-cash-machine)](https://github.com/astzesk/challenge-python-cash-machine/stargazers)
[![license](https://img.shields.io/github/license/astzesk/challenge-python-cash-machine)](https://github.com/astzesk/challenge-python-cash-machine/blob/master/LICENSE)
[![issues](https://img.shields.io/github/issues/astzesk/challenge-python-cash-machine)](https://github.com/astzesk/challenge-python-cash-machine/issues)
[![issues-pr](https://img.shields.io/github/issues-pr/astzesk/challenge-python-cash-machine)](https://github.com/astzesk/challenge-python-cash-machine/pulls)
[![milestones](https://img.shields.io/github/milestones/open/astzesk/challenge-python-cash-machine)](https://github.com/astzesk/challenge-python-cash-machine/milestones)

The cash machine simulation project consists of a simulation of the cash machine using the object-oriented python programming language that permits the calculation of the getting change and the number of banknotes and coins in euro. The program contains restrictions on the values of banknotes and coins on payment.

**Payment values permitted**

Euro Banknotes: `500, 200, 100, 50, 20, 10 and 5.`

Euro Coins: `2 and 1.`

Cents Coins: `0.50, 0.20, 0.10, 0.05 0.02 and 0.01.` 

## General Information

### Table of Content
All essential information about the project, you can be found here.

| Project    | Community |
|    :----   |    :----   |
| [Getting Started](#getting-started) | [Code of Conduct](https://github.com/astzesk/challenge-python-cash-machine/blob/master/CODE_OF_CONDUCT.md) |
| [Screenshots](#screenshots) | [Contributing](https://github.com/astzesk/challenge-python-cash-machine/blob/master/CONTRIBUTING.md)|
| [Technologies](#technologies) | [License](https://github.com/astzesk/challenge-python-cash-machine/blob/master/LICENSE) |
| [Features](#features) |[Security Policy](https://github.com/astzesk/challenge-python-cash-machine/blob/master/SECURITY.md) |
| [Author](#author) |[Discussions](https://github.com/astzesk/challenge-python-cash-machine/discussions) |

## Getting Started

### Requirements

It is essential to know the requirements of the program before being used.

#### Program Execution

If you want to run the program, see the requirements.

##### Recommended Requirements

- Operation System: Windows, Linux, and macOS or other OS compatible.
- Python Version: Python 3.9 or up.

#### Integrated Development Environment

If you want to modify the project code, see the requirements.

##### Recommended Requirements

- Operation System: Windows, Linux, and macOS or other OS compatible.
- Python Version: Python 3.9 or up.
- IDE: Visual Studio, and PyDev or other IDE compatible.

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

### Code Sample

This section contains examples of the descriptions of functionalities and constitutions of the application code.

#### Example 1 - Main Description

The current code of the constructor has two variables, and every variable contains an input method with a message. The first variable is the `price` used for the `lPrice` parameter of the `Program` constructor. The `payment` variable only accepts the **payment values permitted** located in the `Invoice` class if the `payment` variable has been into the `lPayment` parameter of the constructor. The `Program` constructor gets the arguments before running the `pay` method. The `pay` method is essential to execute all functionalities to obtain the getting change and the number of coins and banknotes.

**main.py file**
```python

try:
    price = float(input(self.printReport('request', 0)))
    payment = float(input(self.printReport('request', 1)))
    
    Program(
        price,
        payment
    ).pay()

except ValueError:
    self.print('msg', 'error', 1)
except:
    self.error()
finally:
    self.confirm()

```

The `money` variable specifies the **payment values permitted** for the `lPayment` parameter of the constructors such as `Program`; `Init`; `Bank` and `Invoice` class. It is possible to modify the restriction.

**invoice.py file**
```python

money = [
    [500, 200, 100],
    [50, 20, 10],
    [5, 2, 1],
    [0.50, 0.20, 0.10],
    [0.05, 0.02, 0.01]
]

```
For the least, if all top statements don't match the code, the program will return a message with an error explanation.

#### Example 2 - Default Constructor

The `lPrice` and the `lPayment` are parameters of the `Bank` and `Invoice` constructors. These two constructors have default parameters that mustn't require arguments for the parameters. The code represented can be inserted in the `run` method on the `Program` class inside the while loop. When running the code in the compiler will get the final result.

**main.py file**
```python

app = Extend

Program(
    float(price), 
    float(payment)
).pay()

```
Remember, it's essential to remove or reuse the current code of the application.

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
