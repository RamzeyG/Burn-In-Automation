
from questions import *
import time
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

        if 'yes' in license or 'y' in license or 'no' not in str(os) or 'n' not in str(os):
            # Replace default IP with my IP
            file = open('log-in-credentials.txt').read()
            file = file.replace('192.168.1.1', '10.10.192.66')
            f = open('log-in-credentials.txt', 'w')
            f.write(file)
            f.close()

            # Run commands on the firewall
            run_ssh_automation('pan', sf_name='os_cmd.txt')


            # Replace default IP with my IP
            file = open('log-in-credentials.txt').read()
            file = file.replace('10.10.192.66', '192.168.1.1')
            f = open('log-in-credentials.txt', 'w')
            f.write(file)
            f.close()
        else:
            f.close()

# upgrade_os('pan', '8.1.3')
