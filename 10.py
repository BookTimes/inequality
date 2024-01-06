 x = int(input("Enter the value for x: "))
 y = int(input("Enter the value for y: "))

 expression1 = abs(x) + abs(y)
 expression2 = abs(x + y)
 print(f'|x| + |y| = |{x}| + |{y}|')
 print(f'          = {abs(x)} + {abs(y)}')
 print(f'The value of |x| + |y| is: {expression1}\n\n')

 print(f'|x + y| = |{x} + {y}|')
 print(f'        = |{x+y}|')
 print(f'The value of |x + y| is: {expression2}\n\n')

 if expression1 > expression2:
     print('|x| + |y| is greater than |x + y|')
 elif expression1 < expression2:
     print('|x| + |y| is less than |x + y|')
 else:
     print('|x| + |y| is equal to |x + y|')

