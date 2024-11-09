print({1, 3, 5} == {3, 5, 1,1})
print({1, 3, 5} != {3, 5, 1})

set1 = {1, 2, 3, 4}
set2 = {4,5,3,1,2}

# Proper subset (<) and improper subset (<=) comparison
print("Proper subset (<):", set1 < set2)   
print("Improper subset (<=):", set1 <= set2)  

# Proper superset (>) and improper superset (>=) comparison
print("Proper superset (>):", set1 > set2)      
print("Improper superset (>=):", set2 >= set1) 

# Check for improper subset and improper superset using issubset and issuperset methods
print("Improper subset using issubset:", set1.issubset(set2))    
print("Improper superset using issuperset:", set1.issuperset(set2))  

# Union of sets (|)
union_set = set1 | set2
print("Union of sets:", union_set) 

# Intersection of sets (&)
intersection_set = set1 & set2
print("Intersection of sets:", intersection_set)  

# Difference between sets (-)
difference_set = set2 - set1
print("Difference between sets:", difference_set)  
