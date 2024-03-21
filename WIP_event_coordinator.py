guests = {}
def read_guestlist(file_name = "guest_list.txt"):
  text_file = open(file_name,'r')
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    yield name

#WIP BELOW - NOT WORKING
def add_guest(guest_data):
  name = guest_data[0]
  age = int(guest_data[1])
  guests.append[name] = age
  yield name

guestlist_generator = read_guestlist()

#for guest in list(guestlist_generator)[:10]:
#  print(guest)

for i in range(10):
  try:
    print(next(guestlist_generator))
  except StopIteration:
    print("No more guests")
    break

#WIP BELOW - NOT WORKING
new_guest = add_guest("Jane,35")
print((guestlist_generator.send(new_guest)))
print(next(guestlist_generator))

#WORKS FINE BELOW
#try:
#    while True:
#        guest = next(guestlist_generator)
#        print(guest)
#except StopIteration:
#    print("No more guests")
