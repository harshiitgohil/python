# factorial (7) = 7*6*5*4*3*2*1
# factorial (6) = 6*5*4*3*2*1
# factorial (5) = 5*4*3*2*1
# factorial (0) = 1

def factorial(n):
  if(n==0) or (n==1):
    return 1
  else:
    return n * factorial(n-1) #that's perform like 5, 5-1=4 ,4-1=3, 3-1=2, 2-1=1 over
                              #result is 5*4*3*2*1 

print(factorial(5))
print(factorial(3))
print(factorial(2))