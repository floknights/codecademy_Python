uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def polynomial_hash(s):
  hash_value = 0
  
  for i in range(len(s)):
    hash_value = hash_value + ord(s[i]) * (26**(len(s)-i-1))
    
  return hash_value

polynomial_hash_values = dict()

for i in range(len(uppercase) - 3):
  substring = uppercase[i: i + 4]
  polynomial_hash_values[substring] = polynomial_hash(substring)

print(polynomial_hash_values)
