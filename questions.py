from devicetype import *


#            get_brand()
# Gets the device brand from the user
#
# @return brand - type string - device brand
def get_brand():
    print "     Available Device options:"
    i = 0
    for device in invalid_cmd_key:
        print str(i) + ') ' + device
        i += 1
    brand = raw_input('\n\nWhat Device Manufacture are you using? ')

    for device in invalid_cmd_key:
        if device == brand:
            return brand
    print("\n\nYou did not enter a proper device Name. Try running the program again")
    exit(0)

#
# @return: number - type int, number of interfaces
def get_num_of_interfaces():
    MAX = 100
    try:
        number = input("How many Interfaces does the device have? ")
    except Exception as e:
        print 'You did not enter a valid number. Please try again.'
        exit(0)
    if number < 100 and number > 0:
        return number
    else:
        print 'Current maximum Number is '+ str(MAX-1) + ' Please enter a smaller number.\n\n '
        exit(0)

# get_brand()

get_num_of_interfaces()