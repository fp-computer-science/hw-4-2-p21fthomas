grade_percent = int(input("Whats your Grade Percentage? "))
side = "-"      #as in are you positive or negetive 
#y = 34

if grade_percent < 50:
    print("Just, why are you even here?")
elif grade_percent < 60:
    grade_percent %= 10
    if grade_percent >= 5: 
        side = "+"
    print("Grade: F" ,side,)
elif grade_percent < 70:
    grade_percent %= 10
    if grade_percent >= 5: 
        side = "+"
    print("Grade: D" ,side,) 
elif grade_percent < 80:
    grade_percent %= 10
    if grade_percent >= 5: 
        side = "+"
    print("Grade: C" ,side,)
elif grade_percent < 90:
    grade_percent %= 10
    if grade_percent >= 5: 
        side = "+"
    print("Grade: B",side,)
elif grade_percent < 100:
    grade_percent %= 10
    if grade_percent >= 5: 
        side = "+"
    print("Grade: A",side,)
else:
    print("Grade: A++")





#x = 55         i ran many tests to figure this out I didn't just want to make a formula for just regular letter grade but
#a              also a positve and negetive values given. I just couldn't stop working it once I started.
#print(x)
#x %= 10
#if (y %= 10) < 5:
   # print("program must be shit")