#! /usr/bin/python3

def read_number(line, index):
  number = 0
  while index < len(line) and line[index].isdigit():
    number = number * 10 + int(line[index])
    index += 1
  if index < len(line) and line[index] == '.':
    index += 1
    decimal = 0.1
    while index < len(line) and line[index].isdigit():
      number += int(line[index]) * decimal
      decimal /= 10
      index += 1
  token = {'type': 'NUMBER', 'number': number}
  return token, index

def read_plus(line, index):
  token = {'type': 'PLUS'}
  return token, index + 1

def read_minus(line, index):
  token = {'type': 'MINUS'}
  return token, index + 1

def read_divid(line, index):
  token = {'type': 'DIVID'}
  return token, index + 1

def read_times(line, index):
  token = {'type': 'TIMES'}
  return token, index + 1

def read_rparenthesis(line, index):
  token = {'type': 'RPARENTHESIS'}
  return token, index + 1

def read_lparenthesis(line, index):
  token = {'type': 'LPARENTHESIS'}
  return token, index + 1

def tokenize(line):
  tokens = []
  index = 0
  while index < len(line):
    if line[index].isdigit():
      (token, index) = read_number(line, index)
    elif line[index] == '+':
      (token, index) = read_plus(line, index)
    elif line[index] == '-':
      (token, index) = read_minus(line, index)
    elif line[index] == '/':
      (token, index) = read_divid(line, index)
    elif line[index] == '*':
      (token, index) = read_times(line, index)
    elif line[index] == '(':
      (token, index) = read_lparenthesis(line, index)
    elif line[index] == ')':
      (token, index) = read_rparenthesis(line, index)
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  return tokens


def evaluate(tokens):
  for i in range(2):
      index = 1
      while index < len(tokens):
          if tokens[index]['type'] == 'NUMBER':
              if tokens[index - 1]['type'] == 'PLUS' and i == 1:
                  tokens[index - 2] = {'type': 'NUMBER', 'number': tokens[index-2]['number'] + tokens[index]['number']}
                  tokens[index-1:index+1] = []
                  index -= 1
              elif tokens[index - 1]['type'] == 'MINUS' and i == 1:
                  tokens[index - 2] = {'type': 'NUMBER', 'number': tokens[index-2]['number'] - tokens[index]['number']}
                  tokens[index-1:index+1] = []
                  index -= 1
              elif tokens[index - 1]['type'] == 'DIVID' and i == 0:
                  tokens[index - 2] = {'type': 'NUMBER', 'number': tokens[index-2]['number'] / tokens[index]['number']}
                  tokens[index-1:index+1] = []
                  index -= 1
              elif tokens[index - 1]['type'] == 'TIMES' and i == 0:
                  tokens[index - 2] = {'type': 'NUMBER', 'number': tokens[index-2]['number'] * tokens[index]['number']}
                  tokens[index-1:index+1] = []
                  index -= 1
              elif tokens[index - 1]['type'] == 'LPARENTHESIS':
              else:
                  index += 1
          else:
              index += 1
  return tokens[0]['number']


def test(line):
  tokens = tokenize(line)
  actual_answer = evaluate(tokens)
  expected_answer = eval(line)
  if abs(actual_answer - expected_answer) < 1e-8:
    print("PASS! (%s = %f)" % (line, expected_answer))
  else:
    print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
  print("==== Test started! ====")
#   test("1+2")
#   test("4*2")
#   test("5/3")
#   test("4-2")
  test("1.0+2.1-3")
#   test("3.0+4*2-1/5")
#   test("4+6/2+5*3-1+6/2")
  print("==== Test finished! ====\n")

run_test()

while True:
  print('> ', end="")
  line = input()
  tokens = tokenize(line)
  answer = evaluate(tokens)
  print("answer = %f\n" % answer)
