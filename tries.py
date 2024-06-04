class Trie:

  def __init__(self):
    self.root = TrieNode()

  def add_string(self, word: str) -> None:
    nxt = self.root
    for i in word:
      nxt = nxt.add_char(i)
      nxt.freq += 1
    nxt.end_of_key = True

  def search_string(self, string: str) -> bool:
    nxt2 = self.root
    for i in string:
      if i not in nxt2.nodes:
        return False
      nxt2 = nxt2.nodes[i]
    return nxt2.end_of_key

  def count_prefix(self, prefix: str) -> int:
    nxt = self.root
    for i in prefix:
      if i not in nxt.nodes:
        return 0
      nxt = nxt.nodes[i]
    return nxt.freq

class TrieNode:

  def __init__(self):
    self.nodes = {}
    self.end_of_key = False
    self.freq = 0

  def add_char(self, c: chr):
    if c not in self.nodes:
      self.nodes[c] = TrieNode()
    return self.nodes[c]

trie = Trie()
 
words = ["AMBER", "ALICE", "AMPLE", "BALLOON", "BALL", "BLAST", "BAND", "DENSE", "DUTCH", "DECK", "DANCE", "DRAMA", "MESS", "MAVERICK", "MAVEN", "PHYSICS", "PHONE", "PHANTOM", "PASS", "PEAK", "PACK", "ZEST", "ZEAL", "ZAP", "ZIP", "ZIPPER"]

for word in words:
  trie.add_string(word)

more_words = ["APPLE", "AMPLIFIER", "AMPLE", "BALLOON", "BALL", "DART", "DUTCH", "DECK", "DRAM", "FLAG", "MOP", "MAVERICK", "MANSION", "PHYSICS", "PHONE", "PHANTOM", "PASS", "PECK", "PAIN", "ZAM", "ZEST", "ZAP", "ZIP", "ZEBRA"]

for word in more_words:
  if trie.search_string(word):
    print(word)

prefixes = ["A", "AM", "B", "BALL", "BA", "C", "CA" "DUTCH", "DECK", "GA", "J", "MA", "P", "PH", "PE", "Z", "ZIP"]

for prefix in prefixes:
  print(trie.count_prefix(prefix))
