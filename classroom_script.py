from classroom_roster import student_roster
from classroom_organizer import ClassroomOrganizer
import itertools

#lists students by name for roll call
student_roster_iterator = iter(student_roster)
for student in student_roster:
  print(next(student_roster_iterator))

organizer = ClassroomOrganizer()

#lists possible combinations for each table of 2
print(organizer.table_combos())

#retrieves iterables for students with the favourite subject Math or Science, combines into one iterable
afterschool_list = itertools.chain(organizer.get_students_with_subject("Math"), organizer.get_students_with_subject("Science"))

#retrieves an iterable for possible combinations for each table of 4
afterschool_combos = itertools.combinations(afterschool_list, 4)

#prints a list of names for the afterschool club
for name in afterschool_list:
  print(name)

#lists possible combinations for each table of 4
for combo in afterschool_combos:
  print(combo)
