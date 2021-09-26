"""Level: Easy 
Three chance to guess correct answers.
"""
import csv

def easy():
    import random as r                
    tscor=0
    chk="T"
    
    
    while chk=="T":
        num=r.randint(1,6)
        
        ent=int(input("Choose a digit between 1 to 6:"))
        if ent==num:
            tscor+=150
            print("Right! Score till now:",tscor)
            
            continue
        
        else:
            chc=int(input("Wrong Choice!!(2 chances left) Enter another number:"))
            if chc==num:
                tscor+=100
                print("Right! Score till now:",tscor)
                
                continue
            
            else:
                chc1=int(input("Wrong Choice!!(Last Chance) Enter another number:"))
                if chc1==num:
                    tscor+=50
                    print("Right! Score till now:",tscor)
                    
                    continue
                
                else:
                    chk="F"
                
    
    print("Game Over :(")
    print("The number was:",num)    
    print("Your Score:",tscor)
    savescr(tscor)


    
    
def savescr(scor):
    file=open("comEasyMode.csv","a",newline="")
    fwrit=csv.writer(file)
    for i in range(5):
        fwrit.writerow(["Player",0])
    file.close()
    
    file=open("comEasyMode.csv","r",newline="")
    read1=csv.reader(file)
    storinlst=list(read1)
    scorestr=[]

    for i in storinlst:
        scorestr.append(i[1])
    scoreint=list(map(int,scorestr))
    
    if scoreint[-1]>=scor:
        pass
    else:
        count1=0
        print("....BINGO....You made it into TOP FIVE....")
        plyrnm=input("Enter Name: ")
        newlst=[plyrnm,scor]
        
        for i in range(len(scoreint)):
            if scor>=scoreint[i] and count1==0:
                count1+=1
                storinlst.insert(storinlst.index(storinlst[i]),newlst)
                storinlst.pop()

            
            
    file=open("comEasyMode.csv","w",newline="")
    fwrit2=csv.writer(file)
    count=1
    for i in storinlst:
        if count<=5:
            fwrit2.writerow(i)
        count+=1
    file.close()
    
    
def scoreread():
    print("\n"*2)
    print("...Top Five Scores...")
    file=open("comEasyMode.csv","r",newline="")
    read2=csv.reader(file)
    for i in read2:
        for j in i:
            print(j,end=" ")
        print()
        
        


            
    
        
