import random
target = random.randint(1000,9999)
print(target)
flag=False
str2=str(target)

def check (target):
    str1=str(target)
    return len(set(str1)) == len(str1)
        
        
while not flag:
    if check(target):
        flag=True
        
    else:
        target = random.randint(1000,9999)
        print("new target :", target)
        

    
flag1=False
bulls=0
cow=0
set1=set()
while not flag1:
    guess=input("Enter your guess:")
    
    
    for i in range(4):
        if guess[i] == str2[i]:
            cow +=1
            set1.add(i)
        elif guess[i] != str2[i]:
            bulls +=1
            
            
            
    print("cow :",cow)
    print("bulls :",bulls)  
    
           
    if len(set1) ==4:
        flag=True
        print("congratulation ! You guessed the numbers right ")     
        
        

        
    