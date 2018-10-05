

from questions import *
from quality_check_interfaces import *

engineer_name = get_engineer()

equipment_manufacturer = get_brand()

equipment_model = get_equipment_model()

serial_num = get_serial_number()


manufacturer_specs_url = get_device_specifications()



# Quality checks
interface_count = get_num_of_interfaces()

interface_success_percentage = check_interfaces()

