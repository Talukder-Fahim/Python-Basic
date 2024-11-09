name = input("Enter employee name:")
work_hours = int(input("Enter the work hours :"))
years_of_work = int(input("Enter years of work :"))
tasks_done = int(input("Enter tasks done :"))
tasks_given = int(input("Enter tasks given :"))

productivity = tasks_done / tasks_given

if work_hours > 20 and years_of_work >= 2 :
    if 0.5<= productivity <= 0.69:
        Bonus = "Bronze"
    elif 0.7<= productivity <= 0.89:
        Bonus = "Silver"
    elif 0.90<= productivity <= 1.00:
        Bonus = "Gold"
    else :
        Bonus = "normal"
    print(name.title() + " is eligible for the " + Bonus + " bonus")
else :
    print(name.title() + " is not eligible for a bonus")

    
    
            