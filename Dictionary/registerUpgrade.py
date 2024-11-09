company_hr_register = {
                    101: {'name': 'Alice', 'age': 35,'performance': 90, 'salary': 50000},
                    102: {'name': 'Bob', 'age': 58,'performance': 98, 'salary': 70000},
                    103: {'name': 'Charlie', 'age': 45,'performance': 85, 'salary': 60000},
                    104: {'name': 'David', 'age': 60,'performance': 75, 'salary': 55000},
                    105: {'name': 'Eve', 'age': 28,'performance': 92, 'salary': 48000},
                    106: {'name': 'Frank', 'age': 50,'performance': 55, 'salary': 52000},
                    107: {'name': 'Grace', 'age': 62,'performance': 97, 'salary': 75000},
}
total_amount = 0
count = 0
updated_hr_register = {}

for keys,values in company_hr_register.items():
    if values["age"] > 55 and values["performance"] > 95:
        del values["age"]
        del values["performance"]
        del values["salary"]

        updated_hr_register[keys] = values
        
        total_amount += 15000
        count += 1
        
        # for key,value in updated_hr_register.items():
        #     if value == "age" and value == "performance" and value == "salary" :
        #         del updated_hr_register[key][value]
        # print(f"Updated_hr_register = {updated_hr_register}")    
# delete = ["age", "performance", "salary"]
# for i in delete:
#     if i in  updated_hr_register.values():
#         del updated_hr_register[102][i]
print(f"Updated_hr_register = {updated_hr_register}") 
print(f'Total_bonus_amount = {total_amount}')
print(f'Total_employee = {count}')


