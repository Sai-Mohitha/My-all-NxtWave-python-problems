def validate_atm_pin_code(pin):
    # Complete this function
    if (len(pin) == 6 or len(pin)==4) and pin.isdigit():
        print("Valid PIN Code")
    else :
        print("Invalid PIN Code")
        

pin = input()
# Call the validate_atm_pin_code function
validate_atm_pin_code(pin)