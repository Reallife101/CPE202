from stack_array import Stack


# You do not need to change this class
class PostfixFormatException(Exception):
    pass


def postfix_eval(input_str):
    """Evaluates a postfix expression"""
    # Psemdas

    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ^ or numbers
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""

    stack = Stack(30)  # Stack of size 30
    exponent_list = []
    operators = ["+", ">>", "<<", "-", "**", "*", "/"]  # Allowed operands
    running_exponents = False

    split_string = input_str.split()  # Split input string into usable chunks in a list

    for val in split_string:  # Run through every value in list in order
        if val != "**" and running_exponents:
            hold = exponent_list[0]
            for i in range(1, len(exponent_list)):
                hold = exponent_list[i] ** hold
            stack.push(hold)
            exponent_list.clear()
            running_exponents = False

        if val not in operators:  # If not a number or operator then its an invalid token
            try:
                stack.push(int(val))
            except:
                try:
                    stack.push(float(val))
                except:
                    raise PostfixFormatException("Invalid token")
        elif stack.size() < 2 and not running_exponents:  # Can't operate unless you got at least two operands
            raise PostfixFormatException("Insufficient operands")
        elif val == "+":
            stack.push(stack.pop() + stack.pop())
        elif val == ">>":
            pop1 = stack.pop()
            pop2 = stack.pop()

            try:
                stack.push(pop2 >> pop1)
            except:
                raise PostfixFormatException("Illegal bit shift operand")
        elif val == "<<":
            pop1 = stack.pop()
            pop2 = stack.pop()
            try:
                stack.push(pop2 << pop1)
            except:
                raise PostfixFormatException("Illegal bit shift operand")
        elif val == "**":
            if not running_exponents:
                exponent_list.append(stack.pop())
            exponent_list.append(stack.pop())
            running_exponents = True
        elif val == "*":
            stack.push(stack.pop() * stack.pop())
        elif val == "/":
            pop1 = stack.pop()
            pop2 = stack.pop()
            if pop1 == 0:
                raise ValueError
            stack.push(pop2 / pop1)
        elif val == "-":
            pop1 = stack.pop()
            pop2 = stack.pop()
            stack.push(pop2 - pop1)

    if running_exponents:
        hold = exponent_list[0]
        for i in range(1, len(exponent_list)):
            hold = exponent_list[i] ** hold
        stack.push(hold)

    if stack.size() > 1:
        raise PostfixFormatException("Too many operands")
    return stack.pop()


def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression """

    stack = Stack(30)  # Stack of size 30
    operators = ["(", ")", ">>", "<<", "**", "*", "/", "+", "-"]  # Allowed operands
    final_list = ""
    first_run = True

    split_string = input_str.split()  # Split input string into usable chunks in a list

    for val in split_string:  # Run through every value in list in order

        if val == "(":
            stack.push("(")
        elif val == ")":
            popping = True
            while popping:
                popped_value = stack.pop()
                if popped_value == "(":
                    popping = False
                else:
                    final_list += " " + popped_value
        elif val in operators:
            popping = True
            while popping:
                if stack.is_empty():
                    popping = False
                elif stack.peek() == "(":
                    popping = False
                elif (val == ">>" or val == "<<") and operators.index(stack.peek()) > 3:
                    popping = False
                elif val == "**" and operators.index(stack.peek()) > 3:
                    popping = False
                elif (val == "*" or val == "/") and operators.index(stack.peek()) > 6:
                    popping = False
                else:
                    final_list += " " + stack.pop()
            stack.push(val)
        else:
            if first_run:
                final_list += str(val)
                first_run = False
            else:
                final_list += " " + str(val)

    popping = True
    while popping:
        if stack.is_empty():
            popping = False
        else:
            final_list += " " + stack.pop()

    return final_list


def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    stack = Stack(30)  # Stack of size 30
    operators = ["(", ")", ">>", "<<", "**", "*", "/", "+", "-"]  # Allowed operands

    split_string = input_str.split()  # Split input string into usable chunks in a list
    split_string.reverse()

    for val in split_string:  # Run through every value in list in order

        if val in operators:
            repop = stack.pop() + " " + stack.pop() + " " + val
            stack.push(repop)
        else:
            stack.push(val)
    return stack.pop()
