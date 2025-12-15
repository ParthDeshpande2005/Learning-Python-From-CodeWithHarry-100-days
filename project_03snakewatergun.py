#Snake,Water,Gun project
#         S W  G
compare=[[0,1,-1]   #S
        ,[-1,0,1]   #W
        ,[1,-1,0]]  #G

#comare[player][computer]
#for player=> s=0,w=1,g=2
#for computer=>s=0,w=1,g=2

#taking player input
print("Snake:0,Water:1,Gun=2")
i=int(input("Enter your choice: "))

#generating computer choice
import random
j=random.randint(0,2)
print(j)

#comparing the computer and palyer choice and giving output
if(compare[i][j]==0):print("draw")
if(compare[i][j]==1):print("win(with reference to player)")
if(compare[i][j]==-1):print("loss(with reference to player)")