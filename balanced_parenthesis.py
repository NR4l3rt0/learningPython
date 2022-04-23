def balanced(expression):
    #your code goes here
    lst = []
    for el in expression:
        if el == '(':
            lst.insert(0,el)
        elif el == ')':
            if len(lst) > 0 and lst[0] == '(':
                lst.pop(0)
            else:
                return False
        else:
            continue

    return True if len(lst) == 0 else False

print(balanced(input()))
