class PoemFiles:
  def __init__(self, poem_file, mode):
    print('Starting up a poem context manager')
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print('Opening poem file')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

  def __exit__(self, *exc):
    print('Closing poem file')
    self.opened_poem_file.close()

with PoemFiles('poem.txt', 'w') as open_poem_file:
  open_poem_file.write("Hope is the thing with feathers")


from contextlib import contextmanager

@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = open(file, mode)
  
  try:
    yield open_poem_file
    
  finally:
    print('Closing File')
    open_poem_file.close()

with poem_files('poem.txt', 'a') as opened_file:
 print('Inside yield')
 opened_file.write('Rose is beautiful, Just like you.')


from contextlib import contextmanager
 
@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = open(file, mode)
  
  try:
    yield open_poem_file
  
  except AttributeError as e:
    print(e)

  finally:
    print('Closing File')
    open_poem_file.close()

with poem_files('poem.txt', 'a') as opened_file:
 print('Inside yield')
 opened_file.sign('Buzz is big city. big city is buzz.')


from contextlib import contextmanager
 
@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = open(file, mode)
  
  try:
    yield open_poem_file
    
  finally:
    print('Closing File')
    open_poem_file.close()


@contextmanager
def card_files(file, mode):
  print('Opening File')
  open_card_file = open(file, mode)
  
  try:
    yield open_card_file
    
  finally:
    print('Closing File')
    open_card_file.close()
 
with poem_files('poem.txt', 'r') as poem:
  with card_files('card.txt', 'w') as card:
    print(poem, card)
    card.write(poem.read())
