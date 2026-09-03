#comparison operators
maths = int(input("Enter your maths score :"))
print("  ")
eng= int(input("Enter your English score :"))
print("  ")
his = int(input("Enter your  History score :"))
print("  ")
cscience = int(input("Enter your computer Science score :"))
print("  ")
ttmarks = maths + eng + his + cscience
print("Your total marks are :", ttmarks)
avg = ttmarks/4
print("The average is", avg)
#conditional statements 
#comparison operators
if avg >= 90:
 print("Grade A")
elif (avg >= 70):
 print("Grade B")
 
