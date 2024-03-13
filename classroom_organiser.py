from classroom_roster import student_roster
import itertools

class ClassroomOrganiser:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)

  def _sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students

  def __iter__(self):
    self.index = 0
    return self

  def __next__(self):
    if self.index < len(self.sorted_names):
      name_index = self.sorted_names[self.index]
      self.index += 1
      return name_index
    else:
      raise StopIteration

  def table_combos(self):
    options = []
    table_combos = itertools.combinations(self.sorted_names, 2)
    for table in table_combos:
      options.append(table)
    return options
    
#testing sorted_names function
organiser = ClassroomOrganiser()
print(organiser.sorted_names)

#testing index function
for index in organiser:
  print(index)

#testing table_combos function
print(organiser.table_combos())
