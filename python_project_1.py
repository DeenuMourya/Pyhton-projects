#python script to make a game to rearrange the characters of a string to create words

import os

list_1=["OBKO","ESWT","RETGI","OTBFLAOL","RECODS"]
list_2=["book",'west','tiger','football','coders']

count=0

os.system('cls')

print('\n\n     :: YOU have 5 chances to win the GAME ::\n\n')
print("Note :: Every move will reduce yours chances\n\tfor win score at least 3 points.")

for a in range(0,5):
    print("\n",list_1[a])
    temp=input("Enter the correct word :: ")
    if(temp==list_2[a]):
        count+=1
        print('|| Correct ||\n')
    else:
        count-=1
        print('|| Wrong ||')

if count>3:
    print("Congratulations you have won the game\nScore is",count)
else:
    print('You Lose the game ::\nScore is',count)
input()