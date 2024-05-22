from logic_gates import NAND_gate, NOT_gate, AND_gate, OR_gate, XOR_gate

# HALF ADDER
def half_adder(a, b):
  s = XOR_gate(a, b)
  c = AND_gate(a, b)
  return (s, c)

# TEST CASES
print("A: 0, B: 0 | Output: {0}".format(half_adder(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(half_adder(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(half_adder(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(half_adder(1, 1)))

# FULL ADDER
def full_adder(a, b, c):
  s = XOR_gate(XOR_gate(a, b), c)
  c_out = OR_gate(AND_gate(OR_gate(a, b), c), AND_gate(a, b))
  return (s, c_out)

# TEST CASES
print("A: 0, B: 0, C: 0 | Output: {0}".format(full_adder(0, 0, 0)))
print("A: 0, B: 0, C: 1 | Output: {0}".format(full_adder(0, 0, 1)))
print("A: 0, B: 1, C: 0 | Output: {0}".format(full_adder(0, 1, 0)))
print("A: 1, B: 0, C: 0 | Output: {0}".format(full_adder(1, 0, 0)))
print("A: 0, B: 1, C: 1 | Output: {0}".format(full_adder(0, 1, 1)))
print("A: 1, B: 1, C: 0 | Output: {0}".format(full_adder(1, 1, 0)))
print("A: 1, B: 1, C: 1 | Output: {0}".format(full_adder(1, 1, 1)))
print("A: 1, B: 0, C: 1 | Output: {0}".format(full_adder(1, 0, 1)))

# FULL ADDER 2 - using half adder
def full_adder2(a, b, c):
  s1, c1 = half_adder(a, b)
  s2, c2 = half_adder(c1, c)
  s = XOR_gate(s1, c)
  c_out = OR_gate(c1, AND_gate(s1, c))
  return (s, c_out)  

# TEST CASES
print("A: 0, B: 0, C: 0 | Output: {0}".format(full_adder2(0, 0, 0)))
print("A: 0, B: 0, C: 1 | Output: {0}".format(full_adder2(0, 0, 1)))
print("A: 0, B: 1, C: 0 | Output: {0}".format(full_adder2(0, 1, 0)))
print("A: 1, B: 0, C: 0 | Output: {0}".format(full_adder2(1, 0, 0)))
print("A: 0, B: 1, C: 1 | Output: {0}".format(full_adder2(0, 1, 1)))
print("A: 1, B: 1, C: 0 | Output: {0}".format(full_adder2(1, 1, 0)))
print("A: 1, B: 1, C: 1 | Output: {0}".format(full_adder2(1, 1, 1)))
print("A: 1, B: 0, C: 1 | Output: {0}".format(full_adder2(1, 0, 1)))


# ARITHMETIC LOGIC UNIT
def ALU(a, b, c, opcode):
  if opcode == 0:
    s, c = half_adder(a, b)
  if opcode == 1:
    s, c = full_adder(a, b, c)
  return (s, c)

# TEST CASES
print("A: 0, B: 0, C: 0 | Output: {0}".format(ALU(0, 0, 0, 0)))
print("A: 0, B: 0, C: 1 | Output: {0}".format(ALU(0, 0, 1, 0)))
print("A: 0, B: 1, C: 0 | Output: {0}".format(ALU(0, 1, 0, 0)))
print("A: 1, B: 0, C: 0 | Output: {0}".format(ALU(1, 0, 0, 0)))
print("A: 0, B: 1, C: 1 | Output: {0}".format(ALU(0, 1, 1, 0)))
print("A: 1, B: 1, C: 0 | Output: {0}".format(ALU(1, 1, 0, 0)))
print("A: 1, B: 1, C: 1 | Output: {0}".format(ALU(1, 1, 1, 0)))
print("A: 1, B: 0, C: 1 | Output: {0}".format(ALU(1, 0, 1, 0)))

print("A: 0, B: 0, C: 0 | Output: {0}".format(ALU(0, 0, 0, 1)))
print("A: 0, B: 0, C: 1 | Output: {0}".format(ALU(0, 0, 1, 1)))
print("A: 0, B: 1, C: 0 | Output: {0}".format(ALU(0, 1, 0, 1)))
print("A: 1, B: 0, C: 0 | Output: {0}".format(ALU(1, 0, 0, 1)))
print("A: 0, B: 1, C: 1 | Output: {0}".format(ALU(0, 1, 1, 1)))
print("A: 1, B: 1, C: 0 | Output: {0}".format(ALU(1, 1, 0, 1)))
print("A: 1, B: 1, C: 1 | Output: {0}".format(ALU(1, 1, 1, 1)))
print("A: 1, B: 0, C: 1 | Output: {0}".format(ALU(1, 0, 1, 1)))
