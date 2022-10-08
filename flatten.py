l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
list_new = []
def flatten(n):
    for i in n:
        if isinstance(i, list):
            flatten(i)
        else:
            list_new.append(i)

flatten(l)
print(list_new)