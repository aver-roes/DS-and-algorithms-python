''' Write a Python program that can “make change.” Your program should take two numbers as input,
 one that is a monetary amount charged and the other that is a monetary amount given.
 It should then return the number of each kind of bill and coin to give back as change for the difference between the amount given and the amount charged.
  The values assigned to the bills and coins can be based on the monetary system of any current or former government.
 Try to design your program so that it returns as few bills and coins as possible.'''




amount_payed = int(input("Pay: "))
AMOUNT_CHARGED = 300

def change(AMOUNT_CHARGED, amount_payed):
  money_type=(100,50,20,10,5,1,0.5,0.1)

  if AMOUNT_CHARGED < amount_payed:
    return "The amount you've is not enough"
  elif AMOUNT_CHARGED == amount_payed:
    return "The bill is payed successfully!, no change "

  result = {}
  total = AMOUNT_CHARGED - amount_payed

  for bill in money_type:
    num = total // bill
    result[str(bill) + '$'] = int(num)
    total = total - num*bill

  print(f'The change is {result}')

change(AMOUNT_CHARGED, amount_payed)
