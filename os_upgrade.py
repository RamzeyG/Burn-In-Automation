from ssh_automate import *

def upgrade_os(equipment_manufacturer, os):
    if equipment_manufacturer == 'pan':
        file = open('os_cmd.txt', 'w')
        file.write('exit\n')
        file.write('request system software check\n')
        file.write('request system software download version '+os+'\n')
        file.write('sleep 5\n')
        file.write('request system software install version ' + os + '\n')
        file.write('sleep 5\n')
        file.write('request restart system\n')

        file.close()

        run_ssh_automation('pan', sf_name='os_cmd.txt')
