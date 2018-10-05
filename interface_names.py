

def get_options_pan():
    options = {
        1: 'ethernet1/'
    }
    return options


def get_options_cisco():
    options = {
        1: 'ethernet1/'
    }

    return options




option_types = {
    'pan': get_options_pan,
    'cisco': get_options_cisco
}


def get_interface_name_scheme(device):
    options = option_types[device]()
    length = len(options)
    prompt = "Please select a name scheme you want (1-" + str(length)+")"
    print prompt
    for z in range(1, length+1, 1):
        print str(z) + ") " + options.get(z)
    user_choice = raw_input('\n')
    if user_choice.isdigit():
        num = int(user_choice)
        if (num > 0) and (num <= length):
            return options.get(num)
        print 'Invalid Number. Please enter a valid number.\n\n '
        return get_interface_name_scheme(device)
    else:
        print 'Not a Number. Please enter a valid number.\n\n '
        return get_interface_name_scheme(device)



# get_interface_name_scheme('pan')