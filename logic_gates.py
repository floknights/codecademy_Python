# NAND GATE - returns current if at least one of the inputs is off
def NAND_gate(a, b):
  if a:
    if b:
      return 0
  return 1

# TEST CASES
print("A: 0, B: 0 | Output: {0}".format(NAND_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(NAND_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(NAND_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(NAND_gate(1, 1)))


# NOT GATE - returns current if the input is off
def NOT_gate(a):
  if a:
    return 0
  else:
    return 1

# TEST CASES
print("A: 0 | Output: {0}".format(NOT_gate(0)))
print("A: 1 | Output: {0}".format(NOT_gate(1)))


# AND GATE - returns current if both of the inputs are on
def AND_gate(a, b):
  if a:
    if b:
      return 1
  return 0

# TEST CASES
print("A: 0, B: 0 | Output: {0}".format(AND_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(AND_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(AND_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(AND_gate(1, 1)))


# OR GATE - returns current if either of the inputs are on
def OR_gate(a, b):
  return NAND_gate(NAND_gate(a, a), NAND_gate(b, b))

# TEST CASES
print("A: 0, B: 0 | Output: {0}".format(OR_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(OR_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(OR_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(OR_gate(1, 1)))


# XOR GATE - returns current if only one of the inputs is on
def XOR_gate(a, b):
  return AND_gate(NAND_gate(a, b), OR_gate(a, b))

# TEST CASES
print("A: 0, B: 0 | Output: {0}".format(XOR_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(XOR_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(XOR_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(XOR_gate(1, 1)))


# NOR GATE - returns current if neither of the inputs is on
def NOR_gate(a, b):
  if(a == 0) and (b == 0):
        return 1
    elif(a == 0) and (b == 1):
        return 0
    elif(a == 1) and (b == 0):
        return 0
    elif(a == 1) and (b == 1):
        return 0

# TEST CASES
print("A: 0, B: 0 | Output: {0}".format(NOR_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(NOR_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(NOR_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(NOR_gate(1, 1)))
