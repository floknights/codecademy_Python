def polynomial_hash(s):
	hash_value = 0

	for i in range(len(s)):
		hash_value += (ord(s[i])*(26**(len(s) - i - 1)))
    
	return hash_value

def polynomial_rolling_hash(previous_hash, c1, c2, pattern_length):
	return (previous_hash - ord(c1) * (26**(pattern_length - 1))) * 26 + ord(c2)

def rabin_karp_algorithm_multiple(patterns, text):
  pattern_hashes = dict()
  occurrences = dict()
  pattern_lengths = set()

  for pattern in patterns:
    pattern_hashes[polynomial_hash(pattern)] = pattern
    occurrences[pattern] = 0
    pattern_lengths.add(len(pattern))
  
  for pattern_length in pattern_lengths:
    substring_hash = polynomial_hash(text[:pattern_length])

    if substring_hash in pattern_hashes:
      pattern = pattern_hashes.get(substring_hash)
      occurrences[pattern] += 1

    for i in range(len(text) - pattern_length):
      previous_hash = substring_hash
      substring_hash = polynomial_rolling_hash(previous_hash, text[i], text[i + pattern_length], pattern_length)

      if substring_hash in pattern_hashes:
        pattern = pattern_hashes.get(substring_hash)
        occurrences[pattern] += 1
        
    return occurrences

patterns = ['ABC', 'BCD', 'CDE', 'DEF']
text = 'ABCBCDCDEDEF'

print(rabin_karp_algorithm_multiple(patterns, text))
