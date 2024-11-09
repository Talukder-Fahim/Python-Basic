hours = input("Hours Worked: ").split()
wages = input("Hourly Wage: ").split()
m =len(wages)
bill=0
hours= [int(x) for x in hours]
wages= [int(x) for x in wages]

for x in range(1,m+1):
  hour=hours[x-1]
  wage=wages[x-1]

if hour <= 40:
  bill=int(hour*wage)
else:
  extra=hour-40
  bill=int((wage*40)+(wage*1.5*extra))

print(f"Employee {x}: {bill}")