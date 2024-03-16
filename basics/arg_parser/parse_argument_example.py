"""

Here we are writing a program that takes 3
inputs,
1) First Number
2) Second Number
3) Operation ("add","subtract","multiply")
It should return result of operation based on the inputs
"""

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help = "First number")
    parser.add_argument("number2", help="Second number")
    parser.add_argument("operation", help="operation")
    args = parser.parse_args()

    # print(args.number1, args.number2, args.operation)

    n1 = int(args.number1)
    n2 = int(args.number2)
    res  = None
    if(args.operation == "add"):
        res = n1+n2
    elif (args.operation == "subtract"):
        res = n1 - n2
    elif (args.operation == "multiply"):
        res = n1 * n2
    elif (args.operation == "divide"):
        res = n1 / n2

    print(res)