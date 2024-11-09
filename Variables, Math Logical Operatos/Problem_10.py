score = float(input())

if 90<=score<=100:
    Grade = "A"
    Remarks = "Oustanding"
elif 86<=score<=89:
    Grade = "A-"
    Remarks = "Excellent"
elif 82<=score<=85:
    Grade = "B+"
    Remarks = "Very Good"
elif 78<=score<=81:
    Grade = "B"
    Remarks = "Good"
elif 74<=score<=77:
    Grade = "B-"
    Remarks = "Above Average"
elif 70<=score<=73:
    Grade = "C+"
    Remarks = "Average"
elif 66<=score<=69:
    Grade = "C"
    Remarks = "Below Average"
elif 62<=score<=65:
    Grade = "C-"
    Remarks = "Poor"
elif 58<=score<=61:
    Grade = "D+"
    Remarks = "Very Poor"
elif 55<=score<=57:
    Grade = "D"
    Remarks = "Pass"
else:
    Grade = "F"
    Remarks = "Fail"
print("Grade= "+Grade+","+Remarks)


