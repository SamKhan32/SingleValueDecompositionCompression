print('Hey user, please input ten values and I"\'ll tell you the largest odd number')
i=0
x = int((input(' Enter: ')))

while (i < 10):
        a = int((input('Enter: ')))
        
        if a%2 ==1 and a>x:
            print('If statement reached')
            x = a
        i = i+1
if x%2 ==1:
    print(x)
    print(' is the largest odd number inputted')
else:
    print('No odd numbers inputed')