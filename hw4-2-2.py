dave = int(input("Whats your BMI? "))

if dave < 19: 
    print("Dave is Undeweight")
elif dave < 25:
    print("Dave is Healthy")
elif dave < 30:
    print("Dave is Overweight")
elif dave < 40:
    print("Dave is Obese")
elif dave > 40:
    print("Dave is Extremely Obese")

