
from ssh_automate import *


#     dict_list
#
# 0 config_mode
# 1 invalid_cmd_key
# 2 interface_funcs




def pan_interface_check(percentage, num_of_interfaces, dict_list):

    parser = argparse.ArgumentParser()
    parser.add_argument('-kfile', '--kevinfile')
    parser.add_argument('-sf', '--singlefile', default='pan-sf.txt')
    parser.add_argument('-b', '--devicebrand', default='pan')

    args = parser.parse_args()
    Main(args, dict_list)
    single_file = open('pan_int_cmds.txt', 'w')



def cisco_interface_check(percentage, num_of_interfaces, dict_list):
    print 'in CISCO'


def arista_interface_check(percentage, num_of_interfaces, dict_list):
    print 'in arista'

def juniper_interface_check(percentage, num_of_interfaces, dict_list):
    print 'in juniper'


def ubuntu_interface_check(percentage, num_of_interfaces, dict_list):
    print 'in ubuntu'
