def sqrt(n):
  lastGuess = 0.01
  nextGuess = 1
  while (nextGuess - lastGuess) > 0.0001 or (lastGuess - nextGuess) > 0.0001:      # the guess may be larger or smaller than the initial one 
    k = nextGuess  
    nextGuess = (lastGuess + (n / lastGuess)) / 2
    lastGuess = k
  return nextGuess
                                                    # to make sure the input is a positive number
n = input("please input a positive number:")
n=float(n)
          
num = sqrt(n)        
print("the square root is:", num)