#App to countdown birthday with Talk python to me
import datetime


def print_Header():
    print('----------------------------------------------------------------')
    print('                  Birthday Countdown App               ')
    print('----------------------------------------------------------------')
    print('')
    
    
def Get_Birthday_From_User():
    print("When were you born? ")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [mm]: ")) #Keyboard short cuts are extremely useful, Ctrl+Shift+D copy line down
    day = int(input("Day [DD]: "))

    bday =datetime.date(year, month, day)
    return bday


def compute_Days_Between_Dates(Original_date, Target_date):
    this_year = datetime.date(Target_date.year, Original_date.month, Original_date.day)
    dt = this_year - Target_date
    
    return dt.days


def print_Birthday_Information(days):
    if days < 0:
        print ("You had your birthday {} days ago this year." .format(-days))
    elif days > 0:
        print("Your birthday is in {} days!" .format(days))
    else:
        print("Your birthday must be today! Happy birthday!")


def main(): #Main method is not needed in python, unlike java, this is just a convention
    print_Header()
    bday = Get_Birthday_From_User()
    today = datetime.date.today() #None == Equivalent to null?
    Number_Of_Days = compute_Days_Between_Dates(bday, today)
    print_Birthday_Information(Number_Of_Days)
  
    
#we have to invoke main() this way, is not ideal but he will show a better way.
main()