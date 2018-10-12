
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

engineer_name = get_engineer()

date = get_date()

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
file = 'Burn-in-results-' + serial_num
f = open(file + '.tex', 'w')
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

# send email
sender, recv = email_questions(engineer_name)
send_email(file + '.pdf', recv, sender, 'Burn In')

