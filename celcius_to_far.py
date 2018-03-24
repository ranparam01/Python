def convert_c_to_f(cel):
    if float(cel) < (-273.15):
        print ("Temp cannot be less than -273.15")
    else:
        f=float(cel)*9/5+32
        return f;

cel= input("Enter the temperature in Celcius:")
print(convert_c_to_f(cel))
