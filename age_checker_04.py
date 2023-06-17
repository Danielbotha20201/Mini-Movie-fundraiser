# checks users enter an integer to a given question
def num_check(question):

  while True:

    try:
      response = int(input(question))
      return response

    except ValueError:
      print("please enter an integer.")

tickets_sold = 0

while True:
  name = input("Enter your name / xxx to quit: ")
  
  if name == "xxx":
    break

  age = num_check("Age: ")
  
  if 12 <= age <= 120:
    pass
    
  elif age < 12:
    print("Sorry you are too young for this movie")
    continue

  elif age > 120:
    print("Sorry you are too young for this movie")
    continue
  
  tickets_sold += 1