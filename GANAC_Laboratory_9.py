#Jefferson O. Ganac
#IT - 103
rownumber = int(input("Enter the number of rows: "))
#input for number of rows
number = 1
#number of rows
for i in range(1, rownumber + 1):
  
  
    for j in range(i):
        print(number, end=" ")
        number += 1 
    print()  