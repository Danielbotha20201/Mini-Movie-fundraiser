# chechs user has entered yes/no to a question
def yes_no(question):

  while True:
    response = input(question).lower()
    
    if response == "yes" or response == "y":
      return "yes"

    elif response == "no" or response == "n":
      return "no"

    else:
      print ("Please enter yes or no")
# checks if user response is not blank
def not_blank(question):
  
  while True:
    response = input (question)
    

    if response == "":
      print("Sorry this can't be blank. Please try again")
    else:
       return response

# checks users enter an integer to a given question
def num_check(question):

  while True:

    try:
      response = int(input(question))
      return response

    except ValueError:
      print("please enter an integer.")

# Calculate the ticket price based on the age
def calc_ticket_price(var_age):

  if var_age < 16:
    price = 7.5

  elif var_age < 65:
    price = 10.5

  else:
    price = 6.5

  return price



# set maximum number of tickets 
MAX_TICKETS = 3
tickets_sold = 0

#ask user if they want to see the instructions
want_instructions = yes_no("Do you want to read the instructions?")
  
if want_instructions == "yes":
   print("instructions go here")
  
print()

# loop to sell tickets

while tickets_sold < MAX_TICKETS:
  
  name = not_blank("Enter your name (or 'xxx' to quit) ")

  if name == 'xxx':
    break

  tickets_sold += 1
 
  age = num_check("Age: ") 
  if 12 <= age <= 120:
      pass
  elif age < 12:
      print("Sorry you are too young for this movie")
      continue
  else:
   print("??That looks like a typo, please try again")
   continue

  # calculate ticket cost
  ticket_cost = calc_ticket_price(age)
  print("age: {}, Ticket Price: ${:.2f}".format(age, ticket_cost))
 
if tickets_sold == MAX_TICKETS:
  print("Congratulations you have sold all the tickets")
else:
  print("you have sold {} ticket/s. There is {} ticket/s "
       "remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))