import paramiko
import time
import argparse
import numpy as np
from tqdm import tqdm

# REMOVE
from devicetype import *


# Remove bad chars
import re

# used for running os commands
import pexpect

# Import my helper functions
from printer import *
from errorcheck import *
from devicetype import *
from helper_func import *

#              ssh_automate.py
# This is a simple program that ssh's into Networking devices and
# gets the interface configuration. This program requires all devices'
# ssh information reside in the file "config.txt", which should be in the
# same directory as this script.
#
# This program assumes devices are already set up for ssh (instructions
# can be found in the file "sshSetupCisco.txt" for Cisco devices)


#         my_sleep()
#
# This function puts a progress bar while sleeping
#
# @param: int time - seconds program sleeps for
def my_sleep(seconds):
	for i in tqdm(range(0, seconds, 1)):
		time.sleep(1)



#         readFile()
#
# This function parses a file for all devices
# we are going to ssh to.
#
# @param: fileName - file that contains the device list
#
# @return: numOfDevices - totalnumber of devices found
# @return: deviceList - a list of devices address, login name, password
def readFile(fileName):
	deviceList =[]
	numOfDevices = 0

	# Check if file exists in THIS directory or src/ directory
	if np.DataSource().exists(fileName):
		readfile = open(fileName, "r")
	else:
		readfile = open('src/'+fileName, "r")
	for line in readfile:
		# Remove leading and trailing spaces
		line = line.strip()

		# Skip commented out and blank lines (\n) which have a len of 2
		if not line.startswith('#') and not line.startswith('//') and len(line) > 2:
			line = line.strip("\r\n")
			line = line.split(" ")
			deviceList.append([line[0], line[1], line[2]])
			numOfDevices += 1
	return numOfDevices, deviceList


#            execute_commands()
#
# This function executes all the commands in a given ip_commands file on the ssh session.
# The session is logged to a new_file named "output-<ip address>-<hostname>.txt"
# this name is the variable new_file.
#
# @param: ip_commands - file that contains all the commands to be executed on THIS device
# @param: ssh_remote - ssh session we are using for THIS device
# @param: kevin_flag - flag that determines weather or not we are using a "kevin file"
# @param: k_file_name - If we have a kevin file, the name of the file is this variable
# @param: conf - commands to enter config mode
#
# @return: new_file - the name of the file that we save the output to.
def execute_commands(ip_commands, ssh_remote, device_name, kevin_flag, k_file_name, conf, device_brand, dict_list):
	global begin_found
	global start

	begin_found, start = check_kevin_file(k_file_name, kevin_flag, ip_commands, begin_found, start)

	new_file = 'output-' + device_name

	# Write extra new line (fixes a lot of ouput issues)
	add_extra_line(ip_commands)

	# Start executing commands
	# Check if file exists in THIS directory or src/ directory
	if np.DataSource().exists(ip_commands):
		command_list = open(ip_commands, "r")
	elif np.DataSource().exists('src/'+ip_commands):
		command_list = open('src/' + ip_commands, "r")
	else:
		print 'Cannot find configuration commands file. Exiting program'
		exit()

	# Executing config commands
	config_cmds = conf.split('\n')
	print 'about to execute config commands: ', config_cmds
	for f in range(0, len(config_cmds), 1):
		curr_cmd = print_progress(config_cmds[f])

		ssh_remote.send(config_cmds[f] + '\n')

		time.sleep(3)
		output = ssh_remote.recv(655350)
		print output
		print_cmd_completion_status(curr_cmd, output,  dict_list[1].get(device_brand))

	first_run = 1
	# Initial sleep to wait for banner to come in
	time.sleep(3)
	# executing user commands
	# print 'command list is: ' , command_list
	for line in command_list:
		cmd = line.strip()
		if 'show' in cmd:
			sleep_time = 10
		elif 'print ' in cmd:
			split = cmd.split(' ')
			print '       Please INSERT Ethernet cable into interface: ' + split[1]+ '\n'
			my_sleep(15)
			line = command_list.next()
		elif 'sleep ' in cmd:
			s_time = cmd.split(' ')
			sn_time = s_time[1]
			if sn_time.isdigit():
				sleep_time = int(sn_time)
				print '| SLEEPING FOR ' + str(sleep_time) + ' MINUTES, ONE'
				if 'sleep 10' in cmd:
					sleep_time = 10 * 60
				else:
					sleep_time = 5 * 60
			else:
				if 'sleep 10' in cmd:
					sleep_time = 10 * 60
				else:
					sleep_time = 5 * 60
					print '| SLEEPING FOR 6 MINUTES, ONE'
			line = command_list.next()
			cmd = line.strip()

			# time.sleep(sleep_time)
			my_sleep(sleep_time)
			sleep_time = 5

		else:
			sleep_time = 5

		if len(cmd) > 0 and '!' != cmd:
			# print '()())))))))))))))))))))))))))))))))))))))))))))))))))))))))()()))))()())()())()()()'

			if 'ping count' in cmd:
				sleep_time = 15
				print 'lower, 15'
			if 'commit' in cmd:
				sleep_time = 20
				print 'lower, 20'
			print 'sleep time is: ', sleep_time

			curr_cmd = print_progress(line)
			# print 'cur cmd, len is ', curr_cmd, len(curr_cmd)
			# Now we can execute commands

			ssh_remote.send(line.lstrip() + '\n')

			# time.sleep(sleep_time)
			my_sleep(sleep_time)

			# Get ssh response.
			new_output, result, new_file = get_ssh_response(ssh_remote, first_run, new_file)
			print new_output
			if first_run:
				final_result = result
				first_run = False

			# Print completion status to terminal
			print_cmd_completion_status(curr_cmd, new_output, dict_list[1].get(device_brand))

			# Write output to the output file
			final_result.write(new_output)
			# print 'wrote new output'


	if final_result is None:
		print 'ERROR. You do not have any commands in your list.'
	final_result.close()
	command_list.close()
	remove_extra_line(ip_commands)
	return new_file

