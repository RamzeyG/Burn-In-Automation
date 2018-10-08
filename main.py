

from questions import *
from quality_check_interfaces import *
from latex import *

engineer_name = get_engineer()

date = get_date()

equipment_manufacturer = get_brand()

equipment_model = get_equipment_model()

serial_num = get_serial_number()



manufacturer_specs_url = get_device_specifications()

burn_in_time = get_burn_in_duration()

# Quality checks
interface_count = get_num_of_interfaces()


interface_success_percentage = check_interfaces(interface_count, equipment_manufacturer)



# Write to LaTex
