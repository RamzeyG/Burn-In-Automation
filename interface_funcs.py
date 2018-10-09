
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
    interface_name = get_interface_name_scheme('pan')
    # print 'here2'
    single_file = open('pan_int_cmds.txt', 'w')
    ping_cmd = 'ping source 10.10.192.65 host www.google.com'

    used_ports = get_used_ports(percentage, num_of_interfaces)
    used_ports.sort()

    # System cmds are device wide settings necessary for test
    system_cmds = []
    system_cmds.append('exit')
    system_cmds.append('set cli pager off')
    system_cmds.append('set cli config-output-format set')
    system_cmds.append('configure')

    # Add ntp server to obtain time
    system_cmds.append('set deviceconfig system ntp-servers primary-ntp-server ntp-server-address 0.us.pool.ntp.org')
    system_cmds.append('set deviceconfig system ntp-servers secondary-ntp-server ntp-server-address 1.us.pool.ntp.org')
    system_cmds.append('set network profiles interface-management-profile Standard-Mgmt https yes')
    system_cmds.append('set network profiles interface-management-profile Standard-Mgmt ssh yes')
    system_cmds.append('set network profiles interface-management-profile Standard-Mgmt ping yes')
    # system_cmds.append('delete network interface ethernet ethernet1/1 virtual-wire')
    # system_cmds.append('delete network interface ethernet ethernet1/2 virtual-wire')
    system_cmds.append('delete network virtual-wire default-vwire interface1')
    system_cmds.append('delete network virtual-wire default-vwire interface2')
    system_cmds.append('delete network virtual-wire default-vwire')
    system_cmds.append('delete zone trust network virtual-wire ethernet1/2')
    system_cmds.append('delete zone untrust network virtual-wire ethernet1/1')
    system_cmds.append('set zone untrust network layer3 [ ]')
    system_cmds.append('set network virtual-router default routing-table ip static-route default-route nexthop ip-address 10.10.192.1')
    system_cmds.append('set network virtual-router default routing-table ip static-route default-route destination 0.0.0.0/0')

    system_cmds.append('commit')

    ping_test_cmds = []
    ping_test_cmds.append('commit')
    ping_test_cmds.append('exit')
    ping_test_cmds.append('ping source 10.10.192.65 host www.google.com')
    ping_test_cmds.append('configure')

    for command in system_cmds:
        single_file.write(command + '\n')
    # mgmt address (don't need)
    # Default mgmt address: 192.168.1.1/24
    # system_cmds.append('set deviceconfig system ip-address 10.10.192.64')


    # Get Proper commands
    for port in used_ports:
        my_interface = interface_name + str(port)
        cmd_list = []
        cmd_list.append('network interface ethernet ' + my_interface + ' layer3 interface-management-profile Standard-Mgmt')
        cmd_list.append('network interface ethernet ' + my_interface + ' layer3 ip 10.10.192.65/21')
        cmd_list.append('network virtual-router default interface ' + my_interface)
        cmd_list.append('zone trust network layer3 ' + my_interface)
        cmd_list.append('set network virtual-router default routing-table ip static-route default-route interface '+my_interface)



        for command in cmd_list:
            single_file.write('set ' + command + '\n')

        for command in ping_test_cmds:
            single_file.write(command + '\n')

        # Delete commands
        for command in cmd_list:
            single_file.write('delete ' + command + '\n')
    single_file.close()


    # Run ssh automation script
    run_ssh_automation('pan', single_file=None)




def cisco_interface_check(percentage, num_of_interfaces, dict_list):
    print 'in CISCO'


def arista_interface_check(percentage, num_of_interfaces, dict_list):
    print 'in arista'

def juniper_interface_check(percentage, num_of_interfaces, dict_list):
    print 'in juniper'


def ubuntu_interface_check(percentage, num_of_interfaces, dict_list):
    print 'in ubuntu'



def get_args(device_type, sf_name):
    parser = argparse.ArgumentParser()
    parser.add_argument('-kfile', '--kevinfile', default=None)
    if sf_name is None:
        parser.add_argument('-sf', '--singlefile', default=device_type+'-sf.txt')
    else:
        parser.add_argument('-sf', '--singlefile', default=sf_name)
    parser.add_argument('-b', '--devicebrand', default=device_type)

    return parser.parse_args()


def run_ssh_automation(device_type, sf_name):
    Main(get_args(device_type, sf_name), dict_list)


def get_used_ports(percentage, num_of_interfaces):
    used_ports = []
    MAX = percentage * num_of_interfaces
    while len(used_ports) < int(MAX):
        # rand num in range: [1, num_of_interfaces] ( inclusive)
        port = random.randint(1, num_of_interfaces)
        if port not in used_ports:
            used_ports.append(port)
    return used_ports
