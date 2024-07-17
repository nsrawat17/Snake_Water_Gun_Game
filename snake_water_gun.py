'''
1 for   snake
-1 for water
0 for gun



'''
import random



computer =random.choice([1, -1, 0])
print("s for snake \nw for water \ng for gun ")
youstr=input("enter your choice ")
youDict={"s" : 1,"w" :-1 , "g" :0}
reverseDict={1:"Snake", -1:"Water" ,0: "Gun"}

you=youDict[youstr]

print(f" You choose {reverseDict[you] }\n Computer choose   {reverseDict[computer]}")

if(computer==you):
    print("it's Draw")

else:
    if(computer==1 and you==-1):
        print("YOU LOSE !")
    elif(computer==1 and you ==0):
        print("YOU WIN!")
    elif(computer==-1 and you ==1):
        print("YOU WIN!! ")
    elif(computer==-1 and you==0):
        print("YOU LOSE!")
    elif(computer==0 and you==1):
        print("YOU LOSE!")
    elif(computer==0 and you==-1):
        print("YOU WIN!")

    else:
        print("SOMETHING WENT WRONG !")


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
