"""
Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence 
by either returning the string true or false. The str parameter will be composed of + and = symbols with several characters 
between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. So the string to the left would be false.
The string will not be empty and will have at least one letter. 
"""
import re
def SimpleSymbols(strParam):

  # code goes here
  harfler=list("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")

  strParam = strParam.lower()
  n = 0
  letter_str = re.sub("[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz]", "", strParam)
  letters = len(letter_str)
  if strParam[0] in harfler or strParam[-1] in harfler:
    return False
  else: 
    for x in range(1,len(strParam)-1):
      index = harfler[x]
      if index in harfler and strParam[x-1]== "+" and strParam[x+1] == "+":
        n +=1
      else:
        n+= 0
  if n == letters:
    return True
  else:
    return False
    
    

  return strParam

# keep this function call here 
print SimpleSymbols(raw_input())
