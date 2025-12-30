def stu_rep(name, m1, m2, m3, m4, m5, m6):
    avg = (m1 + m2 + m3 + m4 + m5 + m6)/6
    perc = ((m1 + m2 + m3 + m4 + m5 + m6)/600) * 100
    if (perc >= 85 and perc <= 100):
        grade = 'A'
    elif (perc >= 75 and perc < 85):
        grade = 'B'   
    elif (perc >= 60 and perc < 75):
        grade = 'C'
    elif (perc >= 35 and perc < 60):
        grade = 'D'
    elif (perc >= 0 and perc < 35):
        grade = 'F'  
    else:
        grade = "Invalid marks" 
    return avg, perc, grade
name = "Sangeeta"
m1 = 93
m2 = 87
m3 = 99
m4 = 96
m5 = 91 
m6 = 96
avg, percent, grade = stu_rep(name, m1, m2, m3, m4, m5, m6)
print(f"name: {name}\nAverage: {avg}\nPercentage: {percent}\nGrade: {grade}")