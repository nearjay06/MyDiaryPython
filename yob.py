from datetime import date
  


def age():
    yob= int(input( 'Enter year of birth:  '))                    
    today_date = date.today().year
    age= today_date - yob
    if age < 18:
        print('minor')
    elif age >= 18 and age <= 36:
        print('youth')    
    else:
        print('elder')    

age()           


