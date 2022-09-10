Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Different ways to create a list
>>> lst1 = []
>>> type(lst1)
<class 'list'>
>>> lst1
[]
>>> lst2 = list() #Empty List
>>> lst2
[]
>>> lst3 = [5,1,9,2,5,9,2,8]
>>> lst3
[5, 1, 9, 2, 5, 9, 2, 8]
>>> mytup = (6,1,8)
>>> lst4 = list(mytup)
>>> lst4
[6, 1, 8]
>>> lst5 = list("Indira")
>>> lst5
['I', 'n', 'd', 'i', 'r', 'a']
>>> myset = {7,1,9,2,5}
>>> lst6 = list(myset)
>>> lst6
[1, 2, 5, 7, 9]
>>> lst7 = list(lst4)
>>> lst7
[6, 1, 8]
>>> 