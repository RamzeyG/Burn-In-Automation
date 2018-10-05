
from ssh_automate import *

from interface_names import *
import random
#     dict_list
#
# 0 config_mode
# 1 invalid_cmd_key
# 2 interface_funcs



# @param: percentage - percentage of interfaces you want to check - deciaml form
def pan_interface_check(percentage, num_of_interfaces, dict_list):
    # print 'HERE'
    interface_name = get_interface_name_scheme('pan')
    print 'here2'
    single_file = open('pan_int_cmds.txt', 'w')
    used_ports = []
    ping_cmd = 'ping source 10.10.192.65 host www.google.com'
    port = -1
    MAX = percentage * num_of_interfaces
    print 'MAX IS: ', int(MAX)
    while len(used_ports) < int(MAX):

        # rand num in range: [1, num_of_interfaces] ( inclusive)
        port = random.randint(1, num_of_interfaces)
        if port not in used_ports:
            used_ports.append(port)
    print used_ports




    # Run ssh automation script
    #run_ssh_automation('pan')




def cisco_interface_check(percentage, num_of_interfaces, dict_list):
    print 'in CISCO'


def arista_interface_check(percentage, num_of_interfaces, dict_list):
    print 'in arista'

def juniper_interface_check(percentage, num_of_interfaces, dict_list):
    print 'in juniper'


def ubuntu_interface_check(percentage, num_of_interfaces, dict_list):
    print 'in ubuntu'



def get_args(device_type):
    parser = argparse.ArgumentParser()
    parser.add_argument('-kfile', '--kevinfile', default=None)
    parser.add_argument('-sf', '--singlefile', default=device_type+'-sf.txt')
    parser.add_argument('-b', '--devicebrand', default=device_type)

    return parser.parse_args()


def run_ssh_automation(device_type):
    Main(get_args(device_type), dict_list)