Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = ([101,'ABC'], [102,'XYZ'],[103,'PQR'])  #Tuple of Lists
>>> d1 = dict(data)
>>> d1
{101: 'ABC', 102: 'XYZ', 103: 'PQR'}
>>> data = [('Roll',101),('Name','Dravid')]   #List of Tuples
>>> d2 = dict(data)
>>> d2
{'Roll': 101, 'Name': 'Dravid'}
>>> #You may have List of Lists and Tuple of Tuples to create dictionary using dict() function
>>> #WAY-3
>>> d3 = dict(Roll=101,Name='Saina',City='Hyderabad')
>>> d3
{'Roll': 101, 'Name': 'Saina', 'City': 'Hyderabad'}
>>> #Function with Keyword arguments in Python
>>> 