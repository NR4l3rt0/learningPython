if 4 == 4:
    print('true')


is_true = 'False'

if not is_true:
    print('catcha')
elif type(is_true) == type(bool()):
    print("It's boolean")
else:
    print('It was false')

