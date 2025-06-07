def run(*a,playername):
    sum=0
    c=0
    for i in a:
        c=c+1
        sum=sum+i
    avg=sum/c
    print(playername,"Average score is :",avg)
b=int(input("Enter a no. of matches:"))
a=[]
for i in range (b):
    score=int(input("Enetr score:"))
    a.append(score)
playername=input("Enter playername:")
run(*a,playername=playername)
    
