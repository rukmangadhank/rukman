from sys import argv
script,num1,num2,num3=argv
if (num1 >= num2) and (num1 >=num3):
      print(num1)

elif (num2 >= num1) and (num2>=num3):
     print(num2)

else:
     print(num3)     
