def arithmetic_arranger(problems, show_answers=False):
  # Check that the list is not too long
  if len(problems) > 5:
    return "Error: Too many problems."

  # Initialize variables for the problem parts
  first_line = ""
  second_line = ""
  dash_line = ""
  answer_line = ""

  # Iterate over each problem
  for problem in problems:
    # Split the problem into operands and operator
    parts = problem.split()
    operand1 = parts[0]
    operator = parts[1]
    operand2 = parts[2]

    # Check that the operands are numeric
    if not operand1.isnumeric() or not operand2.isnumeric():
      return "Error: Numbers must only contain digits."

    # Check that the operands are not too long
    if len(operand1) > 4 or len(operand2) > 4:
      return "Error: Numbers cannot be more than four digits."

    # Calculate the answer
    if show_answers:
      if operator == "+":
        answer = str(int(operand1) + int(operand2))
      elif operator == "-":
        answer = str(int(operand1) - int(operand2))
      elif operator == '/':
        return "Error: Operator must be '+' or '-'."
      else:
        return "Error: Operator must be '+' or '-'."

    # Determine the length of the longest operand
    max_length = max(len(operand1), len(operand2))

    # Add padding to the operands so they are the same length
    operand1 = operand1.rjust(max_length + 2)
    operand2 = operator + operand2.rjust(max_length + 1)

    # Add padding to the answer so it lines up with the operands
    if show_answers:
      answer = answer.rjust(max_length + 2)

    # Add the parts of the problem to the appropriate line
    first_line += operand1 + "    "
    second_line += operand2 + "    "
    dash_line += "-" * (max_length + 2) + "    "
    if show_answers:
      answer_line += answer + "    "

  # Remove trailing whitespace from each line
  first_line = first_line.rstrip()
  second_line = second_line.rstrip()
  dash_line = dash_line.rstrip()
  if show_answers:
    answer_line = answer_line.rstrip()

  # Combine the lines into a single string
  arranged_problems = first_line + "\n" + second_line + "\n" + dash_line
  if show_answers:
    arranged_problems += "\n" + answer_line

  return arranged_problems


print(arithmetic_arranger(["32 / 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))