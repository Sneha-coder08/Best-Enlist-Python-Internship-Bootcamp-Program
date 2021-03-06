
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

>>> #print particular character
>>> Challenge = "I will win"

>>> print(Challenge[7:10])

win
>>> print(Challenge[2:5])

wil
>>> print(Challenge[2:6])
will


>>> #print the length of character
>>> Challenge = "I will win"
>>> print(len(Challenge))
10

>>> Sneha="intern"
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
>>> print(c)
30 Days 30 hours

>>> #Case fold
>>> text = "Thirty days and Thirty hours"
>>> x = text.casefold()
>>> print(x)
thirty days and thirty hours

#Capitalize-Upper case the first letter in this sentence

>>> x = text.capitalize()
>>> print(x)
Thirty days and thirty hours

#isalpha-returns True if all the characters are alphabet letters (a-z)
>>> x = text.isalpha()
>>> print(x)
False

#isalnum-returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9)
>>> x = text.isalnum()
>>> print(x)
False
