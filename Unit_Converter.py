
print "Welcome to my unit converter! Lets convert kilometers into miles!"

while True:
    print "Enter a number of kilometers you want to convert into miles"
    km = raw_input("Kilometers: ")

    try:
        km = float(km.replace(",", "."))

        miles = km * 0.621371

        print "{0} kilometers is {1} miles.".format(km, miles)
    except Exception as e:
        print "Please enter a number, not text!"

    choice = raw_input("Do you want to do another conversion (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        print "Thank you for using our converter!"
        break
