#Conditonal statements 
#Grading system
student_name = (input("Enter student name :"))
sub_1 = int(input("Enter math grades :"))
sub_2 = int(input("Enter economics grades :"))
sub_3 = int(input("Enter accounting grades :"))
total = sub_1 + sub_2 + sub_3
print(student_name, "your total marks are", total)
if total > 260 :
    print("Grade A")
elif total > 240 :
    print("Grade B")
elif total > 220 :
    print("Grade C")
elif total > 200 :
    print("Grade D")
elif total > 180 :
    print("Grade E")
else :
    print("Fail")