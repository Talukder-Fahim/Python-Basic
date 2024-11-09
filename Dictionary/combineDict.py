lnput_data = [
        {'item': 'item1', 'amount': 400},
        {'item': 'item2', 'amount': 300},
        {'item': 'item1', 'amount': 750}
]
totals = {}

for item in lnput_data:
    if item["item"] in totals:
        totals[item['item']] += item['amount']
    else:
        totals[item['item']] = item['amount']

print(totals)
#Expected Output:{'item1': 1150, 'item2': 300}