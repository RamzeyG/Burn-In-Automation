
# from ssh_automate import *
from devicetype import *
from questions import *
from quality_check_interfaces import *
from latex import *
from os_upgrade import *
from my_email_sender import *
from interface_names import *
# from ssh_automate import *
import subprocess

num_of_devices = get_num_of_devices()

engineer_name = get_engineer()

date = get_date()

file = []
for i in range(0, num_of_devices, 1):
    equipment_manufacturer = get_brand()

    os = get_os_upgrade(equipment_manufacturer, 9)

    # Quality checks
    total_interface_count = get_num_of_interfaces()

    interface_percentage = check_interfaces(total_interface_count, equipment_manufacturer)

    upgrade_os_and_license(equipment_manufacturer, os)

    equipment_model = get_equipment_model()

    serial_num = get_serial_number()

    manufacturer_specs_url = get_device_specifications()

    burn_in_time = get_burn_in_duration()

    inventory_check = get_inventory()

    damage_assement = get_damage_assesment()




    # Write to LaTex
    file.append('Burn-in-results-' + serial_num)
    f = open(file[length(file)-1] + '.tex', 'w')
    f.write(begin)
    f.write(set_title(engineer_name, date))
    f.write(set_equipment_info(equipment_manufacturer, equipment_model, serial_num))
    f.write(set_manufacturer_specs_url(manufacturer_specs_url))

    table, pass_count = set_quality_checks_table(os, damage_assement, total_interface_count * (interface_percentage / 100), interface_percentage, burn_in_time, inventory_check)
    f.write(table)

    # 5 tests were checked
    f.write(set_ending(5, pass_count))
    f.write(end_document())
    f.close()

    #generate PDF
    proc = subprocess.Popen(['pdflatex', file + '.tex'])
    proc.communicate()

    file[length(file) - 1] = file[length(file) - 1] + '.pdf'


#
# file = []
# engineer_name = 'Ramzey Ghanaim'
# file.append('burn-in-results-016201004695.pdf')
# file.append('burn-in-results-016201004696.pdf')
# file.append('burn-in-results-016201004721.pdf')
# file.append('burn-in-results-016201004725.pdf')
# me = []
# me.append('Ramzey Ghanaim')
# me.append('rghanaim@intervision.com')
# me.append('')
#
# to = []
# to.append('Ramzey')
# # to.append('Ramon')
# to_email = []
# to_email.append('rghanaim@intervision.com')
# to_email.append('ramon.macalisang@intervision.com')
# print 'files im sending are: ', file


# send email
me, to, to_email= email_questions(engineer_name)
send_email(file, to, to_email, me, 'Burn In Results')

