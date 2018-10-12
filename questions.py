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
# @return: number - type int, number of interfaces that are being checked
def get_num_of_interfaces():
    MAX = 100
    try:
        number = input("How many total Interfaces does the device have? ")
        # number2 = input("How many Interfaces do you want to check? ")
    except Exception as e:
        print 'You did not enter a valid number. Please try again.'
        exit(0)
    if number < MAX and number > 0: # or (number2 < number and number2 > 0):
        return number
        #, number2
    else:
        print 'Please enter a valid number.\n\n '
        return get_num_of_interfaces()

def get_os_upgrade(device_type):
    # Interface funcs are stored in interface_funcs.py
    os_upgrade_funcs[device_type]()
#                get_os_upgrade_pan()
#
# This function asks the user what PAN OS they want to upgrade to.
#
# @return os_version - type string - os version user wants to upgrade PAN to.
def get_os_upgrade_cisco():
    os_version = raw_input('\n\nWhat Cisco OS version would you like to upgrade to? ')
    os_versions = []
    MAX_OS = 16
    for i in range(0, MAX_OS, 1):
        panos_versions.append(str(i+1)+'.')

    for z in range(0,MAX_OS, 1):
        if os_version.startswith(os_versions[i]):
            return os_version

    print "Please enter a proper OS. Available options are: ", os_versions


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


def get_os_upgrade(brand, MAX_OS):
    prompt = '\n\nWhat ' + brand + ' OS version would you like to upgrade to? '
    os_version = raw_input(prompt)
    os_versions = []
    for i in range(0, MAX_OS, 1):
        os_versions.append(str(i + 1) + '.')

    for z in range(0, MAX_OS, 1):
        if os_version.startswith(os_versions[z]):
            return os_version

    print "\nPlease enter a proper OS. Available options are: ", os_versions

    return get_os_upgrade(brand, MAX_OS)



def get_burn_in_duration():
    my_prompt = 'How many hours is the burn in running for? '
    my_confirmation = 'About to use hour count of: '
    return get_information(my_prompt, my_confirmation)



def get_inventory():
    my_prompt = 'Did you take inventory and verify the entire shipment arrived?[yes/no] '
    my_confirmation = 'About to use value of: '
    return get_information(my_prompt, my_confirmation)


def get_damage_assesment():
    my_prompt = 'Are there damages to the devices or box? '
    my_confirmation = 'About to submit: '
    return get_information(my_prompt, my_confirmation)


def email_questions(engineer_name):
    to = []
    sender = []
    sender.append(engineer_name)
    my_prompt = 'What is your e-mail? '
    my_confirmation = 'Your e-mail is: '
    sender.append(get_information(my_prompt, my_confirmation))
    my_prompt = 'What is your Password? '
    my_confirmation = 'Your Password is: '
    sender.append(get_information(my_prompt, my_confirmation))

    # Sender Informatin:
    my_prompt = 'Who are you sending this report to? '
    my_confirmation = 'You are sending this report to: '
    to.append(get_information(my_prompt, my_confirmation))

    my_prompt = 'What is '+ to[0] + "'s e-mail? "
    my_confirmation = to[0] + "'s e-mail is: "
    sender.append(get_information(my_prompt, my_confirmation))

    return sender, to
# get_date()
# print get_equipment_model()
# get_serial_numbers()
# get_os_upgrade_pan()
# get_brand()

# get_num_of_interfaces()