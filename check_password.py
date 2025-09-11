
import re

def strength_check(password):
    strength=0

    # length check
    if len(password) >=8:
        strength +=1

    # lowercase letter check
    if re.search(r'[a-z]',password):
        strength +=1

    # uppercase letter check
    if re.search(r'[A-Z]',password):
        strength +=1

    # special character check
    if re.search(r'[@#$^%&*!_?])',password):
        strength += 1

    # strength score
    if strength <=2:
        return "Weak"
    elif strength ==3:
        return "Medium"
    else:
        return "Strong"
    
pwd= input("Enter the password:")
check=strength_check(pwd)
print(check)


    
        
    
        
