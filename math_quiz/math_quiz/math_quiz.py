import random

def random_number(min_value, max_value):
    """
    Generates a random number between min_value and max_value (inclusive).

    inputs:
        min_value (int): The minimum possible value for the random integer.
        max_value (int): The maximum possible value for the random integer.

    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def random_operator():
    """
    Generates a random arithmetic operator: '+', '-', or '*'.

    Returns:
        str: A randomly chosen arithmetic operator.
    """
    return random.choice(['+', '-', '*'])

def result(num1, num2, operator):
    """
    Calculates the result of an arithmetic operation.

    input:
        num1 (int): The first operand.
        num2 (int): The second operand.
        operator (str): The arithmetic operator ('+', '-', or '*').

    Returns:
        The arithmetic problem and its result.
    """
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    problem = f"{num1} {operator} {num2}"
    return problem, result

def math_quiz():
    score = 0
    number_of_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(number_of_questions):
        num1 = random_number(1, 10)
        num2 = random_number(1, 5)  # Changed to an integer
        operator = random_operator()

        problem, answer = result(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
       #Getting user inputs
        user_answer = int(input("Your answer: "))

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{number_of_questions}")

if __name__ == "__main":
    math_quiz()
