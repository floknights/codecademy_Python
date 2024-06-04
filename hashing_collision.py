uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

def prime_value(c):
  return prime_numbers[ord(c)-ord('A')]

prime_values = dict()

for c in uppercase:
  prime_values[c] = prime_value(c)

print(prime_values)

def prime_hash(s):
  hash_value = 1

  for c in s:
    hash_value *= prime_value(c)

  return hash_value

prime_hash_values = dict() 

for i in range(len(uppercase) - 3):
  substring = uppercase[i: i + 4]
  prime_hash_values[substring] = prime_hash(substring)

print(prime_hash_values)

string1 = 'AB'
string2 = 'BA'

colliding_hash_values = {string1: prime_hash(string1), string2: prime_hash(string2)}
print(colliding_hash_values)
