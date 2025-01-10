Startyear=int(input("enter the start year:"))
Endyear=int(input("enter the end year:"))
print("the leap year between", Startyear,"and",Endyear,"are:")
for i in range(Startyear,Endyear):
    if(i%4==0 and i%100!=0 or i%400==0):
        print(i)
