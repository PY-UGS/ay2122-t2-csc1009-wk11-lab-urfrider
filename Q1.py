class Calculator:
    def adder(self, input1, input2):
        return input1 + input2

    def subtractor(self, input1, input2):
        return input1 - input2

    def multiplier(self, input1, input2):
        return input1 * input2

    def divider(self, input1, input2):
        return input1 / input2

    def clear(self):
        return 0
# create an object calculator
calculator = Calculator()

# loop until user wants to quit
while True:
    # get input from user to choose desired operation
    option = input("1) Addition 2) Subtraction 3) Multiplication 4) Division: ")
    if option in ('1', '2', '3', '4'):
        # perform addition
        if option == '1':
            x, y = map(int, input("input the value of x and y for addition:").split())
            result = calculator.adder(x, y)
            print("{0} + {1} = {2}".format(x, y, result))
        # perform subtraction
        if option == '2':
            x, y = map(int, input("input the value of x and y for subtraction:").split())
            result = calculator.subtractor(x, y)
            print("{0} - {1} = {2}".format(x, y, result))
        # perform multiplication
        if option == '3':
            x, y = map(int, input("input the value of x and y for multiplication:").split())
            result = calculator.multiplier(x, y)
            print("{0} * {1} = {2}".format(x, y, result))
        # perform division
        if option == '4':
            x, y = map(int, input("input the value of x and y for division:").split())
            result = calculator.divider(x, y)
            print("{0} / {1} = {2}".format(x, y, result))
        # ask if user wants to continue calculation
        option2 = input("Continue calculation? press any to continue or q to quit: ")
        # clear the calculator to 0
        calculator.clear()
        # break the loop
        if option2 == 'q':
            break
    # ask user to input option 1 to 4
    else:
        print("Please input 1, 2, 3 or 4!")