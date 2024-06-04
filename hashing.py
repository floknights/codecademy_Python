uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ascii_values = dict()

for c in uppercase:
  ascii_values[c] = ord(c)
  
print(ascii_values)

def ascii_hash(s):
  hash_value = 1
  
  for c in s:
    hash_value = hash_value * ord(c)
    
  return hash_value

ascii_hash_values = dict()

for i in range(len(uppercase) - 3):
  hash_value = 1
  substring = uppercase[i: i + 4]
  ascii_hash_values[substring] = ascii_hash(substring)

print(ascii_hash_values)

string1 = 'AT'
string2 = 'NF'

colliding_hash_values = {string1: ascii_hash(string1), string2: ascii_hash(string2)}
print(colliding_hash_values)
