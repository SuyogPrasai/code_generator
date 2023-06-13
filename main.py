import os
from generator import generator
## Main Sequence
while True:
    while True:
        choice = str(input("Do you want to encrypt or decrypt [(E)\(D)]: "))
        choice = choice.lower()
        if choice == "e" or choice == "d": 
            break   
    text = str(input("Give me text: "))
    generator_instance = generator()
    if choice == "e":
        p_message = "Encrypted" 
        newText = generator_instance.encrypt(text)
    elif choice == "d": 
        p_message = "Decrypted"
        newText = generator_instance.decrypt(text)
    else: 
        print("Error")
    print("=================================================")
    print(f"{p_message} Text: ", newText)
    print("=================================================")

    exit_true = "Y"
    exit_true = str(input("Do you want to continue? [(Y)/(N)]: "))
    exit_true = exit_true.upper()
    if exit_true == "N": 
        break
    else:
        os.system('cls')
        continue 

        
