Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Different Ways to create a Dictionary
>>> d1 = {'Roll':101,'Name':'Dravid', 'City':'Bengluru'}
>>> d1
{'Roll': 101, 'Name': 'Dravid', 'City': 'Bengluru'}
>>> type(d1)
<class 'dict'>
>>> d1['Name']
'Dravid'
>>> d1['Name'] = 'Rahul Dravid'
>>> d1
{'Roll': 101, 'Name': 'Rahul Dravid', 'City': 'Bengluru'}
>>> del d1['City']
>>> d1
{'Roll': 101, 'Name': 'Rahul Dravid'}
>>> d1['Per']
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    d1['Per']
KeyError: 'Per'
>>> d1['Per']  = 9.8
>>> d1
{'Roll': 101, 'Name': 'Rahul Dravid', 'Per': 9.8}
>>> d1['Marks']= [56,78,91]
>>> d1
{'Roll': 101, 'Name': 'Rahul Dravid', 'Per': 9.8, 'Marks': [56, 78, 91]}
>>> d2 = {1:1,2:4,3:9,4:16,5:25,3:19}
>>> d2
{1: 1, 2: 4, 3: 19, 4: 16, 5: 25}
>>> d3 = {101:'ABC', 102:'PQR',103:'ABC', 102:'XYZ']
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> d3 = {101:'ABC', 102:'PQR',103:'ABC', 102:'XYZ'}
>>> d3[102]
'XYZ'
>>> d3.
SyntaxError: invalid syntax
>>> d3
{101: 'ABC', 102: 'XYZ', 103: 'ABC'}
>>> d4 = {1:('ABC','PQR'), 2:[1,2,3],3:{6,8,9}}
>>> d4
{1: ('ABC', 'PQR'), 2: [1, 2, 3], 3: {8, 9, 6}}
>>> d4[1]
('ABC', 'PQR')
>>> d4[2]
[1, 2, 3]
>>> d5 = {[1,2]:"Hello", 56:'ABC'}
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    d5 = {[1,2]:"Hello", 56:'ABC'}
TypeError: unhashable type: 'list'
>>> 