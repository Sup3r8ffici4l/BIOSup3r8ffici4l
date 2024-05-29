#HolLOW WORLD!
print("Hello World")
print("Welcome Can you guess the passkey???")

#set passcode
correct_passcode="fatcat2024"

#initialize Attempts
max_attempts=666
attempts=0

while attempts<max_attempts:
    user_passcode=input("Input passkey")
#check input
    if user_passcode==correct_passcode:
        print("Access Granted")
        print("Death is only the beginning")
        print("Materials will be left behind")
        break #exits loop if correct passcode
    else:
        print("Forbidden knowledge access denied")
        attempts+=66
if attempts==max_attempts:
    print("Commense System Wipe...progress 100%")

