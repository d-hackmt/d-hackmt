lst = [5,1,"Hi",2,"Hi"]
ans = list(set(lst))
print(ans)
def remove_duplicates():
    t = ['a', 'b', 'c', 'd']
    t2 = ['a', 'c', 'd']
    for t in t2:
        t.append(t.remove())
    return t
