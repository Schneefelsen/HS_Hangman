from collections import deque


class ExpressionError(Exception):
    def __str__(self):
        return "Invalid expression"


class CommandError(Exception):
    def __str__(self):
        return "Unknown Command"


class VariableError(Exception):
    def __str__(self):
        return "Unknown variable"


class VariableSyntaxError(Exception):
    def __str__(self):
        return "Invalid variable"


class AssignmentError(Exception):
    def __str__(self):
        return "Invalid assignment"


class Calculator:
    """
    A Class to represent an interactive basic arithmetics calculator
    capable of addition, subtraction, multiplication, integer division,
    exponentiation, the assignment of variables for more complex
    calculations and calculation with parenthesis.
    ...

    Attributes
    ----------
    variables : dict
        saved variables
    text : str
        user input
    text_list : list
        user input, split into a list for either assignment or calculation
    postfix : list
        calculation in postfix notation
    messages : dict
        possible command messages
    """

    def __init__(self):
        """
        Constructs all necessary attributes for the calculator object.
        """
        self.variables = {}
        self.text = ""
        self.text_list = []
        self.postfix = []
        self.messages = {"/help": "Write the desired calculation in the following format:\n"
                                  "<a> <operation> <b> <operation> <c>...\n"
                                  "For now the only possible calculations are '+' and '-'.\n"
                                  "The calculator will output the result "
                                  "and await for the next calculation",
                         "/exit": "Bye!"}
        self.precedents = {"-": 1, "+": 1, "*": 2, "/": 2, "^": 3}

    def read_input(self):
        """ Reads user input. """
        self.text = input()

    def isempty(self):
        """ Help method to check if text is empty. """
        return self.text == ""

    def iscommand(self):
        """
        Help method to check if text is a command

        Returns:
            Bool: Empty text indicator
        """
        return self.text[0] == "/"

    def exec_command(self):
        """
        Checks, if the user input is a possible command or not.

        Returns:
            True: Command is known
        """
        if self.text in self.messages.keys():
            print(self.messages[self.text])
            if self.text == "/exit":
                return True
        else:
            raise CommandError

    def isassignment(self):
        """
        Help method to check if user input is an assignment.

        Returns:
            Bool: Assignment indicator
        """
        return "=" in self.text

    def generate_assign_list(self):
        """ Splits user input into two parts for assignment. """
        self.text_list = self.text.replace(" ", "").split("=")

    def assign(self):
        """
        Generates a list representing an assignment, checks for assignment validity and
        saves the (variable: value) pair in the 'variables' dictionary.
        """
        self.generate_assign_list()
        if not self.text_list[0].isalpha():
            raise VariableSyntaxError
        elif (len(self.text_list) != 2 or
              not self.text_list[1].isnumeric() and
              not self.text_list[1].isalpha()):
            raise AssignmentError
        elif (self.text_list[1].isalpha() and
                self.text_list[1] not in self.variables.keys()):
            raise VariableError
        else:
            self.variables.update({self.text_list[0]: self.text_list[1]})

    def replace_variable(self):
        """
        Help method to replace known variables
        in the user input with their value by string splicing.
        """
        for key, var in self.variables.items():
            if key in self.text:
                var_index1 = self.text.index(key)
                var_index2 = self.text.index(key[-1])
                self.text = (self.text[: var_index1] +
                             str(var) +
                             self.text[var_index2 + 1:])

    def generate_calc_list(self):
        """
        Separates the user input into numbers and operators.

        Raises:
            VariableError
        """
        calc_text = self.text.replace(" ", "")
        is_numeric = False
        number_str = ""
        for num, letter in enumerate(calc_text):
            if letter.isnumeric():
                is_numeric = True
                number_str = number_str + letter
                if num == len(calc_text) - 1:
                    self.text_list.append(int(number_str))
            elif is_numeric:
                is_numeric = False
                self.text_list.append(int(number_str))
                number_str = ""
                self.text_list.append(letter)
            elif letter.isalpha():
                raise VariableError
            else:
                self.text_list.append(letter)

    def strip_dash_operators(self):
        """
        Help method to strip dash operators in text_list
        if they are repeated while upholding the switching of operators
        for even sequences of subtraction operators.
        """
        is_negative = -1
        new_list = []
        for num, elem in enumerate(self.text_list):
            if elem == "+" and self.text_list[num + 1] in set("-+"):
                continue
            elif elem == "-":
                if self.text_list[num + 1] == "-":
                    is_negative *= -1
                elif is_negative < 0:
                    new_list.append("-")
                else:
                    new_list.append("+")
            else:
                new_list.append(elem)
        self.text_list = new_list

    def generate_postfix(self):
        """
        Generates a postfix notation from the attribute text_list
        for easier calculation.

        Raises:
            ExpressionError
        """
        stack = deque()
        for elem in self.text_list:
            if str(elem).isnumeric():
                self.postfix.append(elem)
            elif elem in set("+-*/^"):
                if len(stack) == 0:
                    stack.appendleft(elem)
                elif stack[0] == "(":
                    stack.appendleft(elem)
                elif self.precedents[elem] > self.precedents[stack[0]]:
                    stack.appendleft(elem)
                elif self.precedents[elem] <= self.precedents[stack[0]]:
                    while len(stack) > 0:
                        if stack[0] == "(":
                            break
                        elif self.precedents[elem] <= self.precedents[stack[0]]:
                            self.postfix.append(stack.popleft())
                        else:
                            break
                    stack.appendleft(elem)
            elif elem == "(":
                stack.appendleft(elem)
            elif elem == ")":
                while stack[0] != "(":
                    self.postfix.append(stack.popleft())
                stack.popleft()
        while len(stack) != 0:
            if "(" in stack:
                raise ExpressionError
            else:
                self.postfix.append(stack.popleft())

    def calc(self):
        """
        Generates a postfix notation from the user input
        and calculates it, if possible.
        It can parse the basic arithmetic operators '+', '-', '*', '/',
        the power operator '^' and parenthesis '(', ')'.

        Raises:
            ExpressionError
        """
        self.replace_variable()
        self.generate_calc_list()
        self.strip_dash_operators()
        self.generate_postfix()
        stack = deque()
        for elem in self.postfix:
            if str(elem).isnumeric():
                stack.appendleft(elem)
            elif elem in set("+-*/^"):
                if len(stack) > 1:
                    num2 = stack.popleft()
                    num1 = stack.popleft()
                    if elem == "+":
                        stack.appendleft(num1 + num2)
                    elif elem == "-":
                        stack.appendleft(num1 - num2)
                    elif elem == "*":
                        stack.appendleft(num1 * num2)
                    elif elem == "/":
                        stack.appendleft(num1 // num2)
                    else:
                        stack.appendleft(num1 ** num2)
                elif elem == "-":
                    stack[0] = -1 * stack[0]
                else:
                    raise ExpressionError
            else:
                raise ExpressionError
        if len(stack) == 1:
            print(stack.popleft())
        else:
            raise ExpressionError

    def clear_lists(self):
        """ Help method for clearing the cage of a calculator object
        for further calculations. """
        self.text_list.clear()
        self.postfix.clear()

    def start(self):
        """
        Loops till exited via command '/exit', differentiates between
        commands, assignments and calculations and operates accordingly.
        """
        while True:
            try:
                self.clear_lists()
                self.read_input()
                if self.isempty():
                    continue
                elif self.iscommand():
                    if self.exec_command():
                        break
                    continue
                elif self.isassignment():
                    self.assign()
                    continue
                else:
                    self.calc()
            except ExpressionError as err:
                print(err)
            except CommandError as err:
                print(err)
            except VariableError as err:
                print(err)
            except VariableSyntaxError as err:
                print(err)
            except AssignmentError as err:
                print(err)
            except UnboundLocalError:
                print("Invalid expression")
            except IndexError:
                print("Invalid expression")


if __name__ == "__main__":
    cal = Calculator()
    cal.start()
