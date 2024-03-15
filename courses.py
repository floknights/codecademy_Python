#generator expressions

def cs_generator():
  for i in range(1,5):
    yield "Computer Science " + str(i)
cs_courses = cs_generator()
for course in cs_courses:
  print(course)
cs_generator_exp = ("Computer Science {}".format(i) for i in range(1,5))
for course in cs_generator_exp:
  print(course)

#generator methods (send)

MAX_STUDENTS = 50
def get_student_ids():
  student_id = 1
  while student_id <= MAX_STUDENTS:
    n = yield student_id
    if n is not None:
      student_id = n
      continue
    student_id += 1
student_id_generator = get_student_ids()
for i in student_id_generator:
  if i == 1:
    i = student_id_generator.send(25)
  print(i)

#generator methods (throw)

def student_counter():
  for i in range(1,5001):
    yield i
student_generator = student_counter()
for student_id in student_generator:
  if student_id > 100:
    student_generator.throw(ValueError, "Invalid student ID")
  print(student_id)

#generator methods (close)

def student_counter():
  for i in range(1,5001):
    yield i
student_generator = student_counter()
for student_id in student_generator:
  print(student_id)
  if student_id == 100:
    student_generator.close()

#connected generators

def science_students(x):
  for i in range(1,x+1):
    yield i
def non_science_students(x,y):
  for i in range(x,y+1):
    yield i 
def combined_students():
  yield from science_students(5)
  yield from non_science_students(10, 15)
  yield from non_science_students(25, 30)
student_generator = combined_students()
for student in student_generator:
  print(student)

#nested generators

def course_generator():
    yield ("Computer Science", 5)
    yield ("Art", 10)
    yield ("Business", 15)
def add_five_students(courses):
  for course, num_students in courses:
    yield (course, num_students + 5)
increased_courses = add_five_students(course_generator())
for course in increased_courses:
  print(course)
