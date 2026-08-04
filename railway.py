while True:
    def railway_ticket():
        ticket=1000
        gender=input("Enter your gender (male/female): ")
        age=int(input("Enter your age: "))
        if gender=="male" and age>=60:
            print("senior citizen")
            ticket=ticket-30/100*ticket
            print("Your ticket price is:",ticket)
        elif gender=="male" and age<60:
            print("normal citizen")
            print("Your ticket price is:",ticket)
        elif gender=="female" and age>=60:
            print("senior citizen")
            ticket=ticket-50/100*ticket
            print("Your ticket price is:",ticket)
        elif gender=="female" and age<60:
            print("normal citizen")
            print("Your ticket price is:",ticket)
    railway_ticket()