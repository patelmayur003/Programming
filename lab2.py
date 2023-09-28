'''
lab2
'''
# Define Variable title, keyword, explanations and words
title = 'fill in the correct terms'
keyword = 'editor'
words = 'type', 'date', 'input', 'int', 'float', 'varible'
explanations = ('Describes how much space the value needs in the memory', 
                'Python libary for handling dates',
                  'Built-in function to read users input to the program',
                    'Integer number', 'Decimal point number',
                      'Named place in program memory accessed with a name')
#print(title) 
print(25*' ',title)
#Print  the line aligned to the middle

print('_'*78)
#print explanations aligned to the left 
#replaces letters in the words and leaves the keyword letter & upper case
print(explanations[0], ' '*12,'_'*3 + keyword[0].upper())
print(explanations[1], ' '*37, keyword[1].upper(),'_'*3)
print(explanations[2],' '*17, keyword[2].upper(),'_'*4)
print(explanations[3],' '*52, '_'*2 , keyword[3].upper())
print(explanations[4], ' '*46,'_'*2,keyword[4].upper(),'_'*2)
print(explanations[5],' '*16,'_'*2, keyword[5].upper(),'_'*5)
print('  ')

# Explanations one by one and ask a user to enter his guess
print("Type your Guess")
print=('  ')
Question0=  input(f"{explanations[0]}{' '*17}:")+++++
Question1=  input(f"{explanations[1]}{' '*39}:")+++++
Question2=  input(f"{explanations[2]}{' '*19}:")
Question3=  input(f"{explanations[3]}{' '*57}:")
Question4=  input(f"{explanations[4]}{' '*51}:")
Question5=  input(f"{explanations[5]}{' '*21}:")

#Print the result so that the correct guesses are printed into the puzzle but the wrong guesses are printed with hidden characters
x = 0
y = 48
if x>y:
    ("x is greanter than y") 
