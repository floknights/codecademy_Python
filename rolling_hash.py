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
prime_rolling_hash_values = {s:p}

for c in uppercase[4:]:
  p = prime_rolling_hash(s, p, c)
  s = s[1:] + c
  prime_rolling_hash_values[s] = p

print(prime_rolling_hash_values)
