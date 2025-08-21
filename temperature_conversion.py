#Temperature conversion i.e. from Celsius to Fahrenheit and vice versa

#Celsius as user input
celsius=float(input("Enter the temperature in Celsius\n"))

#convert the Celsius into fahrenheit and display the result 
celsuis_to_fahrenheit=(celsius*9/5)+32
print(f"Temperature in celsius {celsius}")
print(f"In Fahrenheit : {celsuis_to_fahrenheit}")

#Fahrenheit as user input
fahrenheit=float(input("Enter the temperature in fahrenheit\n"))

#convert the fahrenheit into Celsius and display the result 
fahrenheit_to_celsius=(fahrenheit-32)*5/9
print(f"Temperature in Fahrenheit {fahrenheit}")
print(f"In Celsius : {fahrenheit_to_celsius}")
