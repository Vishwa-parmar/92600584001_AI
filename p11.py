
print("=================================================")
print("       MEDICAL DIAGNOSIS EXPERT SYSTEM")
print("=================================================")

print("Answer the following questions with yes or no.")

fever = input("Do you have fever? ").lower()
cough = input("Do you have cough? ").lower()
cold = input("Do you have a cold? ").lower()
headache = input("Do you have headache? ").lower()

print("\n======= Diagnosis Result =======")

if fever == "yes" and cough == "yes" and cold == "yes":
    print("Possible Condition: Flu-like illness")
elif cough == "yes" and cold == "yes":
    print("Possible Condition: Common cold")
elif fever == "yes" and headache == "yes":
    print("Possible Condition: Fever with headache")
elif headache == "yes":
    print("Possible Condition: Headache")
else:
    print("No matching rule found.")

print("\nPlease consult a doctor for proper diagnosis.")
print("Thank you for using the Medical Diagnosis Expert System!")
