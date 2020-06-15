#soru1
# To take input from the user
num = int(input("Display multiplication table of? = "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', numi)
print("Display multiplication table of? = ",num+1)
for j in range(1, 11):
   print(num+1, 'x', j, '=', (num+1)j)
#soru2
year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print(year,"{0} is a leap year".format(year))
       else:
           print(year,"{0} is not a leap year".format(year))
   else:
       print(year,"{0} is a leap year".format(year))
else:
   print(year,"{0} is not a leap year".format(year))

#soru 3

my_list = [12, 65, 54, 39, 102, 339, 221]

# use anonymous function to filter
result = list(filter(lambda x: (x % 3 == 0), my_list))

# display the result
print("Numbers divisible by 3 are",result)


#soru4
from tkinter import *
def calculate():
    first_s=float(first_n.get())
    second_s=float(second_n.get())
    results=first_s*second_s
    labelresult=Label(myGUI,text="Result : %.2f"%results).grid(row=3,column=0)
    return
myGUI = Tk()
myGUI.geometry('400x200+100+200')
myGUI.title("Multiple Calculator")

first_n=StringVar()
second_n=StringVar()

label1 =Label(myGUI,text='First').grid(row=1,column=0)
label2 =Label(myGUI,text='Second').grid(row=2,column=0)

first=Entry(myGUI,textvariable=first_n).grid(row=1,column=2)
second =Entry(myGUI,textvariable=second_n).grid(row=2,column=2)

button1= Button(myGUI,text='Calculate',command=calculate).grid(row=2,column=3)

myGUI.mainloop()

#soru 5
number = int (input ("Enter an integer number: "))

# calculate square
square = number*number

# print
print ("Square of {0} is {1} ".format (number, square))



#soru6
total = 0 
i = 1
while i<=10:
    total = total + i
    i = i+1
print(total)