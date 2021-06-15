Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #DAY 4 - PYTHGON VARIABLES & DATA TYPES
>>> #EXERCISE
>>> #1)Create three variables (a,b,c) to same value of any integer & do the following a) Divide a by 10 b) Multiply b by 50 c) Add c value by 60
>>> a=b=c=30
>>> print("The value of a,b and c are ",a" ,",b" and ",c)
SyntaxError: invalid syntax
>>> >>> print("The value of a,b and c are " ,a" ,",b " and ",c)
SyntaxError: invalid syntax
>>> print( "The values of a=" ,a "b=" ,b "and c=" ,c)
SyntaxError: invalid syntax
>>>  print("The value of a,b and c are ",a,b,"and",c)
 
SyntaxError: unexpected indent
>>> print("The value of a,b and c are ",a,b,"and",c)
The value of a,b and c are  30 30 and 30
>>> print( "The values of a=" ,a, "b=" ,b, "and c=" ,c)
The values of a= 30 b= 30 and c= 30
>>> print( "The values of a=",a,"b=",b,"and c=",c)
The values of a= 30 b= 30 and c= 30
>>> print( "The values of a =" ,a, "b =" ,b, "and c =" ,c)
The values of a = 30 b = 30 and c = 30
>>> #a) Divide a by 10
>>> print("Divide a by 10 =",a/10)
Divide a by 10 = 3.0
>>> #b) Multiply b by 50
>>> print("Multiply b by 50 =",b*50)
Multiply b by 50 = 1500
>>> #c) Add c value by 60
>>> print
<built-in function print>
>>> print("Add c value by 60 =",c+10)
Add c value by 60 = 40
>>> #2)Create a String variable of 5 characters and replace the 3rd character with G
>>> string_variable="sneha"
>>> print("String before replacing the 3rd character with G",string_variable)
String before replacing the 3rd character with G sneha
>>> print("String before replacing the 3rd character with G =",string_variable)
String before replacing the 3rd character with G = sneha
>>> print("String after replacing the 3rd character with G =",string_variable.replace("c","G"))
String after replacing the 3rd character with G = sneha
>>> print("String after replacing the 3rd character with G =",string_variable.replace("e","G"))
String after replacing the 3rd character with G = snGha
>>> #3)Create two values (a,b) of int,float data type & convert the vise versa, Hint : convert a from int to float datatype & b from float to int datatype
>>> int a = 10
SyntaxError: invalid syntax
>>> a = 5
>>> b = 5.0
>>> print("The value of a before typecasting=",a)
The value of a before typecasting= 5
>>> print("The value of a before typecasting =",a)
The value of a before typecasting = 5
>>> print("The value of a after typecasting=",float(a))
The value of a after typecasting= 5.0
>>> print("The value of b before typecasting =",b)
The value of b before typecasting = 5.0
>>> print("The value of b after typecasting=",int(b))
The value of b after typecasting= 5
>>> 