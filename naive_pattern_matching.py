def naive_pattern_matching(pattern, text):
  pattern_length = len(pattern)
  text_length = len(text)
  occurrences = 0

  for i in range(text_length - pattern_length + 1):
    pattern_match = True

    for j in range(pattern_length):
      if (pattern[j] != text[i + j]): 
        pattern_match = False
        break
    
    if (pattern_match):
      occurrences += 1

  return occurrences

pattern = 1000*'A'
text = 100000*'A'
print(naive_pattern_matching(pattern, text))
