from devicetype import *
import datetime

#            get_brand()
#
# Gets the device brand from the user
#
# @return brand - type string - device brand
def get_brand():
    print "     Available Device options:"
    i = 0
    for device in invalid_cmd_key:
        print str(i) + ') ' + device
        i += 1
    brand = raw_input('\n\nWhat Device Manufacture are you using?[name] ')
    if brand.isdigit():
        print 'Type the full name please'
        return get_brand()
    for device in invalid_cmd_key:
        print device
        if device == brand:
            return brand
    print("\n\nYou did not enter a proper device Name. Try again.")
    return get_brand()

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
        print 'Please enter a valid number.\n\n '
        return get_num_of_interfaces()


#                get_os_upgrade_pan()
#
# This function asks the user what PAN OS they want to upgrade to.
#
# @return os_version - type string - os version user wants to upgrade PAN to.
def get_os_upgrade_pan():
    os_version = raw_input('\n\nWhat PAN OS version would you like to upgrade to? ')
    panos_versions = []
    MAX_OS = 8
    for i in range(0, MAX_OS, 1):
        panos_versions.append(str(i+1)+'.')

    for z in range(0,MAX_OS, 1):
        if os_version.startswith(panos_versions[i]):
            return os_version

    print "Please enter a proper OS. Available options are: ", panos_versions

#        get_information()
#
# Helper function that prints prompt, gets input from user
# and confirms this input is what the user wants.
def get_information(prompt, confirmation):
    while 1:
        usr_input = raw_input('\n\n' + prompt)
        if usr_input == 'exit' or usr_input =='Exit':
            exit()
        print '\n\n' + confirmation + usr_input
        confirm = raw_input('Are you sure? [y/n]: ')
        if 'y' in confirm or 'Y' in confirm:
            return usr_input


#         get_engineer()
#
# This function Asks the user for his/her name
#
# @return: Name of the User
def get_engineer():
    my_prompt = 'Who are you? '
    my_confirmation ='About to use name: '
    return get_information(my_prompt, my_confirmation)


def get_serial_number():
    my_prompt = 'What is the device\'s serial number \n  (You can find this on the box or device itself)? '
    my_confirmation = 'About to use serial number: '
    return get_information(my_prompt, my_confirmation)

#         get_device_specifications()
#
# This function asks the user for the device specs URL
#
# @return: url - string  - url to add to the report
def get_device_specifications():
    my_prompt = 'What is the URL to the device specifications? '
    my_confirmation = 'About to use URL: '
    return get_information(my_prompt, my_confirmation)


#      get_date()
#
# This function gets the date based of the computer's set date
#
# @return: date - string type - MM/dd/YYYY format
def get_date():
    return datetime.datetime.today().strftime('%m/%d/%Y')


def get_equipment_model():
    my_prompt = 'What device model do you have? '
    my_confirmation = 'About to use device model: '
    return get_information(my_prompt, my_confirmation)


def get_os_upgrade():
    my_prompt = ''

# get_date()
# print get_equipment_model()
# get_serial_numbers()
# get_os_upgrade_pan()
# get_brand()

# get_num_of_interfaces()