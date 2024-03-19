num=int(input("enter the value of number"))
if(num<0):
         print("number is nagetive")
elif(num>0):
        if(num<=10):
           print("num is between 0 and 10")
        elif(num>10 and num<20):
            print("num is between 10 and 20")
        else:
            print("num is greater than 20")
else:
         print("number is positive")      
            