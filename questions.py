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


#                get_os_upgrade_pan()
# This function asks the user what PAN OS they want to upgrade to.
#
# @return os_version - type string - os version user wants to upgrade PAN to.
def get_os_upgrade_pan():
    os_version = raw_input('\n\nWhat PAN OS version would you like to upgrade to? ')
    panos_versions = []
    MAX_OS = 8
    for i in range(0,MAX_OS, 1):
        panos_versions.append(str(i+1)+'.')

    for z in range(0,MAX_OS, 1):
        if os_version.startswith(panos_versions[i]):
            return os_version

    print "Please enter a proper OS. Available options are: ", panos_versions


#         get_engineer()
#
# This function Asks the user for his/her name
#
# @return: Name of the User
def get_engineer():
    while 1:
        user = raw_input('\n\nWho are you? ')
        print 'About to use name: ' + user
        confirm = raw_input('Are you sure? [y/n]: ')
        if 'y' in confirm or 'Y' in confirm:
            print 'about to return ' + user
            return user

print get_engineer()
# get_os_upgrade_pan()
# get_brand()

# get_num_of_interfaces()