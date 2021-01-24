# Payroll Program
def main ():
    hrs,rate=dataentry()
    normal_hrs,overtime_hrs,overtime=computepay(hrs,rate)
    regular,total_pay=preovertime_hrs(hrs,rate,overtime)
    displayPay(rate,normal_hrs,overtime_hrs,regular,total_pay)
def dataentry():
    name=input("Name of Staff :")
    hrs=float(input("Enter the hrs worked :"))
    rate=float(input("Enter the Pay Rate :"))
    return hrs,rate
def computepay(hrs,rate):
    if hrs<40:
        normal_hrs=hrs
        overtime_hrs=0
    else:
        normal_hrs=40
        overtime_hrs=hrs-40
    if hrs >40:
        overtimerate=2.8 * rate
        overtime=(hrs-40)*overtimerate
    else:
        overtime=0
    return normal_hrs,overtime_hrs,overtime
def preovertime_hrs(hrs,rate,overtime):
    regular=hrs*rate
    total_pay=regular
    return regular,total_pay    
def displayPay(rate,normal_hrs,overtime_hrs,regular,total_pay):
    print('Take Home is $'+format(total_pay,'.2f'))
main()


   
