#code by Geovane Fernandes
def arithmetic_arranger(problems, answers=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    for problem in problems:

        # Split the list into two numbers and an operator
        num1, op, num2 = problem.split()


        # Checking for errors
        if op not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if op == "+":
            # convertendo para inteiro e somando os valores das variáveis num1 e num2 
            result = str(int(num1) + int(num2))
        else:
            result = str(int(num1) - int(num2))

        # Determine the length of the longest number and add 2 to create the length of the line
        length = max(len(num1), len(num2)) + 2

        # Create the lines of the problem + spaces to align them
        first_line += str(num1).rjust(length) + "    "
        second_line += op + str(num2).rjust(length - 1) + "    "
        third_line += "-" * length + "    "
        fourth_line += str(result).rjust(length) + "    "

    # Checking if the user wants to display the answers
    if answers == True:
        arranged_problems = first_line.rstrip() + "\n"\
         + second_line.rstrip() + "\n" + third_line.rstrip() + "\n" + fourth_line.rstrip()
    else:
        arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + third_line.rstrip()

    return arranged_problems
