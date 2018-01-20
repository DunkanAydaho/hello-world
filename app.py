#PY Script
book = int(input("Enter number of books:"))
price = 50
total = book * price
#Check and reply
if book >= 5:
  print("Good choise, your total sum: ${}".format(total))
elif book < 5:
  print("Take more!")
else:
  print("What da fuk a u doin brah?")
#Need new function here
