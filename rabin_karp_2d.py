def polynomial_hash(s):
	hash_value = 0

	for i in range(len(s)):
		hash_value += (ord(s[i])*(26**(len(s) - i - 1)))
    
	return hash_value

def polynomial_rolling_hash(previous_hash, c1, c2, pattern_length):
	return (previous_hash - ord(c1) * (26**(pattern_length - 1))) * 26 + ord(c2)

def rabin_karp_algorithm_2D(pattern, text):
  m1 = len(pattern) # number of rows of m2 characters in pattern
  m2 = len(pattern[0]) # number of columns of m1 characters in pattern
  n1 = len(text) # number of rows of n2 characters in text
  n2 = len(text[0]) # number of columns of n1 characters in text
  
  occurrences = 0
  pattern_hash = 0
  
  for i in range(m1):
    pattern_hash += polynomial_hash(pattern[i])*(10**(m1 - i - 1))

  all_hashes = [[0 for j in range(n2 - m2 + 1)] for i in range(n1)]

  for i in range(n1):
    substring_hash = polynomial_hash(text[i][:m2])
    all_hashes[i][0] = substring_hash

    for j in range(n2 - m2):
      previous_hash = substring_hash
      substring_hash = polynomial_rolling_hash(previous_hash, text[i][j], text[i][j + m2], m2)
      all_hashes[i][j + 1] = substring_hash 

  for j in range(n2 - m2 + 1):
    column_hash = 0
    for i in range(m1):
      column_hash += all_hashes[i][j]*(10**(m1 - i - 1))

    if (column_hash == pattern_hash):
      occurrences += 1

    for i in range(n1 - m1):
      previous_hash = column_hash
      column_hash = (previous_hash - all_hashes[i][j]*(10**(m1 - 1)))*10 + all_hashes[i + m1][j]

      if (column_hash == pattern_hash):
        occurrences += 1

  return occurrences

pattern = ['ABC', 'GHI']
text = ['ABCDEF', 'GHIJKL', 'MNOPQR', 'STUVWX', 'YZABCD', 'EFGHIJ', 'KLMNOP']

print(rabin_karp_algorithm_2D(pattern, text))
