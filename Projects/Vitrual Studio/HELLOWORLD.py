#HolLOW WORLD!
print("Hello World")
print("Enter the secret PassWord to see the output of secrets")
print("Hint: the answer is linked to README.")

#set passcode
correct_passcode = "chainsmoker"

#initialize Attempts
max_attempts = 666
attempts = 0

while attempts < max_attempts:
    user_passcode = input("Input passkey ")
#check input
    if user_passcode == correct_passcode:
        print("Access Granted")
        print("The world is changing at every turn")
        print("I Bought the Earth...SOld it too")
        break #exits loop if correct passcode
    else:
        attempts += 66
if attempts == max_attempts:
    print("Commense System Wipe...progress 100%")

