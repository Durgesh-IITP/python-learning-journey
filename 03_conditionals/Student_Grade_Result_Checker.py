# Student Grade & Result Checker 
name = input ("Enter your name:")
marks = float(input("Enter your marks (0-100):"))

if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100:")

elif marks >= 90:
    print(f"\n{name}, your grade is A+")
    print("Very Good Performance!")

elif marks >= 80:
    print(f"\n{name}, your grade is A")
    print(" Very Good Performance!")

elif marks >= 70:
    print(f"\n{name}, your grade is B")
    print("Good Performance!")

elif marks >= 60:
    print(f"\n{name}, your grade is C")
    print("Keep Improving!")

elif marks >= 50:
    print(f"\n{name}, your grade is D")
    print("You Passed, but you can do better.")

else:
  print(f"\n{name}, you have failed.")
  print("Don't give up. Keep practicing!")


    