#------------------------------------------------------------------------------------------------
#                      Main()
# Main program starts here


#     dict_list
#
# 0 config_mode
# 1 invalid_cmd_key
# 2 interface_funcs

def Main(args, dict_list):
	kevin_file = args.kevinfile
	single_file = args.singlefile
	device_brand = args.devicebrand

	# Check if device_brand is compatible with this program
	check_device_brand_compatability(device_brand, dict_list[1])

	# Get config commands based off device brand
	conf = dict_list[0].get(device_brand)

	# kevin flag is off by default
	kevin_flag = False

	# create an ssh session
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


	# Read in file for address, username and password
	numOfDevices, deviceList = readFile("log-in-credentials.txt")

	# Establish Global vars (used for kevin file)
	global begin_found
	global start
	start = 1  # 1
	begin_found = 0  # 0

	# check if we have a kevin_file
	if kevin_file:
		kevin_flag = True

	# List of output file names
	output_files_list = []

	# Iterate thorough all devices and execute commands
	for i in range(numOfDevices):
		print "********** Now Going into device: ", deviceList[i][0], " ************"
		# print begin_found, start
		ssh.connect(deviceList[i][0], port=22, username=deviceList[i][1], password=deviceList[i][2], look_for_keys=False)

		ssh_remote = ssh.invoke_shell()

		if single_file:
			output_file = execute_commands(single_file, ssh_remote, deviceList[i][0], kevin_flag, kevin_file, conf, device_brand, dict_list)
		else:
			output_file = execute_commands(deviceList[i][0], ssh_remote, deviceList[i][0], kevin_flag, kevin_file, conf, device_brand, dict_list)

		ssh.close()

		begin_found += 1

		output_files_list.append(output_file)


	# When complete, check all output files for errors
	error_check(device_brand, output_files_list, dict_list[1])
	# return the name of the first output file
	return output_files_list[0]


#
# parser = argparse.ArgumentParser()
# parser.add_argument('-kfile', '--kevinfile', default=None)
# parser.add_argument('-sf', '--singlefile')
# parser.add_argument('-b', '--devicebrand', default='pan')
# from interface_funcs import *
#
# #     device_type.py
# #
# # This file contains the list of supported devices,
# # and commands used by each device
#
#
# # Commands to get into config mode
# config_mode = {
# 		'cisco': 'en\nconf t\nterm len 0',
# 		'arista': 'en\nconf t\nterm len 0',
# 		'juniper': 'cli\nconfigure\nset cli screen-length 0',
# 		'pan': 'set cli pager off\nconfigure'
# }
#
#
#
# # keys used to look for "wrong command"
# # Note, multi word keys need quotes around them
# # aditional cmds: pan: Invalid syntax.
# invalid_cmd_key = {
# 	'cisco': 'Invalid',
# 	'arista': 'Invalid',
# 	'juniper': '',
# 	'pan': '"Unknown command:"\n"Invalid syntax"',
# 	'ubuntu': '"not found"'
# }
#
# def pan_interface_check():
# 	return 'heelo there'
#
#
# interface_funcs = {
# 	# 'cisco': cisco_interface_check,
# 	# 'arista': arista_interface_check,
# 	# 'juniper': juniper_interface_check,
# 	'pan': pan_interface_check,
# 	# 'ubuntu': ubuntu_interface_check
# }
#
# dict_list = []
# dict_list.append(config_mode)
# dict_list.append(invalid_cmd_key)
# dict_list.append(interface_funcs)
#
# def get_dict_list():
# 	dict_list = []
# 	dict_list.append(config_mode)
# 	dict_list.append(invalid_cmd_key)
# 	dict_list.append(interface_funcs)
#
# 	return dict_list
#
# #     dict_list
# #
# # 0 config_mode
# # 1 invalid_cmd_key
# # 2 interface_funcs
# Main(parser.parse_args(), dict_list)
