def data_type(y):
    if y is  None:
      return "no value"
    elif type(y) == str:
      return len(y)
    elif type(y) == bool:
      return y
    elif type(y) == int:
        if y < 100:
            return "less than 100"
        else: 
            return "more than 100"
    elif type(y) == list:
        if len(y) < 3:
            return None
        else:
            return y[2]