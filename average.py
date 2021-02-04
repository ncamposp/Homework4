def average (list): #5 elements
  #empty list == dividing by zero
  if len(list) == 0:
    return "Error"
  else:
    return sum(list) / len(list)
  
  