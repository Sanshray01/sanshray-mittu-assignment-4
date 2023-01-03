import random 
num1 = [1,2,3,4,5,6,7,8,9,10] # making list for random variables
for i in range(1,11):
     a1 = random.choice(num1)
     a2 = random.choice(num1)
     print(f"{a1} X {a2}")
     y = round(a1 * a2)
     x = int(input("Enter your answer : "))
     if x ==y:
        print("Congratulations, your answer is correct")
     else:
         print(f"Your answer is wrong, the correct answer is {y}")