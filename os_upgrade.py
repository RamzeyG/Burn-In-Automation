
from questions import *
import time
# import re # remove extra whitepace
# from quality_check_interfaces import *

# Upgrade OS and pull license.
def upgrade_os_and_license(equipment_manufacturer, os):
    if equipment_manufacturer == 'pan':

        license = raw_input('\n\n Do you want to install licences? [yes/no] ')
        if 'yes' in license or 'y' in license or 'no' not in str(os) or 'n' not in str(os):
            file = open('os_cmd.txt', 'w')
            file.write('set deviceconfig system ip-address 10.10.192.66\n')
            file.write('set deviceconfig system netmask 255.255.248.0\n')
            file.write('set deviceconfig system default-gateway 10.10.192.1\n')
            file.write('set deviceconfig system dns-setting servers primary 8.8.8.8 secondary 8.8.8.8\n')
            file.write('set deviceconfig system ntp-servers primary-ntp-server ntp-server-address 0.us.pool.ntp.org\n')
            file.write('set deviceconfig system ntp-servers secondary-ntp-server ntp-server-address 1.us.pool.ntp.org\n')
            file.write('commit\n')


            file.close()
            # run_ssh_automatino is not defined.....
            run_ssh_automation('pan', sf_name='os_cmd.txt')
            print '\n\n              PLEASE Plug Management port into the Wall!!! You have 15 seconds...'
            time.sleep(15)
        file = open('os_cmd.txt', 'w')
        file.write('exit\n')
        if 'yes' in license or 'y' in license:
            # Global protect
            version_gp = raw_input('\n\n What Global Protect version do you want? [version/no] ')

            # All Licenses
            file.write('request license fetch\n')
            if 'no' not in version_gp or 'n' != version_gp:
                file.write('request global-protect-client software check\n')
                file.write('request global-protect-client software download version ' + version_gp)
                file.write('sleep 2\n')
                file.write('request global-protect-client software activate version ' + version_gp + '\n')
                file.write('y\n')


        # OS update
        if 'no' not in str(os) or 'n' not in str(os):
            file.write('request system software check\n')
            file.write('request system software download version '+str(os)+'\n')
            file.write('sleep 6\n')
            file.write('request system software check\n')
            file.write('request system software install version ' + str(os) + '\n')
            file.write('y\n')
            file.write('sleep 10\n')
            file.write('set deviceconfig system ip-address 192.168.1.1\n')
            file.write('set deviceconfig system netmask 255.255.255.0\n')
            file.write('set deviceconfig system default-gateway 192.168.1.0\n')
            file.write('commit\n')
            file.write('request restart system\n')
            file.write('y\n')
            file.close()
        if 'yes' in license or 'y' in license or 'no' not in str(os) or 'n' not in str(os):
            # Replace default IP with my IP
            file_login = open('log-in-credentials.txt').read()
            file_login = file_login.replace('192.168.1.1', '10.10.192.66')

            f = open('log-in-credentials.txt', 'w')
            f.write(file_login)
            f.close()
            # file_login.close()

            # Run commands on the firewall
            run_ssh_automation('pan', sf_name='os_cmd.txt')


            # Replace default IP with my IP
            file_login = open('log-in-credentials.txt').read()
            file_login = file_login.replace('10.10.192.66', '192.168.1.1')
            f = open('log-in-credentials.txt', 'w')
            f.write(file_login)
            f.close()
            file_login.close()
        else:
            file.close()
    elif equipment_manufacturer == 'aruba':
        if 'no' not in str(os) or 'n' not in str(os):
            get_aruba_boot_partition()
            ip = raw_input('What is the IP address of the SCP server? ')
            uname = raw_input('What is the user name of the SCP server? ')
            passwd = raw_input('What is the password of the SCP server? ')
            file = open('os_cmd.txt', 'w')
            partition = get_aruba_boot_partition()
            file.write('copy scp: '+ip + ' ' + uname + ' ' + passwd + ' system partition '+partition+'\n')
            # file.write('')
            file.close()

# upgrade_os('pan', '8.1.3')


def get_aruba_boot_partition():
    boot_part_file = open('boot_cmd.txt', 'w')
    boot_part_file.write('show boot\n')
    boot_part_file.close()
    output = run_ssh_automation('aruba', sf_name='boot_cmd.txt')

    file = open(output, 'r')
    for line in file:
        if 'partition' in line:
            print "Line is ", line
            if '1' in line:
                return '0'
            else:
                return '1'
    file.close()