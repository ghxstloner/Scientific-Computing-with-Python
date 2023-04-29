def arithmetic_arranger(problems, show_answers=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  first_line = ""
  second_line = ""
  dash_line = ""
  answer_line = ""

  for problem in problems:
    parts = problem.split()
    operand1 = parts[0]
    operator = parts[1]
    operand2 = parts[2]

    if not operand1.isnumeric() or not operand2.isnumeric():
      return "Error: Numbers must only contain digits."

    if len(operand1) > 4 or len(operand2) > 4:
      return "Error: Numbers cannot be more than four digits."

    if show_answers:
      if operator == "+":
        answer = str(int(operand1) + int(operand2))
      elif operator == "-":
        answer = str(int(operand1) - int(operand2))
      elif operator == '/':
        return "Error: Operator must be '+' or '-'."
      else:
        return "Error: Operator must be '+' or '-'."

    max_length = max(len(operand1), len(operand2))

    operand1 = operand1.rjust(max_length + 2)
    operand2 = operator + operand2.rjust(max_length + 1)

    if show_answers:
      answer = answer.rjust(max_length + 2)

    first_line += operand1 + "    "
    second_line += operand2 + "    "
    dash_line += "-" * (max_length + 2) + "    "
    if show_answers:
      answer_line += answer + "    "

  first_line = first_line.rstrip()
  second_line = second_line.rstrip()
  dash_line = dash_line.rstrip()
  if show_answers:
    answer_line = answer_line.rstrip()

  arranged_problems = first_line + "\n" + second_line + "\n" + dash_line
  if show_answers:
    arranged_problems += "\n" + answer_line

  return arranged_problems

