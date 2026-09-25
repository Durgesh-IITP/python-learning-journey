# Scholarship / Eligibility Checker
# Checks eligibility based on age, marks, family income, and student type

age = int(input("Enter your age: "))
marks = float(input("Enter your marks (%): "))
family_income = int(input("Enter annual family income: "))
regular_student = input("Are you a regular student? (yes/no): ").lower()

if age >= 18 and marks >= 75 and family_income <= 300000 and regular_student == "yes":
    print("✅ Congratulations! You are eligible.")
else:
    print("❌ Sorry, you are not eligible.")
    
    # Optional: tell them which condition(s) failed
    if age < 18:
        print("- Age criteria not met (must be 18 or above)")
    if marks < 75:
        print("- Marks criteria not met (must be 75% or above)")
    if family_income > 300000:
        print("- Family income criteria not met (must be 3,00,000 or below)")
    if regular_student != "yes":
        print("- Must be a regular student")