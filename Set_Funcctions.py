Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1 = set()
>>> s1 = {4,8,1,3,2}
>>> s2 = {6,1,9,4}
>>> #Set Difference
>>> ans = s1 - s2
>>> ans
{8, 2, 3}
>>> ans = s2-s1
>>> ans
{9, 6}
>>> ans = s1.difference(s2)
>>> s1
{1, 2, 3, 4, 8}
>>> s2
{1, 4, 6, 9}
>>> ans
{8, 2, 3}
>>> #Set Union
>>> ans = s1 | s2
>>> ans
{1, 2, 3, 4, 6, 8, 9}
>>> ans = s1.union(s2)
>>> ans
{1, 2, 3, 4, 6, 8, 9}
>>> #Set Intersection
>>> ans = s1 & s2
>>> ans
{1, 4}
>>> ans = s1.intersection(s2)
>>> ans
{1, 4}
>>> #Symmetric Difference
>>> ans = s1 ^ s2
>>> ans
{2, 3, 6, 8, 9}
>>> ans = s1.symmetric_difference(s2)
>>> ans
{2, 3, 6, 8, 9}
>>> s3 = {1,3,6}
>>> s4 =  {7,8}
>>> #Disjoint sets --> Both the involved sets not having any common element with them
>>> s3.isdisjoint(s4)
True
>>> s1
{1, 2, 3, 4, 8}
>>> s1.isdisjoint(s3)
False
>>> s5 = {3,4,1}
>>> s1 > s5 #s1 is superset of s5 ?
True
>>> s5 < s1 #s5 is subset of s1 ?
True
>>> s1.issuperset(s5)
True
>>> s2.issubset(s5)
False
>>> s2
{1, 4, 6, 9}
>>> s5.isset(s1)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s5.isset(s1)
AttributeError: 'set' object has no attribute 'isset'
>>> s5.issubset(s1)
True
>>> s1
{1, 2, 3, 4, 8}
>>> s2
{1, 4, 6, 9}
>>> s1 = s1 - s2
>>> s1
{8, 2, 3}
>>> s1= {1, 2, 3, 4, 8}
>>> s2
{1, 4, 6, 9}
>>> s1.difference_update(s2)  # s1 = s1 - s2
>>> s2
{1, 4, 6, 9}
>>> s1
{2, 3, 8}
>>> #frozenset
>>> #frozenset is IMMUTABLE in nature.
>>> s1
{2, 3, 8}
>>> fzset = frozenset(s1)
>>> type(fzset)
<class 'frozenset'>
>>> fzset
frozenset({8, 2, 3})
>>> 