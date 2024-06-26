tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

def linear_search(search_list, target_value):
  matches = []
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      matches.append(idx)
  if len(matches) > 0:
    return matches
  else:
    raise ValueError("{0} not in list".format(target_value))

tour_stops = linear_search(tour_locations, target_city)
print(tour_stops)
