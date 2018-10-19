
from devicetype import *
# from questions import get_num_of_interfaces
#       check_interfaces()
#
# This function will apply an IP address, attempt to ping and
# remove the address
def check_interfaces(num_of_interfaces, device_type):
    if 'no' in num_of_interfaces or 'n' in num_of_interfaces:
        return 0
    percentage = get_percentage()/ 100.0

    # Interface funcs are stored in interface_funcs.py
    interface_funcs[device_type](percentage, num_of_interfaces, dict_list)

    return percentage * 100




# @return: value - type int - percentage of interfaces to check (1-100)
def get_percentage():
    value = raw_input('What percentage of interfaces do you want to check? [1-100] ')

    if value.isdigit():
        value = int(value)
        if (value <= 100) and (value >= 1):
            return value
        print 'Not a valid Percentage. Try again'
        return get_percentage()
    else:
        print 'Not valid input. Please Try again.'
        return get_percentage()




# check_interfaces(10, 'pan')