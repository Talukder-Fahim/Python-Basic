original = {
    'Emma': {
        'name': 'Emma',
        'major':'Computer Science',
        'cgpa': 3.8,
        'completed_credits': 90
        },
    'Daniel': {
        'name': 'Daniel', 
        'major':'Electrical Engineering', 
        'cgpa': 3.5,
        'completed_credits': 75
        },
    'Sophia': {
        'name': 'Sophia', 'major':'Mechanical Engineering', 
        'cgpa': 3.2,
        'completed_credits': 60
        }
}
print(original["Emma"]["major"])
for key,value in original.items():
    del value["name"]
    del value["major"]
    transformed = sorted(original.items(), key= lambda x : x[1]["cgpa"], reverse= True )

print(transformed)