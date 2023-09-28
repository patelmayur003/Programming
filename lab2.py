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
#print
print(30*' ', title, '\n', '_' *90)
print (explanations [0] + ' '* 4+ '_ '*3+keyword[0].upper())
print (explanations [1] + ' '* 31+keyword[1].upper()+ ' _ '*3)
print (explanations [2] + ' '* 11+keyword[2].upper()+ ' _ '*4)          
print (explanations [3] + ' '* 46+ '_ '*2+keyword[3].upper())
print (explanations [4] + ' '* 40+ '_ '*2+keyword[4].upper()+ ' _ '*2)
print (explanations [5] + ' '* 11+ '_ '*2+keyword[5].upper()+ ' _ '*5)

print( '_' *90)
correct=0
a1= input(explanations[0]+':')
a2= input(explanations[1]+':')
a3= input(explanations[2]+':')
a4= input(explanations[3]+':')
a5= input(explanations[4]+':')
a6= input(explanations[5]+':')

print( '_' *90)
#check 1
if (a1==words[0]):
    print(explanations[0] + ' '*4 + 'T Y P E')
    correct+=1
else:
    print (explanations [0] + ' '* 4+ '_ '*3+keyword[0].upper())


if (a2==words[1]):
    print (explanations [1] + ' '* 31+'D A T E')
    correct+=1
else:
    print (explanations [1] + ' '* 31+keyword[1].upper()+ ' _ '*3)


if (a3==words[2]):
    print (explanations [2] + ' '* 11+'I N P U T')          
    correct+=1
else:
    print (explanations [2] + ' '* 11+keyword[2].upper()+ ' _ '*4)          

if (a4==words[3]):
    print (explanations [3] + ' '* 46+ 'I N T')
    correct+=1
else:
    print (explanations [3] + ' '* 46+ '_ '*2+keyword[3].upper())

if (a5==words[4]):
    print (explanations [4] + ' '* 40+ 'F L O A T')
    correct+=1
else:
    print (explanations [4] + ' '* 40+ '_ '*2+keyword[4].upper()+ ' _ '*2)

if (a6==words[5]):
    print (explanations [5] + ' '* 11+'V A R I A B L E')
    correct+=1
else:
    print (explanations [5] + ' '* 11+ '_ '*2+keyword[5].upper()+ ' _ '*5)

print( '_' *90)

if (correct==6):
    print('You cracked it, good work')
else:
    print('Check your answers and try again!')
