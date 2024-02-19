import random

name = "Flo"
question = "Will it be sunny tomorrow?"
answer = ""
random_number = random.randint(1, 9)

#This will generate a random number
#print(random_number)

#This will determine an answer
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
 answer = "Error"

#This will change the format, if no name is input
if name == "":
  print("Question: ", question)
else:
  print(name, " asks: ", question)

#This will return a message, if no question is input
if question == "":
  print("You need to ask a question.")

#This will return the answer
else:
  print("Magic 8-Ball's answer: ", answer)
