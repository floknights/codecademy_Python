uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def polynomial_hash(s):
	hash_value = 0

	for i in range(len(s)):
		hash_value += (ord(s[i])*(26**(len(s) - i - 1)))

	return hash_value

polynomial_hash_ABCD = polynomial_hash('ABCD')
rolling_hash_BCDE = (polynomial_hash_ABCD - ord('A') * (26**3)) * 26 + ord('E')
polynomial_hash_BCDE = polynomial_hash('BCDE')

def polynomial_rolling_hash(s, H, c):
  return (H - ord(s[0]) * 26**(len(s) - 1)) * 26 + ord(c)

s = 'ABCD'
H = polynomial_hash(s)
polynomial_rolling_hash_values = {s:H} # initialize dictionary with first substring and its polynomial hash

for c in uppercase[4:]: # loop through next characters in line from 'E' to 'Z'
  H = polynomial_rolling_hash(s, H, c) # calculate polynomial rolling hash of next substring
  s = s[1:] + c # build the next substring by slicing through s and adding c
  polynomial_rolling_hash_values[s] = H # update the dictionary with the next substring and its prime hash
  
print(polynomial_rolling_hash_values)
