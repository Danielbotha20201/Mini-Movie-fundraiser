# Calculate the ticket price based on the age
def calc_ticket_price(var_age):

  if var_age < 16:
    price = 7.5

  elif var_age < 65:
    price = 10.5

  else:
    price = 6.5

  return price

# loop for testing
while True:

  age = int(input("Age: "))

#calculate ticket cost
  ticket_cost = calc_ticket_price(age)
  print("age: {}, Ticket Price: ${:.2f}".format(age, ticket_cost))