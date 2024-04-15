class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for i in range(self.array_size)]

  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]
    if current_array_value == None:
      self.array[array_index] = [key, value]
    elif key == current_array_value[0]:
      self.array[array_index] = value
    else:
      pass

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    return self.array[array_index]

hash_map = HashMap(20)

hash_map.assign("gneiss", "metamorphic")

print(hash_map.retrieve("gneiss"))
