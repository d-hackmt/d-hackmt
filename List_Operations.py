Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #List Operations
>>> lst1 = [5,1,8]
>>> lst2 = [6,2]
>>> #Add two lists
>>> lst3 = lst1 + lst2
>>> lst3
[5, 1, 8, 6, 2]
>>> ans = lst1*3  #Repetition
>>> ans
[5, 1, 8, 5, 1, 8, 5, 1, 8]
>>> #Membership Operators
>>> 8 in lst1
True
>>> -8 not in lst1
True
>>> 1 not in lst1
False
>>> #Indexing Operations
>>> lst3
[5, 1, 8, 6, 2]
>>> lst3[2]
8
>>> lst3[-4]
1
>>> #Slicing Operation
>>> lst3[2:5]
[8, 6, 2]
>>> rev_lst = lst3[::-1]
>>> rev_lst
[2, 6, 8, 1, 5]
>>> lst3
[5, 1, 8, 6, 2]
>>> max(lst3)
8
>>> min(lst3)
1
>>> sum(lst3)
22
>>> len(lst3)
5
>>> #Performing the Mutability Test over the LIST
>>> lst3
[5, 1, 8, 6, 2]
>>> lst3[2] = 21
>>> lst3
[5, 1, 21, 6, 2]
>>> del lst3[-1]
>>> lst3
[5, 1, 21, 6]
>>> lst3 = lst3 + [2,9,4,1,6]
>>> lst3
[5, 1, 21, 6, 2, 9, 4, 1, 6]
>>> del lst3[3:6]
>>> lst3
[5, 1, 21, 4, 1, 6]
>>> lst3[1:3] = 5,6,7
>>> lst3
[5, 5, 6, 7, 4, 1, 6]
>>> #Performing operations using few Misc. Functions on the sequence LIST
>>> lst1 = [6,"Hi",9.0,3.4,45]
>>> all(lst1)
True
>>> lst2 = [6,"Hi",0.0,3.4,45]
>>> all(lst2)
False
>>> lst3 = [0,False,"",None,[],(),{},"ICCS"]
>>> any(lst3)
True
>>> lst4 = [0,False,"",None,[],(),{}]
>>> any(lst4)
False
>>> #Nested List
>>> lst_num = [5,1,7,[11,22,33],8,9]
>>> len(lst_num)
6
>>> lst_num[3]
[11, 22, 33]
>>> lst_num[3][1]
22
>>> 