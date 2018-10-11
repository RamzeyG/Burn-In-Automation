
from questions import *
import time
# from quality_check_interfaces import *

def upgrade_os(equipment_manufacturer, os):
    if equipment_manufacturer == 'pan':
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
        file.write('request system software check\n')
        file.write('request system software download version '+os+'\n')
        file.write('sleep 5\n')
        file.write('request system software install version ' + os + '\n')
        file.write('y\n')
        file.write('sleep 5\n')
        file.write('request restart system\n')
        file.write('y\n')

        file = open('log-in-credentials.txt').read()
        file = file.replace('192.168.1.1', '10.10.192.66')
        f = open('log-in-credentials.txt', 'w')
        f.write(file)
        f.close()

        run_ssh_automation('pan', sf_name='os_cmd.txt')


# upgrade_os('pan', '8.1.3')
