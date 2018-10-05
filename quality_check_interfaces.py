
from devicetype import *

#       check_interfaces()
#
# This function will apply an IP address, attempt to ping and
# remove the address
def check_interfaces(num_of_interfaces, device_type):
    percentage = num_of_interfaces/100.0

    # Interface funcs are stored in interface_funcs.py
    interface_funcs[device_type](percentage, num_of_interfaces, dict_list)



check_interfaces(10, 'pan')