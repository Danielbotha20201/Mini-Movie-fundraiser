def not_blank(question):
  
  while True:
    response = input (question)
    

    if response == "":
      print("Sorry this can't be blank. Please try again")
    else:
       return response
      

while True:
  name = not_blank("Enter your name (or 'xxx' to quit) ")
  if name == "XXX":
      break

print ("we are done")