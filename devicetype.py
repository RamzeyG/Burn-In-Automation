from interface_funcs import *

#     device_type.py
#
# This file contains the list of supported devices,
# and commands used by each device


# Commands to get into config mode
config_mode = {
		'cisco': 'en\nconf t\nterm len 0',
		'arista': 'en\nconf t\nterm len 0',
		'juniper': 'cli\nconfigure\nset cli screen-length 0',
		'pan': 'set cli pager off\nconfigure'
}



# keys used to look for "wrong command"
# Note, multi word keys need quotes around them
# aditional cmds: pan: Invalid syntax.
invalid_cmd_key = {
	'cisco': 'Invalid',
	'arista': 'Invalid',
	'juniper': '',
	'pan': '"Unknown command:"\n"Invalid syntax"',
	'ubuntu': '"not found"'
}


interface_funcs = {
	'cisco': cisco_interface_check,
	'arista': arista_interface_check,
	'juniper': juniper_interface_check,
	'pan': pan_interface_check,
	'ubuntu': ubuntu_interface_check
}

dict_list = []
dict_list.append(config_mode)
dict_list.append(invalid_cmd_key)
dict_list.append(interface_funcs)

def get_dict_list():
	dict_list = []
	dict_list.append(config_mode)
	dict_list.append(invalid_cmd_key)
	dict_list.append(interface_funcs)

	return dict_list

#     dict_list
#
# 0 config_mode
# 1 invalid_cmd_key
# 2 interface_funcs