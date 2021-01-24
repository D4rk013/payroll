#Payroll Program
print ("Gross Pay of the Employes")
print('-'*50)
#Enter the hour worked and pay rate
hours=float(input("Enter No. of Hours work : "))
rate=float(input("Enter the Rate in Rs : "))
grosspay = rate*hours
# validate the input data and generate the Gross pay, if valid.
if rate<1000 :
    print("Invalid Pay Rate") 
elif rate>1000000 :
    print("Invalid Pay Rate")
elif hours < 0:
    print("Invalid Hour")
    print("Enter hour between 0 and 100 Range ")
elif hours > 100:
    print("Invalid hour")
    print("Enter hour between 0 and 100 Range")
else :
    print('-'*50)
    print ("Gross Pay is Rs{:,.2f}".format(grosspay))
