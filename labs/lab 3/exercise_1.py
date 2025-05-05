def sleep_in(weekday, vacation):
  if not weekday == True or vacation == True:
    return True
  else:
    return False

def parrot_trouble(talking, hour):
  if (hour < 7 or hour >20) and talking == True:
    return True
  elif hour >= 7 and hour < 20:
    return False
  else:
    return False

def sum_double(a, b):
  global answer
  if a == b:
    answer = 4*a
  else:
    answer = a+b
  return answer

def set_square(x):
    global ret_square
    ret_square = x*x
    return ret_square
