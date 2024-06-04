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

prime_hash_ABCD = prime_hash('ABCD')
rolling_hash_BCDE = prime_hash_ABCD // prime_hash('A') * prime_hash('E')
prime_hash_BCDE = prime_hash('BCDE')

print(rolling_hash_BCDE)
print(prime_hash_BCDE)

def prime_rolling_hash(s, p, c):
  return p // prime_hash(s[0]) * prime_hash(c)

s = 'ABCD'
p = prime_hash(s)
prime_rolling_hash_values = {s:p} # initialize dictionary with first substring and its prime hash

for c in uppercase[4:]: # loop through next characters in line from 'E' to 'Z'
  p = prime_rolling_hash(s, p, c) # calculate prime rolling hash of next substring
  s = s[1:] + c # build the next substring by slicing through s and adding c
  prime_rolling_hash_values[s] = p #u pdate the dictionary with the next substring and its prime hash

print(prime_rolling_hash_values)
