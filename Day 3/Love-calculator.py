# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
names_comb = name1.lower() + name2.lower()
first_digit = names_comb.count("t") + names_comb.count("r") + names_comb.count("u") + names_comb.count("e")
second_digit = names_comb.count("l") + names_comb.count("o") + names_comb.count("v") + names_comb.count("e")
score = int(f"{first_digit}{second_digit}")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
