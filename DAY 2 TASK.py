Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #print a value
>>> print("30 days 30 hour challenge");
30 days 30 hour challenge
>>> print('30 days 30 hour challenge')
30 days 30 hour challenge
>>> #Assigning string to variable
>>> Hours = "thirty"
>>> print(Hours)
thirty
>>> #Indexing using string
>>> days="Thirty days"
>>> print(days[0])
T
>>> print(days[1])
h
>>> print(days[2])
i
>>> print(days[3])
r
>>> print(days[6])
 
>>> print(days[9])
y
>>> #rint particular character
>>> Challenge = "I will win"
>>> print(Challenge[7:10])
win
>>> print(Challenge[2:5])
wil
>>> print(Challenge[2:6])
will
>>> #print the length of character
>>>  Challenge = "I will win"
 
SyntaxError: unexpected indent
>>> Challenge = "I will win"
>>> print(len(Challenge))
10
>>> print(len(sneha))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(len(sneha))
NameError: name 'sneha' is not defined
>>> Sneha="intern"
>>> print(len(sneha))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(len(sneha))
NameError: name 'sneha' is not defined
>>> print(len(Sneha))
6
>>> #string into lower character
>>> Challenge = "I will win"
>>> print(Challenge.lower())
i will win
>>> Sneha="INTERN At BestEnlist"
>>> print(Sneha.lower())
intern at bestenlist
>>> #String Concatenation
>>> a = "30 Days"
>>> b = "30 hours"
>>> c = a + b
>>> print(c)
30 Days30 hours
>>> a = "Intern"
>>> b = " At"
>>> c=" Best Enlist"
>>> d=a+b+c
>>> print(d)
Intern At Best Enlist
>>> #Space during Concatenation
>>> a = "30 Days"
>>> b = "30 hours"
>>> 
KeyboardInterrupt
>>> c = a + " " + b
>>> print(c)
30 Days 30 hours
>>> #Case fold
>>> text = "Thirty days and Thirty hours"
>>> x = text.casefold()
>>> print(x)
thirty days and thirty hours
>>> x = text.capitalize()
>>> print(x)
Thirty days and thirty hours
>>> x = text.find()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    x = text.find()
TypeError: find() takes at least 1 argument (0 given)
>>> x = text.isalpha()
>>> print(x)
False
>>> x = text.isalnum()
>>> print(x)
False
>>> 