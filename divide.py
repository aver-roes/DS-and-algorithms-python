''' Write a Python program that can take a positive integer greater than 2 as input and write out
 the number of times one must repeatedly divide this number by 2 before getting a value less than 2. '''
 
def divide(num):
  if num <= 2:
    return "Enter an intger bigger than 2"
  i = 1
  while pow(2,i) <= num:
    i += 1
  return i - 1

divide(3)
