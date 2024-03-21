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



guestlist_generator = read_guestlist()

#for guest in list(guestlist_generator)[:10]:
#  print(guest)

for i in range(10):
  try:
    print(next(guestlist_generator))
  except StopIteration:
    print("No more guests")
    break

#for i in guestlist_generator:
#  if i == 11:
#    i = guestlist_generator.send(read_guestlist("Jane,35"))
#    print(i)

#print(next(guestlist_generator))
#print(next(guestlist_generator))
#print(next(guestlist_generator))
#print(next(guestlist_generator))
#print(next(guestlist_generator))

#BELOW CODE DOESN'T RETURN EXPECTED VALUE

new_guest = "Jane,35"
returned_value = guestlist_generator.send(new_guest)
print(returned_value)

#print(next(guestlist_generator))

#try:
#    while True:
#        guest = next(guestlist_generator)
#        print(guest)
#except StopIteration:
#    print("No more guests")
