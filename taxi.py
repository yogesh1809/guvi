ch=("y")
km=0
while(ch=="y"):
  a=int(input("Enter source:"))
  b=int(input("enter destination:"))
  km=b-a
  print(km)
  r=int(input("enter option:"))
  if(r==1):
    print("prime")
    i=8
    cost=km*i
    print(cost)
  if(r==2):
    print("micro")
    j=7
    cost=km*j
    print(cost)
  if(r==3):
    print("mini")
    k=6
    cost=km*k
    print("cost")
    print("Do you want to continue")
    ch=input()
            
  
    